#==============================================================================
# ** ParallelManager
#------------------------------------------------------------------------------
#  This module makes it easy to control parallel processed events.
#  Just add to the hash. The entry format is explained on line 9.
#==============================================================================
module ParallelManager
	def self.run
    events = {12=>[[37,13]]} # frames_apart => [[event_id,condition],...]
		events.each do |key,value|					    #Check Hash
			if Graphics.frame_count % key == 0		    #If correct frame...
				value.each do |event,switch|			#... then iterate through values...
					if (switch == 0) || ($game_switches[switch] == true) # ... if corresponding condition is fulfilled ...
						$game_temp.reserve_common_event(event)           #... run each event.
					end
				end
			end
		end
	end
end
#inject Script
class Scene_Map 
  alias_method :pManager, :update
  def update; ParallelManager.run; pManager; end
end