#==============================================================================
# ** 8 Way Movement + Directional Input
#------------------------------------------------------------------------------
# Allows 8 Way Movement and Keeps Track of DI.
#
#==============================================================================
class Game_Player < Game_Character
#Instance Variables
  def iframes; @iframes ||= 0; end  #Amount of frames to hold onto the buffer.
  def iframes=(x); @iframes = x; end
  def input_buffer; @input_buffer ||= ""; end #The input buffer
  def input_buffer=(x); @input_buffer = x; end
#Uses two level logic to determine if the apropriate movement has been made.
  def directionalInput
    temp = self.input_buffer[self.input_buffer.length-4,self.input_buffer.length-1]
    $game_variables[1] = temp
    return "circle" if (temp == "DRUL") || (temp == "DLUR") || (temp == "RDLU") || (temp == "RULD") || (temp == "LDRU") || (temp == "LURD") || (temp == "URDL") || (temp == "ULDR")
    temp = self.input_buffer[self.input_buffer.length-3,self.input_buffer.length-1]
    return "half"   if (temp == "DRU") || (temp == "DLU") || (temp == "RDL") || (temp == "RUL") || (temp == "LDR") || (temp == "LUR") || (temp == "URD") || (temp == "ULD")
    temp = self.input_buffer[self.input_buffer.length-2,self.input_buffer.length-1]
    return "back forward" if (temp == "LR") || (temp == "RL") || (temp == "UD") || (temp == "DU")
    return "neutral"
  end
# Exactly What it Says on the Tin, Replaces it with a useless string so at to avoid length errors.
  def flush_buffer; self.input_buffer = "AAAA"; end
#Hard to Read So Placed it in a Method to increase readability.
  def clean_buffer; self.input_buffer = self.input_buffer[self.input_buffer.length-4,self.input_buffer.length-1]; end
#Repeated Self a bit so Refactored adding to the buffer.
  def buffer(x) 
      $game_player.iframes = 30 if $game_player.iframes == 0
      unless self.input_buffer[-1]==x
        self.input_buffer << x 
      end
  end
#Extends Buffer Time if Needed
  def eb; self.iframes += 15; end;
#8-way movement
  def move_by_input
    unless !movable? || $game_map.interpreter.running?
        if Input.dir8 > 0
       preMove
       case Input.dir8
         when 2; move_straight(Input.dir4) 
         when 4; move_straight(Input.dir4) 
         when 6; move_straight(Input.dir4) 
         when 8; move_straight(Input.dir4) 
         when 1; move_diagonal(4, 2)
         when 3; move_diagonal(6, 2)
         when 7; move_diagonal(4, 8)
         when 9; move_diagonal(6, 8)
       end
     end
   end
 end
#Modularized Methods that Encapsulates pre-movement actions and their variables.
  def pmVar; @pmVar ||= []; end
  def preMove
#Insert Pre-move stuff here.
  end  
end
#Modularized Code Section to Get Input and place into the buffer
def getInput
    $game_player.clean_buffer if $game_player.input_buffer.length > 10
    $game_player.flush_buffer if $game_player.iframes == 0
    case Input.dir8
      when 2; $game_player.buffer('D')
      when 4; $game_player.buffer('L')
      when 6; $game_player.buffer('R')
      when 8; $game_player.buffer('U')
    end
    $game_player.iframes -= 1 if $game_player.iframes > 0  
end
#Hook into update to clear buffer when frames run out.
class Scene_Map 
  alias_method :dirInput, :update
  def update
    getInput
    dirInput     
  end
end
#Call as extend_buffer in a script call to extend the buffer time.
def extend_buffer; $game_player.eb; end
#Alias to concisely call the directional input for use in script calls
def di(x); $game_player.directionalInput == x; end
