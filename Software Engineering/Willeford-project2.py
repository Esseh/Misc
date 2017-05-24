# This program implements a command line interface per the instructions of Alex's Project2.pdf.
# To execute the program from command line "python Willeford-project2.py"
# Running the program will require the python 2.x interpreter.

# Separates a string into two parts delimited on the first space.
def input_pair(input):
	split_input = input.split()
	command   = split_input[0]
	remainder = " ".join(split_input[1:])
	return command,remainder
	
# Interface Representing a Notifiable (Observer) Object
class notifiable_interface:
	def __init__(self, name):
		# Message Container
		self._message = []
		# Unique Identifier
		self._name = name
	# Destructor, Cleans up local objects.
	def __del__(self): 
		self._name = None
		self._message = None
	def get_name(self): return self._name
	# Returns the most recent message.
	def get_messages(self): return self._message[:1]
	# Appends a message making it the most recent.
	def notify(self,msg): self._message = [msg] + self._message

# Interface Representing a Composite (Leaf Node)
class composite_leaf_interface:
	def __init__(self): pass
	def is_leaf(self): return True
	
# Interface Representing a Composite (Inner Node)
class composite_inner_interface:
	def __init__(self, parent):
		self._parent = parent
		self._children = {}
	# Destructor, also recursively calls the destructor of its children and cleans up locals.
	def __del__(self):
		for i in self._children:
			self._children[i].__del__()
			self._parent = None
			self._children = None
	# Adds child assuming it doesn't already exist.
	def add_child(self,key,new_child):
		i = self._children.get(new_child.get_name(),None)
		if i == None: self._children[new_child.get_name()] = new_child
	# Deletes a child and calls its destructor if possible.
	def delete_child(self,key):
		i = self._children.get(key,None)
		if i != None:
			i.__del__()
			self._children.pop(key)
	def is_leaf(self): 		return False
	def get_parent(self): 	return self._parent
	def get_child(self,key):return self._children.get(key,None)


# The component part of the organization composite. 
# It's identity is defined by being a notifiable object, as such the entire composite is a notifiable object.
class organization_component(notifiable_interface):
	def __init__(self, name):
		notifiable_interface.__init__(self, name)
		
# The inner part of the organization composite.
class organization_inner(organization_component,composite_inner_interface):
	def __init__(self,name="root",parent=None):
		organization_component.__init__(self,name)
		composite_inner_interface.__init__(self,parent)
	
# Leaf of organization composite
class user(organization_component,composite_leaf_interface):
	def __init__(self,name):
		organization_component.__init__(self,name)
		composite_leaf_interface.__init__(self)
		
# the observer subject. Carries a list of observers. 
# It is slightly specialized as it handles composite observers which requires an additional "is_leaf()" to fulfill the interface.
class listserv:
	def __init__(self, name):
		# Unique Identifier
		self._name = name
		# List of Messages
		self._message = []
		# List of Composite Observers
		self._observers = {}
	def get_name(self): return self._name
	# Registers a new observer making sure not to duplicate entries.
	def register_observer(self,new_observer):
		i = self._observers.get(new_observer.get_name(),None)
		if i == None:
			self._observers[new_observer.get_name()] = new_observer
			# If the observer isn't a leaf node then recursively register it's children.
			if new_observer.is_leaf() != True:
				for key in new_observer._children:
					self.register_observer(new_observer._children[key])
	# Removes an existing observer, assumes success.
	def unregister_observer(self,name):
		i = self._observers.get(name,None)
		if i != None:
			self._observers.pop(name)
			# If the observer isn't a leaf node then recursively unregister it's children.
			if i.is_leaf() != True:
				for key in i._children: self.unregister_observer(i._children[key].get_name())
	def notify_observers(self,msg):
		# Notify each observer.
		for i in self._observers: self._observers[i].notify(msg)
		# Add message for book keeping.
		self._message = [msg] + self._message
	# Displays the most recent message of this listserv.
	def get_messages(self): return self._message[:1]

