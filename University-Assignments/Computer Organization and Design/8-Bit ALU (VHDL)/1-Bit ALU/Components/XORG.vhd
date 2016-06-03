library ieee;
use ieee.std_logic_1164.all;

entity XORG is
port( 	x1,x2: in std_logic;
		y1:	out std_logic
);
end XORG;

architecture struct of XORG is
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
   
   component NEG is
   port( x1: in std_logic;
		 y1: out std_logic
		);
   end component;
   
   signal negated_a: std_logic;
   signal negated_b: std_logic;
   signal and_a_not_b: std_logic;
   signal and_not_a_b: std_logic;
   
begin
	map_NOT_gate1: NEG  port map (x1,negated_a); -- -a
	map_NOT_gate2: NEG  port map (x2,negated_b); -- -b
	map_AND_gate1: ANDG port map (x1,negated_b,and_a_not_b); -- (a*-b)
	map_AND_gate2: ANDG port map (negated_a,x2,and_not_a_b); -- (-a*b)
	map_OR_gate:   ORG  port map (and_a_not_b,and_not_a_b,y1); -- (-a*b)+(a*-b)
end struct;