library ieee;
use ieee.std_logic_1164.all;

entity ADD_TB is
end ADD_TB;

architecture TB of ADD_TB is
	component ADD is
	port(	a,b,cin: in std_logic;
			sum,cout: out std_logic
	);
	end component;

	signal a1,b1,cin1,sum1,cout1 : std_logic;


	begin
		mapping: ADD port map(a1,b1,cin1,sum1,cout1);
		
	process
		begin
			--case 000
			a1   <= '0';
			b1   <= '0';
			cin1 <= '0';			
			wait for 10 ns;
			assert(cout1 = '0') 
			report "incorrect cout" severity warning;
			assert(sum1 = '0') 
			report "Incorrect sum"  severity warning;
			
			--case 001
			a1   <= '0';
			b1   <= '0';
			cin1 <= '1';			
			wait for 10 ns;
			assert(cout1 = '0') 
			report "incorrect cout" severity warning;
			assert(sum1 = '1') 
			report "Incorrect sum"  severity warning;
			
			--case 010
			a1   <= '0';
			b1   <= '1';
			cin1 <= '0';			
			wait for 10 ns;
			assert(cout1 = '0') 
			report "incorrect cout" severity warning;
			assert(sum1 = '1') 
			report "Incorrect sum"  severity warning;
	
			--case 011
			a1   <= '0';
			b1   <= '1';
			cin1 <= '1';			
			wait for 10 ns;
			assert(cout1 = '1') 
			report "incorrect cout" severity warning;
			assert(sum1 = '0') 
			report "Incorrect sum"  severity warning;
			
			--case 100
			a1   <= '1';
			b1   <= '0';
			cin1 <= '0';			
			wait for 10 ns;
			assert(cout1 = '0') 
			report "incorrect cout" severity warning;
			assert(sum1 = '1') 
			report "Incorrect sum"  severity warning;
			
			--case 101
			a1   <= '1';
			b1   <= '0';
			cin1 <= '1';			
			wait for 10 ns;
			assert(cout1 = '1') 
			report "incorrect cout" severity warning;
			assert(sum1 = '0') 
			report "Incorrect sum"  severity warning;
			
			--case 110
			a1   <= '1';
			b1   <= '1';
			cin1 <= '0';			
			wait for 10 ns;
			assert(cout1 = '1') 
			report "incorrect cout" severity warning;
			assert(sum1 = '0') 
			report "Incorrect sum"  severity warning;
			
			--case 111
			a1   <= '1';
			b1   <= '1';
			cin1 <= '1';			
			wait for 10 ns;
			assert(cout1 = '1') 
			report "incorrect cout" severity warning;
			assert(sum1 = '1') 
			report "Incorrect sum"  severity warning;
			
			wait;
	end process;
end TB;

configuration CFG_TB of ADD_TB is
		for TB
		end for;
end CFG_TB;