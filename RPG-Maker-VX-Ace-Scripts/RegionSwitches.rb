#==============================================================================
# ** RegionSwitch
#------------------------------------------------------------------------------
# Updates a Switch when the player touches a region_id on a given map_id with a
# possible condition.
# This can be used to begin an event by 'region.'
# Format given in line 11
#==============================================================================
module RegionSwitch
	def self.check
	regionMap = {} # region_id => [[map_id,switch_activated,switch_required],...]
                
		regionMap.each do |key , value|
			if $game_player.region_id == key
				value.each do |mapCheck,switch,condition|
					if ($game_map.map_id == mapCheck && (condition == 0 || $game_switches[condition] == true))
						$game_switches[switch] = true
					end
				end
			end
		end
	end
end
#Inject Script
class Scene_Map 
  alias_method :regSwitch, :update
  def update
		RegionSwitch.check if Graphics.frame_count % 15 == 0 
    regSwitch     
  end
end