library ieee;
use ieee.std_logic_1164.all;

entity ADD is
port(	a,b,cin: in std_logic;
		sum,cout: out std_logic
);
end ADD;

architecture struct of ADD is
	
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
   
   component XORG is
   port( x1,x2: in std_logic;
         y1: out std_logic
	);
   end component;
   
   --Declare Signals Here
   signal a_xor_b: std_logic;		-- a xor b in  	a xor b xor cin		and 	(a*b)+(cin*(a xor b))
   signal a_and_b: std_logic;		-- a and b in	(a*b)+(cin*(a xor b))
   signal a_xor_b_and_cin: std_logic; -- cin*(a xor b)	in	(a*b)+(cin*(a xor b))
   
begin
	map_XOR_gate1: XORG port map (a,b,a_xor_b); -- a xor b
	map_XOR_gate2: XORG port map (a_xor_b,cin,sum); -- a xor b xor c  => sum
	map_AND_gate1: ANDG port map (a_xor_b,cin,a_xor_b_and_cin); -- cin*(a xor b)
	map_AND_gate2: ANDG port map (a,b,a_and_b);	-- a and b
	map_OR_gate:    ORG port map (a_and_b,a_xor_b_and_cin,cout); -- (a*b)+(cin*(a xor b)) => cout
end struct;