--Test Bench Program for ALU_1BIT_OF
--By Kenneth Willeford
--OLD DOCUMENTATION--
	--This module will take in 2 inputs, a carry in, a control signal, 
	-- Given 00 it will send out the 'and' of the inputs.
	-- Given 01 it will send out the 'or' of the inputs.
	-- Given 10 it will give out the sum of the inputs. 
	-- Given 11 it will give out '0'.
	-- It will send out the carry out of the sum regardless of signal.
	-- All values will be calculated and then a result chosen.
	-- There are 96 possible test cases.
	-- So I will use 2 of each signal test instead.
--NEW STUFF
--	This specific testbench will be testing the overflow features
	
library ieee;
use ieee.std_logic_1164.all;

entity ALU_1BIT_OF_TB is
end ALU_1BIT_OF_TB;

architecture TB of ALU_1BIT_OF_TB is
	component ALU_1BIT_OF is
	port(	binv,a,b,cin,sig0,sig1: in std_logic;
			result,cout,overflow: out std_logic
	);
	end component;

	signal binv,a,b,cin,bit0,bit1,result,cout,overflow : std_logic;


	begin
		mapping: ALU_1BIT_OF port map(binv,a,b,cin,bit0,bit1,result,cout,overflow);
		
	process
		begin
			bit1   <= '1';
			bit0   <= '0';
			
			binv <= '0';			--Addition Case
			


			
			a <= '0';
			b <= '0';
			cin <= '0';
			wait for 10 ns;
			assert(overflow = '0') 
			report "OVERFLOW FLAG INCORRECT" severity warning;

			
			a <= '0';
			b <= '0';
			cin <= '1';
			wait for 10 ns;
			assert(overflow = '1')
			report "OVERFLOW FLAG INCORRECT" severity warning;
			
			
			a <= '0';
			b <= '1';
			cin <= '0';
			wait for 10 ns;
			assert(overflow = '0') 
			report "OVERFLOW FLAG INCORRECT" severity warning;		
			
			
			a <= '0';
			b <= '1';
			cin <= '1';
			wait for 10 ns;
			assert(overflow = '0') 
			report "OVERFLOW FLAG INCORRECT" severity warning;
	
	
			a <= '1';
			b <= '0';
			cin <= '0';
			wait for 10 ns;
			assert(overflow = '0') 
			report "OVERFLOW FLAG INCORRECT" severity warning;


			
			a <= '1';
			b <= '0';
			cin <= '1';
			wait for 10 ns;
			assert(overflow = '0') 
			report "OVERFLOW FLAG INCORRECT" severity warning;
			
			a <= '1';
			b <= '1';
			cin <= '1';
			wait for 10 ns;
			assert(overflow = '0') 
			report "OVERFLOW FLAG INCORRECT" severity warning;
			
			binv <= '1';			--Subtraction Case

			a <= '0';
			b <= '0';
			cin <= '0';
			wait for 10 ns;
			assert(overflow = '0') 
			report "OVERFLOW FLAG INCORRECT" severity warning;
			
			a <= '0';
			b <= '0';
			cin <= '1';
			wait for 10 ns;
			assert(overflow = '0') 
			report "OVERFLOW FLAG INCORRECT" severity warning;

			
			a <= '0';
			b <= '1';
			cin <= '0';
			wait for 10 ns;
			assert(overflow = '0') 
			report "OVERFLOW FLAG INCORRECT" severity warning;

			
			a <= '0';
			b <= '1';
			cin <= '1';
			wait for 10 ns;
			assert(overflow = '1') 
			report "OVERFLOW FLAG INCORRECT" severity warning;

			a <= '1';
			b <= '0';
			cin <= '0';
			wait for 10 ns;
			assert(overflow = '1') 
			report "OVERFLOW FLAG INCORRECT" severity warning;
			
			a <= '1';
			b <= '0';
			cin <= '1';
			wait for 10 ns;
			assert(overflow = '0') 
			report "OVERFLOW FLAG INCORRECT" severity warning;
			
			
			a <= '1';
			b <= '1';
			cin <= '1';
			wait for 10 ns;
			assert(overflow = '0') 
			report "OVERFLOW FLAG INCORRECT" severity warning;
			wait;
	end process;
end TB;

configuration CFG_TB of ALU_1BIT_OF_TB is
		for TB
		end for;
end CFG_TB;