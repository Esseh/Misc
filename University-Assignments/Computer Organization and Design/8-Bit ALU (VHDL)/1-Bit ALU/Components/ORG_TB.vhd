library ieee;
use ieee.std_logic_1164.all;

entity ORG_TB is
end ORG_TB;

architecture TB of ORG_TB is
	component ORG is
	port(	x1,x2: in std_logic;
			y1: out std_logic);
	end component;
	
	signal i1,i2,o1 : std_logic;
	
	begin
		mapping: ORG port map (i1,i2,o1);
	
	process
		begin
			--case 0
			i1 <= '0';
			i2 <= '0';
			wait for 10 ns;
			assert(o1 = '0')
			report "incorrect output" severity warning;			
			--case 1
			i1 <= '0';
			i2 <= '1';
			wait for 10 ns;
			assert(o1 = '1')
			report "incorrect output" severity warning;
			--case 2
			i1 <= '1';
			i2 <= '0';
			wait for 10 ns;
			assert(o1 = '1')
			report "incorrect output" severity warning;
			--case 3
			i1 <= '1';
			i2 <= '1';
			wait for 10 ns;
			assert(o1 = '0')
			report "incorrect output" severity warning;
			wait;
	end process;
end TB;

configuration CFG_TB of ORG_TB is
		for TB
		end for;
end CFG_TB;