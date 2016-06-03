Step 0. - COMPLETE - Goal 2/12/16 | Completed 2/16/16
	Make sure the engine works on everyone's system.							(DONE)
Step 1. - COMPLETE  - Goal 2/22/16 | Completed 2/22/16
	Minimum Viable Product - 
		API-
			PressKey(string)/ReleaseKey(string) for player control API (Kenneth)(DONE)
				possible inputs-
					Up
					Down
					Left
					Right
					W
					A
					S
					D
		Isocolese Triangle for Player		(Davis/Brian)						(COMPLETE)
			Required API-
				MakePlayer()				(Davis/Brian)						(COMPLETE)
		Moves Left,Right,Up,Down			(Davis/Brian)						(COMPLETE)
			Requipred API-
					PlayerControl() (Davis/Brian) 								(COMPLETE)
							//Utilizing PressKey(string) and ReleaseKey(string)
							//Extend functionality with stretch goal 
		Stretch Goals- Goal 
			'Deceleration' when movement ends.							   
			
Step 2. - WORKING - Goal 3/22/16 | Completed 3/22/16
	Refactor Backend to allow for diverse behavior. (KENNETH)
	REFACTOR BACKEND BY BREAKING UP CONTAINERS
	Player Pointer
	AllyContainer
	EnemyContainer
	Player:
		Takes Damage if Collide with Enemy
	Enemy:
		Takes Damage if Collide with Player/Ally
	Ally:
	Takes Damage if Collide with Enemy
	
	