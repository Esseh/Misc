#==============================================================================
# ** ConnectedMaps
#------------------------------------------------------------------------------
#  This mod allows maps to be connected via note tags. If a note tag doesn't
#  exist (-1) then transfers can't occur.
#  Part of the responsibility is on the user to make sure their connected
#  maps are of consistent size.
#
#   To use this feature simply put corresponding note tags into your map notes.
#   <left:map_id><right:map_id><down:map_id><up:map_id>
#   For example..
#   <left:1>
#   Will transfer to the right side of map 1 when you reach the 'left side' of
#   you current room.
#   The script 'assumes' that both maps are the same size.
#   As such it is your responsibility to be consistent.
#   Simply omit tags not to use the feature.
#==============================================================================
module RPG
  class Map
    #Data only needs to be computed once per room.
    def left; @left ||= parse_direction(/<left:s*(\d+)>/i); end
    def right; @right ||= parse_direction(/<right:s*(\d+)>/i); end
    def down; @down ||= parse_direction(/<down:s*(\d+)>/i); end
    def up; @up ||= parse_direction(/<up:s*(\d+)>/i); end
    def parse_direction(regex)
    res = self.note.match(regex)#Match the regex to the string.
    return -1 unless res;return res[1].to_i; end #-1 if nothing, otherwise int.
  end
end
#The part that performs the actual transfers.
  module ConnectedMaps
    def self.transferCheck
      if $game_player.x == 0 && $game_player.direction == 4 && $game_map.map.left != -1
      $game_player.reserve_transfer($game_map.map.left, $game_map.width - 1, $game_player.y, 4); end      
      if $game_player.y == 0 && $game_player.direction == 8 && $game_map.map.up != -1
      $game_player.reserve_transfer($game_map.map.up, $game_player.x, $game_map.height - 1, 8); end      
      if $game_player.y == $game_map.height - 1 && $game_player.direction == 2 && $game_map.map.down != -1
      $game_player.reserve_transfer($game_map.map.down, $game_player.x, 0, 2); end
      if $game_player.x == $game_map.width - 1 && $game_player.direction == 6 && $game_map.map.right != -1
      $game_player.reserve_transfer($game_map.map.right, 0, $game_player.y, 6); end
    end
  end

# This allows access to the @map instance variable.
class Game_Map; attr_reader :map; end 
#Inject Script
class Scene_Map 
  alias_method :conMap, :update
  def update
		ConnectedMaps.transferCheck if Graphics.frame_count % 15 == 0 #
    conMap
  end
end