# The Object Representing the Command Line Interface of the program
class driver_header:
	def __init__(self):
		# The current "location" of the command line
		self._context = organization_inner() 
		# The group of listserv for notification
		self._listserves = {}
	def list_subscribers(self,input):
		# Get listserv
		i = self._listserves.get(input,None)
		if i != None:
			totMsg = ""
			# collect names of subscribers
			for j in i._observers: totMsg += i._observers[j].get_name() + " "
			print str(len(i._observers)) + " observers"
			print totMsg
	# Creates a listserv
	def build_list(self,input):
		# Attempt to Get listserv
		i = self._listserves.get(input,None)
		# Create listserv
		if i == None: self._listserves[input] = listserv(input)
	# subscribes organization or user to listserv
	def subscribe(self,input):
		command,remainder = input_pair(input)
		# get listserv
		this_listserv = self._listserves.get(command,None)
		if this_listserv != None:
			# get new subscriber
			this_subscriber = self._context.get_child(remainder)
			if this_subscriber != None:
				# register the subscriber and its children
				this_listserv.register_observer(this_subscriber)
	# unsubscribes organization or user to listserv
	def unsubscribe(self,input):
		command,remainder = input_pair(input)
		# get listserv
		this_listserv = self._listserves.get(command,None)
		if this_listserv != None:
			# get subscriber
			this_subscriber = self._context.get_child(remainder)
			if this_subscriber != None:
				# remove subscribers and their children from subscription
				this_listserv.unregister_observer(this_subscriber.get_name())
	# tells a listserv to notify its subscribers
	def notify(self,input):
		command,remainder = input_pair(input)
		# get listserv
		i = self._listserves.get(command,None)
		# notify observer
		if i != None: i.notify_observers(remainder)
	# displays most recent messages of a user from each listserv they are registered in
	def display(self,input):
		# For each listserv...
		for i in self._listserves:
			# Check if the user is in...
			u = self._listserves[i]._observers.get(input,None)
			if u != None:
				# And if so then print the most recent message.
				print self._listserves[i].get_name() + " messages " + " ".join(self._listserves[i].get_messages())
	# Creates a new Organization
	def make_organization(self,input):
		self._context.add_child(input,organization_inner(input,self._context))	
	# Creates a new User
	def create_user(self,input):
		self._context.add_child(input,user(input))
	# Changes the current directoryy
	def change_directory(self,input):
		# Parent Case
		if input == "..":
			res = self._context.get_parent()
			if res != None: self._context = res
		# General Case
		else:
			result = self._context.get_child(input)
			if result != None: self._context = result
	# Deletes a Child Element (The delete cascades through destructors)
	def delete_child(self,input):
		self._context.delChild(input)
	# Lists all items in the directory
	def list_directory(self,input):
		totalMsg = ""
		# From current directory get the names of all children.
		for i in self._context._children:
			totalMsg += self._context._children[i].get_name() + " "
		print totalMsg
	# Parses and executes a command line command.
	def run_command(self,input):
		if input == "": return
		command,remainder = input_pair(input)
		instruction = {
			"listsubs": self.list_subscribers,
			"buildlist": self.build_list,
			"subscribe": self.subscribe,
			"unsubscribe": self.unsubscribe,
			"notify": self.notify,
			"display": self.display,
			"mkorg": self.make_organization,
			"create": self.create_user,
			"cd": self.change_directory,
			"del": self.delete_child,
			"ls": self.list_directory
		}.get(command,None)
		if instruction != None: instruction(remainder)

# Execute The Program
def main():
	input = ""
	# create the driver object
	h = driver_header()
	# run example 2 commands
	create_directory(h)
	# run example 3 commands
	test_commands(h)
	# enter interactive command prompt
	print "command line active"
	while input != "exit":
		input = raw_input()
		h.run_command(input)
main()