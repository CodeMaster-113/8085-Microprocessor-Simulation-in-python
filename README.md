# 8085-Microprocessor-Simulation-in-python

A fully functional Intel 8085 microprocessor simulator written in Python. It supports all 246 standard 8085 mnemonics — from data transfer and arithmetic to branching, stack operations, and I/O — with a complete fetch-decode-execute engine and interactive memory inspection.

Features

Full instruction set — all 246 8085 opcodes supported
Interactive assembler — type mnemonics directly into the terminal; the simulator encodes and loads them into a 64KB memory model in real time
Accurate flag simulation — Sign (S), Zero (Z), Carry (CY), Auxiliary Carry (AC), and Parity (P) flags all computed correctly
Little-endian address encoding — 3-byte instructions stored correctly as low byte first, high byte second
Stack simulation — PUSH, POP, CALL, RET and all conditional variants work with a proper SP-based stack
Memory data entry — manually load data bytes at any address after assembling the program
Memory verification — dumps all non-zero memory locations after data entry
Output checker — inspect the value at any memory address after execution
Post-execution register dump — displays final state of all registers and flags





Requirements:    Python 3.6 or higher
                 No external libraries required


How to Run
bash      python 8085_simulator.py

Workflow
The simulator runs in four sequential phases:
1. Assembly Phase
You are prompted to enter 8085 mnemonics one by one. The simulator converts each to its machine code and stores it in memory starting at address 0000H.
0000: MVI A, 05
0001: MVI B, 03
0003: ADD B
0004: STA 2050
0007: HLT

Addresses auto-increment based on instruction size (1, 2, or 3 bytes).
The program ends when a termination opcode is entered (HLT, RST 0–RST 7).

2. Memory Dump
After assembly, a hex dump of the program area is printed:
Memory Dump (Program Range):
Addr 0000H: 3EH
Addr 0001H: 05H
...
3. Data Entry Phase
Load input data into any memory address (e.g. for LDA, LDAX, etc.):
Enter Address (Hex, -1 to quit): 2050
Enter hex data for 2050: FF
Enter Address (Hex, -1 to quit): -1
Data input success.
4. Execution Phase
The simulator runs the program from 0000H and prints a final register and flag dump:
Executing program from 0x0000...
Program terminated at 0X7H (opcode 0x76)

--- Final Register State ---
  A  : 0X8 (8)
  B  : 0X3 (3)
  ...

--- Flags ---
  S = 0
  Z = 0
  CY = 0
  AC = 0
  P = 1
5. Output Check (Optional Extension)
Inspect memory contents at any address after execution:
Enter Address (Hex, -1 to quit): 2050
Address 2050H: 08H
Enter Address (Hex, -1 to quit): -1
Output check success.
Signing off .....

Supported Instructions
CategoryInstructionsData TransferMOV, MVI, LXI, LDA, STA, LHLD, SHLD, LDAX, STAX, XCHGArithmeticADD, ADI, ADC, ACI, SUB, SUI, SBB, SBI, INR, DCR, INX, DCX, DAD, DAALogicalANA, ANI, ORA, ORI, XRA, XRI, CMA, CMC, STC, CMP, CPIRotateRLC, RRC, RAL, RARBranchJMP, JC, JNC, JZ, JNZ, JM, JP, JPE, JPOCallCALL, CC, CNC, CZ, CNZ, CM, CP, CPE, CPOReturnRET, RC, RNC, RZ, RNZ, RM, RP, RPE, RPOStackPUSH, POP, XTHL, SPHL, PCHLRestartRST 0 – RST 7I/O & ControlIN, OUT, NOP, DI, EI, RIM, SIM, HLT

Input Format

Mnemonics are case-insensitive (mvi a, 05 and MVI A, 05 both work)
Immediate/data values must be entered in hexadecimal without the H suffix (e.g. 05, FF, 3E)
Addresses must be in hexadecimal (e.g. 2050, C000)
Register names follow standard 8085 notation: A, B, C, D, E, H, L, M, SP, PSW

Example session
0000: LXI H, 2050
0003: MVI M, 0A
0005: INR M
0006: HLT
This loads 0AH into memory at 2050H, increments it to 0BH, then halts.

Known Limitations

I/O is simulated — IN always loads 00H into A; OUT prints to the terminal
Interrupts are not simulated — DI, EI, RIM, SIM are accepted but have no effect
No assembler labels — branch/call targets must be entered as raw hex addresses
Max 100,000 instruction cycles — execution halts automatically to prevent infinite loops


File Structure
8085_simulator.py   ← single-file simulator (assembler + executor)
README.md           ← this file

License
Free to use for educational purposes.
