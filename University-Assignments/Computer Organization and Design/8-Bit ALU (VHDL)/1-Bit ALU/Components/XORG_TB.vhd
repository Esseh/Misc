library ieee;
use ieee.std_logic_1164.all;

entity XORg_TB is
end XORg_TB;

architecture TB of XORg_TB is
	component XORg is
	port(	x1,x2: in std_logic;
			y1: out std_logic);
	end component;
	
	signal i1,i2,o1 : std_logic;
	
	begin
		mapping: XORg port map (i1,i2,o1);
	
	process
		begin
			--case 0
			i1 <= '0';
			i2 <= '0';
			wait for 10 ns;
	
			--case 1
			i1 <= '0';
			i2 <= '1';
			wait for 10 ns;
			
			--case 2
			i1 <= '1';
			i2 <= '0';
			wait for 10 ns;
			
			--case 3
			i1 <= '1';
			i2 <= '1';
			wait for 10 ns;
			
			wait;
	end process;
end TB;

configuration CFG_TB of XORg_TB is
		for TB
		end for;
end CFG_TB;