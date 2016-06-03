--ALU_8BIT Implementation
-- By Kenneth Willeford
-- This is an implementation of an 8 bit ALU built structurally by combining 8 1-bit ALUs.
-- It can comput AND, OR, ADD, SUB. SUB is ADD with an activated BINV signal.
-- BINV thus acts as the initial carry in.
 
library ieee;
use ieee.std_logic_1164.all;


entity ALU_8BIT is
port(	binv,a7,a6,a5,a4,a3,a2,a1,a0,b7,b6,b5,b4,b3,b2,b1,b0,sig0,sig1: in std_logic;
		r7,r6,r5,r4,r3,r2,r1,r0,cout,overflow: out std_logic
);
end ALU_8BIT;

architecture struct of ALU_8BIT is
component ALU_1BIT is
port(	binv,a,b,cin,sig0,sig1: in std_logic;
		result,cout: out std_logic
);
end component;
component ALU_1BIT_OF is
port(	binv,a,b,cin,sig0,sig1: in std_logic;
		result,cout,overflow: out std_logic
);
end component;
	
   signal co0,co1,co2,co3,co4,co5,co6: std_logic;
   
begin
	FIRST_ALU: ALU_1BIT port map(binv,a0,b0,binv,sig0,sig1,r0,co0);
	SECOND_ALU: ALU_1BIT port map(binv,a1,b1,co0,sig0,sig1,r1,co1);
	THIRD_ALU: ALU_1BIT port map(binv,a2,b2,co1,sig0,sig1,r2,co2);
	FOURTH_ALU: ALU_1BIT port map(binv,a3,b3,co2,sig0,sig1,r3,co3);
	FIFTH_ALU: ALU_1BIT port map(binv,a4,b4,co3,sig0,sig1,r4,co4);
	SIXTH_ALU: ALU_1BIT port map(binv,a5,b5,co4,sig0,sig1,r5,co5);
	SEVENTH_ALU: ALU_1BIT port map(binv,a6,b6,co5,sig0,sig1,r6,co6);
	LAST_ALU: ALU_1BIT_OF port map(binv,a7,b7,co6,sig0,sig1,r7,cout,overflow);
end struct;