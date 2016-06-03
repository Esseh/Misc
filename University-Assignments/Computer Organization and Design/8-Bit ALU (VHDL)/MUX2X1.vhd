--MUX2X1 Implementation by Kenneth Willeford
--The purpose of this particular MUX is to invert our 'b' input
--If our control signal binv is on. 
--Let's Look at our truth table.
-- b	binv	output
-- 0	0		0
-- 0	1		1
-- 1	0		1
-- 1	1		0
--
-- Our true values break down into the following two level logic..
-- (Not b AND binv) OR (b AND NOT binv)
-- Which breaks down to  b XOR binv
-- Thus we can actualize this with a single XOR gate.  
library ieee;
use ieee.std_logic_1164.all;

entity MUX2X1 is
port(	b,binv: in std_logic;
		output: out std_logic
);
end MUX2X1;

architecture struct of MUX2X1 is
	
   component XORG is
   port( x1,x2: in std_logic;
         y1: out std_logic
	);
   end component;
   
begin
	map_XOR_gate: XORG port map (b,binv,output); -- Invert B
	
end struct;