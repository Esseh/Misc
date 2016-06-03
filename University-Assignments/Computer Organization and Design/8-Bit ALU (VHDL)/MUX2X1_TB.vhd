library ieee;
use ieee.std_logic_1164.all;

entity MUX2X1_TB is
end MUX2X1_TB;

architecture TB of MUX2X1_TB is
	component MUX2X1 is
	port(	b,binv: in std_logic;
		output: out std_logic
	);
	end component;
	
	signal i1,i2,o1 : std_logic;
	
	begin
		mapping: MUX2X1 port map (i1,i2,o1);
	
	process
		begin
			--case 0
			i1 <= '0';
			i2 <= '0';
			wait for 10 ns;
			assert (o1='0') report "Incorrect Output" severity warning;
	
			--case 1
			i1 <= '0';
			i2 <= '1';
			wait for 10 ns;
			assert (o1='1') report "Incorrect Output" severity warning;
			
			--case 2
			i1 <= '1';
			i2 <= '0';
			wait for 10 ns;
			assert (o1='1') report "Incorrect Output" severity warning;
			
			--case 3
			i1 <= '1';
			i2 <= '1';
			wait for 10 ns;
			assert (o1='0') report "Incorrect Output" severity warning;
			
			wait;
	end process;
end TB;

configuration CFG_TB of MUX2X1_TB is
		for TB
		end for;
end CFG_TB;