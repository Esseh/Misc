library ieee;
use ieee.std_logic_1164.all;

entity NEG_TB is
end NEG_TB;

architecture TB of NEG_TB is
	component NEG is
	port(	x1: in std_logic;
			y1: out std_logic);
	end component;
	
	signal i1,o1 : std_logic;
	
	begin
		mapping: NEG port map (i1,o1);
	
	process
		begin
			--case 0
			i1 <= '0';
			wait for 10 ns;
			assert(o1 = '1')
			report "incorrect output" severity warning;			
			--case 1
			i1 <= '1';
			wait for 10 ns;
			assert(o1 = '0')
			report "incorrect output" severity warning;
			wait;
	end process;
end TB;

configuration CFG_TB of NEG_TB is
		for TB
		end for;
end CFG_TB;