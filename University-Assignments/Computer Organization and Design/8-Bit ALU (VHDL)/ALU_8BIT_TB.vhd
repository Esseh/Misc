--Test Bench Program for ALU_8BIT
--By Kenneth Willeford
--
	
library ieee;
use ieee.std_logic_1164.all;

entity ALU_8BIT_TB is
end ALU_8BIT_TB;

architecture TB of ALU_8BIT_TB is
	component ALU_8BIT is
	port(	binv,a7,a6,a5,a4,a3,a2,a1,a0,b7,b6,b5,b4,b3,b2,b1,b0,sig0,sig1: in std_logic;
			r7,r6,r5,r4,r3,r2,r1,r0,cout,overflow: out std_logic
	);
	end component;

	signal binv,a7,a6,a5,a4,a3,a2,a1,a0,b7,b6,b5,b4,b3,b2,b1,b0,sig0,sig1,r7,r6,r5,r4,r3,r2,r1,r0,cout,overflow : std_logic;


	begin
		mapping: ALU_8BIT port map(binv,a7,a6,a5,a4,a3,a2,a1,a0,b7,b6,b5,b4,b3,b2,b1,b0,sig0,sig1,r7,r6,r5,r4,r3,r2,r1,r0,cout,overflow);
		
	process
		begin
			a7 <= '1';a6 <= '1';a5 <= '1';a4 <= '1';a3 <= '1';a2 <= '1';a1 <= '1';a0 <= '1';
			b7 <= '1';b6 <= '1';b5 <= '1';b4 <= '1';b3 <= '1';b2 <= '1';b1 <= '1';b0 <= '1';
			
			binv <= '0';sig1 <= '0'; sig0 <= '0';
			wait for 10 ns;
			assert(r7 = '1' and r6 = '1' and r5 = '1' and r4 = '1' and r3 = '1' and r2 = '1' and r1 = '1' and r0 = '1') 
			report "incorrect AND result" severity warning;	

			binv <= '0';sig1 <= '0'; sig0 <= '1';
			wait for 10 ns;
			assert(r7 = '1' and r6 = '1' and r5 = '1' and r4 = '1' and r3 = '1' and r2 = '1' and r1 = '1' and r0 = '1') 
			report "incorrect OR result" severity warning;	
			
			binv <= '0';sig1 <= '1'; sig0 <= '0';
			wait for 10 ns;
			assert(r7 = '1' and r6 = '1' and r5 = '1' and r4 = '1' and r3 = '1' and r2 = '1' and r1 = '1' and r0 = '0') 
			report "incorrect ADD result" severity warning;	
			
			binv <= '1';sig1 <= '1'; sig0 <= '0';
			wait for 10 ns;
			assert(r7 = '0' and r6 = '0' and r5 = '0' and r4 = '0' and r3 = '0' and r2 = '0' and r1 = '0' and r0 = '0') 
			report "incorrect SUB result" severity warning;	
			
			
			a7 <= '0';a6 <= '1';a5 <= '1';a4 <= '1';a3 <= '1';a2 <= '1';a1 <= '1';a0 <= '1';
			b7 <= '1';b6 <= '0';b5 <= '0';b4 <= '0';b3 <= '0';b2 <= '0';b1 <= '0';b0 <= '0';
			
			binv <= '0';sig1 <= '0'; sig0 <= '0';
			wait for 10 ns;
			assert(r7 = '0' and r6 = '0' and r5 = '0' and r4 = '0' and r3 = '0' and r2 = '0' and r1 = '0' and r0 = '0') 
			report "incorrect AND result" severity warning;	

			binv <= '0';sig1 <= '0'; sig0 <= '1';
			wait for 10 ns;
			assert(r7 = '1' and r6 = '1' and r5 = '1' and r4 = '1' and r3 = '1' and r2 = '1' and r1 = '1' and r0 = '1') 
			report "incorrect OR result" severity warning;	
			
			binv <= '0';sig1 <= '1'; sig0 <= '0';
			wait for 10 ns;
			assert(r7 = '1' and r6 = '1' and r5 = '1' and r4 = '1' and r3 = '1' and r2 = '1' and r1 = '1' and r0 = '1') 
			report "incorrect ADD result" severity warning;	
			
			binv <= '1';sig1 <= '1'; sig0 <= '0';
			wait for 10 ns;
			assert(r7 = '1' and r6 = '1' and r5 = '1' and r4 = '1' and r3 = '1' and r2 = '1' and r1 = '1' and r0 = '1') 
			report "incorrect SUB result" severity warning;	
			
			
			a7 <= '1';a6 <= '0';a5 <= '0';a4 <= '0';a3 <= '0';a2 <= '0';a1 <= '0';a0 <= '0';
			b7 <= '0';b6 <= '1';b5 <= '1';b4 <= '1';b3 <= '1';b2 <= '1';b1 <= '1';b0 <= '1';
			
			binv <= '0';sig1 <= '0'; sig0 <= '0';
			wait for 10 ns;
			assert(r7 = '0' and r6 = '0' and r5 = '0' and r4 = '0' and r3 = '0' and r2 = '0' and r1 = '0' and r0 = '0') 
			report "incorrect AND result" severity warning;	

			binv <= '0';sig1 <= '0'; sig0 <= '1';
			wait for 10 ns;
			assert(r7 = '1' and r6 = '1' and r5 = '1' and r4 = '1' and r3 = '1' and r2 = '1' and r1 = '1' and r0 = '1') 
			report "incorrect OR result" severity warning;	
			
			binv <= '0';sig1 <= '1'; sig0 <= '0';
			wait for 10 ns;
			assert(r7 = '1' and r6 = '1' and r5 = '1' and r4 = '1' and r3 = '1' and r2 = '1' and r1 = '1' and r0 = '1') 
			report "incorrect ADD result" severity warning;	
			
			binv <= '1';sig1 <= '1'; sig0 <= '0';
			wait for 10 ns;
			assert(r7 = '0' and r6 = '0' and r5 = '0' and r4 = '0' and r3 = '0' and r2 = '0' and r1 = '0' and r0 = '1') 
			report "incorrect SUB result" severity warning;	
			
			
			a7 <= '0';a6 <= '1';a5 <= '0';a4 <= '1';a3 <= '0';a2 <= '1';a1 <= '0';a0 <= '1';
			b7 <= '1';b6 <= '0';b5 <= '1';b4 <= '0';b3 <= '1';b2 <= '0';b1 <= '1';b0 <= '0';
			
			binv <= '0';sig1 <= '0'; sig0 <= '0';
			wait for 10 ns;
			assert(r7 = '0' and r6 = '0' and r5 = '0' and r4 = '0' and r3 = '0' and r2 = '0' and r1 = '0' and r0 = '0') 
			report "incorrect AND result" severity warning;	

			binv <= '0';sig1 <= '0'; sig0 <= '1';
			wait for 10 ns;
			assert(r7 = '1' and r6 = '1' and r5 = '1' and r4 = '1' and r3 = '1' and r2 = '1' and r1 = '1' and r0 = '1') 
			report "incorrect OR result" severity warning;	
			
			binv <= '0';sig1 <= '1'; sig0 <= '0';
			wait for 10 ns;
			assert(r7 = '1' and r6 = '1' and r5 = '1' and r4 = '1' and r3 = '1' and r2 = '1' and r1 = '1' and r0 = '1') 
			report "incorrect ADD result" severity warning;	
			
			binv <= '1';sig1 <= '1'; sig0 <= '0';
			wait for 10 ns;
			assert(r7 = '1' and r6 = '0' and r5 = '1' and r4 = '0' and r3 = '1' and r2 = '0' and r1 = '1' and r0 = '1') 
			report "incorrect SUB result" severity warning;	
			

			
			a7 <= '1';a6 <= '1';a5 <= '0';a4 <= '1';a3 <= '1';a2 <= '0';a1 <= '1';a0 <= '1';
			b7 <= '1';b6 <= '0';b5 <= '1';b4 <= '0';b3 <= '1';b2 <= '0';b1 <= '1';b0 <= '0';
			
			binv <= '0';sig1 <= '0'; sig0 <= '0';
			wait for 10 ns;
			assert(r7 = '1' and r6 = '0' and r5 = '0' and r4 = '0' and r3 = '1' and r2 = '0' and r1 = '1' and r0 = '0') 
			report "incorrect AND result" severity warning;	

			binv <= '0';sig1 <= '0'; sig0 <= '1';
			wait for 10 ns;
			assert(r7 = '1' and r6 = '1' and r5 = '1' and r4 = '1' and r3 = '1' and r2 = '0' and r1 = '1' and r0 = '1') 
			report "incorrect OR result" severity warning;	
			
			binv <= '0';sig1 <= '1'; sig0 <= '0';
			wait for 10 ns;
			assert(r7 = '1' and r6 = '0' and r5 = '0' and r4 = '0' and r3 = '0' and r2 = '1' and r1 = '0' and r0 = '1') 
			report "incorrect ADD result" severity warning;	
			
			binv <= '1';sig1 <= '1'; sig0 <= '0';
			wait for 10 ns;
			assert(r7 = '0' and r6 = '0' and r5 = '1' and r4 = '1' and r3 = '0' and r2 = '0' and r1 = '0' and r0 = '1') 
			report "incorrect SUB result" severity warning;	
			
			wait;
	end process;
end TB;

configuration CFG_TB of ALU_8BIT_TB is
		for TB
		end for;
end CFG_TB;