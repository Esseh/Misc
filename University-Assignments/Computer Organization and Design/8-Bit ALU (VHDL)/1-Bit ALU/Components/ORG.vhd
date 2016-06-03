library ieee;
use ieee.std_logic_1164.all;

entity ORG is
port( x1,x2: in std_logic;
      y1: out std_logic
     );
end ORG;

architecture behav of ORG is
begin
   process(x1, x2)
   begin
      if ((x1='1') or (x2='1')) then
         y1 <= '1';
      else
         y1 <= '0';
      end if;
   end process;
end behav;
