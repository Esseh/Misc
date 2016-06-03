--Test Bench Program for 2 bit decoder
--By Kenneth Willeford
--This program will test my 2 bit decoder implementation.
--It will check to make sure that I am getting desired outputs for given inputs.
--Here is the corresponding logic table.
--
--	sig0	sig1	out1	out2	out3	out4
--	0		0		1		0		0		0
--	0		1		0		1		0		0
--	1		0		0		0		1		0
--	1		1		0		0		0		1
library ieee;
use ieee.std_logic_1164.all;

entity DECODER2_TB is
end DECODER2_TB;

architecture TB of DECODER2_TB is
	component DECODER2 is
port(	sig0,sig1: in std_logic;
		out1,out2,out3,out4: out std_logic
);
	end component;

	signal bit0,bit1,output00,output01,output10,output11 : std_logic;


	begin
		mapping: DECODER2 port map(bit0,bit1,output00,output01,output10,output11);
		
	process
		begin
			--case 00
			bit1   <= '0';
			bit0   <= '0';
			wait for 10 ns;
			assert(output00 = '1') 
			report "incorrect output" severity warning;
			assert(output01 = '0') 
			report "incorrect output" severity warning;
			assert(output10 = '0') 
			report "incorrect output" severity warning;			
			assert(output11 = '0') 
			report "incorrect output" severity warning;
			--case 01
			bit1   <= '0';
			bit0   <= '1';
			wait for 10 ns;
			assert(output00 = '0') 
			report "incorrect output" severity warning;
			assert(output01 = '1') 
			report "incorrect output" severity warning;
			assert(output10 = '0') 
			report "incorrect output" severity warning;			
			assert(output11 = '0') 
			report "incorrect output" severity warning;			
			--case 10
			bit1   <= '1';
			bit0   <= '0';
			wait for 10 ns;
			assert(output00 = '0') 
			report "incorrect output" severity warning;
			assert(output01 = '0') 
			report "incorrect output" severity warning;
			assert(output10 = '1') 
			report "incorrect output" severity warning;			
			assert(output11 = '0') 
			report "incorrect output" severity warning;			
			--case 11
			bit0   <= '1';
			bit1   <= '1';
			wait for 10 ns;
			assert(output00 = '0') 
			report "incorrect output" severity warning;
			assert(output01 = '0') 
			report "incorrect output" severity warning;
			assert(output10 = '0') 
			report "incorrect output" severity warning;			
			assert(output11 = '1') 
			report "incorrect output" severity warning;			
			wait;
	end process;
end TB;

configuration CFG_TB of DECODER2_TB is
		for TB
		end for;
end CFG_TB;