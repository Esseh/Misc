--Two Bit Decoder Implementation
--By Kenneth Willeford
--This module will take in 2 inputs and return 4 outputs. Only 1 of those outputs are true.
--This is based on a two bit signal. ie
-- 00 => out1 is true
-- 01 => out2 is true
-- 10 => out3 is true
-- 11 => out4 is true
library ieee;
use ieee.std_logic_1164.all;


entity DECODER2 is
port(	sig0,sig1: in std_logic;
		out1,out2,out3,out4: out std_logic
);
end DECODER2;

architecture struct of DECODER2 is
   component ANDG is
   port( x1,x2: in std_logic;
         y1: out std_logic
	);
   end component;
   
   component NEG is
   port( x1: in std_logic;
         y1: out std_logic
	);
   end component;
   
   signal negated_sig0: std_logic;		
   signal negated_sig1: std_logic;
   
begin
	map_NEG1: NEG port map (sig0,negated_sig0); --Negate Signal One and hold it.
	map_NEG2: NEG port map (sig1,negated_sig1); --Negate Signal Two and hold it.
	output00: ANDG port map (negated_sig1,negated_sig0,out1); 	-- 0 and 0 => out1 is true
	output01: ANDG port map (negated_sig1,sig0,out2);			-- 0 and 1 => out2 is true
	output10: ANDG port map (sig1,negated_sig0,out3);			-- 1 and 0 => out3 is true
	output11: ANDG port map (sig1,sig0,out4);					-- 1 and 1 => out4 is true
end struct;