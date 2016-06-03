--ALU_1BIT_OF Implementation
--OLD DOCUMENTATION
	--By Kenneth Willeford
	--This module will take in 2 inputs, a carry in, a control signal, 
	-- Given 00 it will send out the 'and' of the inputs.
	-- Given 01 it will send out the 'or' of the inputs.
	-- Given 10 it will give out the sum of the inputs. 
	-- Given 11 it will give out '0'.
	-- It will send out the carry out of the sum regardless of signal.
	-- All values will be calculated and then a result chosen.
--NEW DETAILS
--	This 1 BIT ALU will have an additional control signal 'binv'
--	Which communicates with a 2X1MUX in order to invert the b signal. This allows for subtraction.
--	The idea is, a - b  is the same as a + (-b) so we simply need to invert b.
-- 	While the one bit ALU does not know this information, the highest level ALU knows that binv is the initial carry in value. This completes 2's complement subtraction.
--MODIFICATION
--	This specific ALU is modified to perform overflow checking.
library ieee;
use ieee.std_logic_1164.all;


entity ALU_1BIT_OF is
port(	binv,a,b,cin,sig0,sig1: in std_logic;
		result,cout,overflow: out std_logic
);
end ALU_1BIT_OF;

architecture struct of ALU_1BIT_OF is
   component MUX4X1 is
	port(	input1,input2,input3,input4,sig0,sig1: in std_logic;
		result: out std_logic
	);
   end component;
   component MUX2X1 is
   port(	b,binv: in std_logic;
			output: out std_logic
   );
   end component;
   component ORG is
   port( x1,x2: in std_logic;
         y1: out std_logic
	);
   end component;
   component ANDG is
   port( x1,x2: in std_logic;
         y1: out std_logic
	);
   end component;
	component XORG is
	port( x1,x2: in std_logic;
		  y1: out std_logic
	);
	end component;
	component ADD is
	port(	a,b,cin: in std_logic;
			sum,cout: out std_logic
	);
	end component;
	component NEG is
	port( x1: in std_logic;
		  y1: out std_logic
	);
	end component;
   signal or_result,and_result,sum_result,true_b: std_logic;
   signal ofxor1,ofxor2,ofxor2_negated: std_logic;
begin
	BINVERT: MUX2X1 port map (b,binv,true_b); -- Invert B if binv is 1.
	SUM_RES: ADD  port map (a,true_b,cin,sum_result,cout);	--	Get Sum and send out Carry Out
	OR_RES:	 ORG  port map (a,true_b,or_result);				--	Get Or Result
	AND_RES: ANDG port map (a,true_b,and_result);			--	Get And Result
	Final_Result: MUX4X1 port map (and_result,or_result,sum_result,'0',sig0,sig1,result);	-- Send out result based on signal.
	-- OVERFLOW CHECKING    
	OVERFLOWXOR1: XORG port map(sum_result,a,ofxor1); --((SUM * -a)+(-SUM*a))
	OVERFLOWXOR2: XORG port map(a,true_b,ofxor2); -- (A_XOR_B)
	OVERFLOWXOR2FIX: NEG port map(ofxor2,ofxor2_negated); -- -(A_XOR_B)
	OVERFLOWRESULT: ANDG port map(ofxor1,ofxor2_negated,overflow); -- ((SUM * -a)+(-SUM*a)) * -(A_XOR_B)
end struct;