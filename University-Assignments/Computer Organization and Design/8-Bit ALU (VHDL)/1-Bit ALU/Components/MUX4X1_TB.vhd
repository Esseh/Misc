--Test Bench Program for MUX4X1
--By Kenneth Willeford
--This program will test my MUX4X1 implementation.
--It will map a control signal for a given output.
--Testing every single combination is cumbersome. (64 test cases.)
--I'll test the following mapping pattern instead to keep things simple.
-- input1 => 0 input2 => 1 input3 => 1 input4 => 0
-- 00 => 0 , 01 => 1 , 10 => 1 , 11 => 0

library ieee;
use ieee.std_logic_1164.all;

entity MUX4X1_TB is
end MUX4X1_TB;

architecture TB of MUX4X1_TB is
	component MUX4X1 is
	port(	input1,input2,input3,input4,sig0,sig1: in std_logic;
			result: out std_logic
	);
	end component;

	signal input1,input2,input3,input4,bit0,bit1,result : std_logic;


	begin
		mapping: MUX4X1 port map(input1,input2,input3,input4,bit0,bit1,result);
		
	process
		begin
			input1 <= '0';		--Initialize Test Cases
			input2 <= '1';
			input3 <= '1';
			input4 <= '0';
			
			--case 00
			bit1   <= '0';
			bit0   <= '0';
			wait for 10 ns;
			assert(result = '0') 
			report "incorrect output" severity warning;
			--case 01
			bit1   <= '0';
			bit0   <= '1';
			wait for 10 ns;
			assert(result = '1') 
			report "incorrect output" severity warning;
			--case 10
			bit1   <= '1';
			bit0   <= '0';
			wait for 10 ns;
			assert(result = '1') 
			report "incorrect output" severity warning;
			--case 11
			bit1   <= '1';
			bit0   <= '1';
			wait for 10 ns;
			assert(result = '0') 
			report "incorrect output" severity warning;
			wait;
	end process;
end TB;

configuration CFG_TB of MUX4X1_TB is
		for TB
		end for;
end CFG_TB;