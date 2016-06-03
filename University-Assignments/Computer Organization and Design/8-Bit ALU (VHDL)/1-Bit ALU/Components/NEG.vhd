library ieee;
use ieee.std_logic_1164.all;

entity NEG is
port( x1: in std_logic;
      y1: out std_logic
     );
end NEG;

architecture behav of NEG is
begin
   process(x1)
   begin
      if (x1='1') then
         y1 <= '0';
      else
         y1 <= '1';
      end if;
   end process;
end behav;
