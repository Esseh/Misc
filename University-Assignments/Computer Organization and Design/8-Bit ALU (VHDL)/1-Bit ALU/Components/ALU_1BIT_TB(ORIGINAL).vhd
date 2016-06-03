--Test Bench Program for ALU_1BIT
--By Kenneth Willeford
--This module will take in 2 inputs, a carry in, a control signal, 
-- Given 00 it will send out the 'and' of the inputs.
-- Given 01 it will send out the 'or' of the inputs.
-- Given 10 it will give out the sum of the inputs. 
-- Given 11 it will give out '0'.
-- It will send out the carry out of the sum regardless of signal.
-- All values will be calculated and then a result chosen.
-- There are 96 possible test cases.
-- So I will use 2 of each signal test instead.

library ieee;
use ieee.std_logic_1164.all;

entity ALU_1BIT_TB is
end ALU_1BIT_TB;

architecture TB of ALU_1BIT_TB is
	component ALU_1BIT is
	port(	a,b,cin,sig0,sig1: in std_logic;
			result,cout: out std_logic
	);
	end component;

	signal a,b,cin,bit0,bit1,result,cout : std_logic;


	begin
		mapping: ALU_1BIT port map(a,b,cin,bit0,bit1,result,cout);
		
	process
		begin
			---------------------------
			bit1   <= '0'; -- and test
			bit0   <= '0';
			a <= '0';
			b <= '1';
			cin <= '0';
			wait for 10 ns;
			assert(cout = '0') 
			report "incorrect cout" severity warning;
			assert(result = '0') 
			report "incorrect result" severity warning;			
			a <= '1';
			b <= '1';
			cin <= '1';			
			wait for 10 ns;			
			assert(cout = '0') 
			report "incorrect cout" severity warning;	
			assert(result = '1') 
			report "incorrect result" severity warning;						
			---------------------------			
			bit1   <= '0'; -- or test
			bit0   <= '1';
			a <= '0';
			b <= '1';
			cin <= '0';
			wait for 10 ns;
			assert(cout = '0') 
			report "incorrect cout" severity warning;			
			assert(result = '1') 
			report "incorrect result" severity warning;						
			a <= '1';
			b <= '1';
			cin <= '1';			
			wait for 10 ns;
			assert(cout = '0') 
			report "incorrect cout" severity warning;		
			assert(result = '1') 
			report "incorrect result" severity warning;						
			---------------------------			
			bit1   <= '1'; -- sum test
			bit0   <= '0';
			a <= '0';
			b <= '1';
			cin <= '0';
			wait for 10 ns;
			assert(cout = '0') 
			report "incorrect cout" severity warning;			
			assert(result = '1') 
			report "incorrect result" severity warning;						
			a <= '1';
			b <= '1';
			cin <= '1';			
			wait for 10 ns;
			assert(cout = '0') 
			report "incorrect cout" severity warning;
			assert(result = '1') 
			report "incorrect result" severity warning;			
			
			---------------------------
			bit1   <= '1';	-- '0' test
			bit0   <= '1';
			a <= '0';
			b <= '1';
			cin <= '0';
			wait for 10 ns;
			assert(cout = '0') 
			report "incorrect cout" severity warning;			
			
			a <= '1';
			b <= '1';
			cin <= '1';			
			wait for 10 ns;
			assert(cout = '0') 
			report "incorrect cout" severity warning;			

			wait;
	end process;
end TB;

configuration CFG_TB of ALU_1BIT_TB is
		for TB
		end for;
end CFG_TB;