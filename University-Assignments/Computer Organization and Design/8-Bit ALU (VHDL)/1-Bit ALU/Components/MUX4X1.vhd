--MUX4X1 Implementation
--By Kenneth Willeford
--This module will take in 4 inputs and return only one of the 4 as the output based on a 2 bit control signal.
--For example..
-- input1 => 0 input2 => 1 input3 => 1 input4 => 0
-- 00 => 0 , 01 => 1 , 10 => 1 , 11 => 0
-- The signals thus are mapped to the appropriate input.
library ieee;
use ieee.std_logic_1164.all;


entity MUX4X1 is
port(	input1,input2,input3,input4,sig0,sig1: in std_logic;
		result: out std_logic
);
end MUX4X1;

architecture struct of MUX4X1 is
   component ANDG is
   port( x1,x2: in std_logic;
         y1: out std_logic
	);
   end component;
   
   component ORG is
   port( x1,x2: in std_logic;
         y1: out std_logic
	);
   end component;
   component DECODER2 is
   port( sig0,sig1: in std_logic;
		out1,out2,out3,out4: out std_logic
	);
   end component;
	
   signal d00,d01,d10,d11: std_logic;	
   signal temp1,temp2,temp_1_2,temp3,temp4,temp_3_4: std_logic;
begin
	Parse_Signal: DECODER2 port map (sig0,sig1,d00,d01,d10,D11);	-- Use the decoder to get three 0 signals and one 1 signal. (Refer to Decoder Documentation for Details)
	MAP_ANDG1: ANDG port map (d00,input1,temp1);					--Match Signal to pass or don't to destroy.
	MAP_ANDG2: ANDG port map (d01,input2,temp2);					--Match Signal to pass or don't to destroy.
	MAP_ORG_1_2: ORG port map (temp1,temp2,temp_1_2);				--Collapse to one correct value, unless both are 0.
	MAP_ANDG3: ANDG  port map (d10,input3,temp3);					--Match Signal to pass or don't to destroy.
	MAP_ANDG4: ANDG port map (d11,input4,temp4);					--Match Signal to pass or don't to destroy.
	MAP_ORG_3_4: ORG port map (temp3,temp4,temp_3_4);				--Collapse to one correct value, unless both are 0.
	MAP_ORG_RESULT: ORG port map (temp_1_2,temp_3_4,result);   		--Collapse to one true result.
end struct;