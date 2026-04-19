from memory import memory
from  opcodes import get_opcode
from execution import execute_program



termination_opcodes = ["76", "C7", "CF", "D7", "DF", "E7", "EF", "F7", "FF"]

pc = 0x0000

print("Enter instructions line by line in uppercase: ")
while True:
    s = input(f"{hex(pc).upper()[2:].zfill(4)}: ").strip()
    arr = get_opcode(s)

    res_opcode = arr[0]
    res_len    = arr[1]

    if res_opcode == "None":
        print(f"  ! Unknown mnemonic: '{s}' — skipped.")
        continue

    memory[pc] = int(res_opcode, 16)
    pc += 1

    parts = s.replace(',', ' ').split()

    if res_len == 2:
        data_hex = parts[-1]
        memory[pc] = int(data_hex, 16)
        pc += 1

    elif res_len == 3:
        address_hex = parts[-1].zfill(4)
        low_byte  = address_hex[2:]
        high_byte = address_hex[:2]
        memory[pc] = int(low_byte, 16)
        pc += 1
        memory[pc] = int(high_byte, 16)
        pc += 1

    if res_opcode in termination_opcodes:
        print(f"Program terminated at {hex(pc-1).upper()}.")
        break

print("\nMemory Dump (Program Range):")
for i in range(pc):
    print(f"Addr {hex(i).upper()[2:].zfill(4)}H: {hex(memory[i]).upper()[2:].zfill(2)}H")

print("\nEnter input data address (-1 to exit the data entry): ")

while True:
    addr_str = input("Enter Address (Hex, -1 to quit): ").strip()
    if addr_str == "-1":
        print("Data input success.")
        break
    try:
        address = int(addr_str, 16)
        hex_data = input(f"Enter hex data for {addr_str.upper()}: ").strip()
        memory[address] = int(hex_data, 16)
    except ValueError:
        print("Invalid Hex input! Use characters 0-9 and A-F.")
    except IndexError:
        print("Address out of range! (Max is FFFF)")

print("\n--- Memory Verification ---")
for i in range(len(memory)):
    if memory[i] != 0:
        print(f"Address {hex(i).upper()[2:].zfill(4)}: {hex(memory[i]).upper()[2:].zfill(2)}")

execute_program(start_addr=0x0000)

print("\nEnter memory locations to check output (-1 to exit): ")

while True:
    addr_str = input("Enter Address (Hex, -1 to quit): ").strip()
    if addr_str == "-1":
        print("Output check success.")
        print("Signing off .....")
        break
    try:
        address = int(addr_str, 16)
        if address > 0xFFFF:
            print("Address out of range! (Max is FFFF)")
            continue
        print(f"Address {hex(address).upper()[2:].zfill(4)}H: {hex(memory[address]).upper()[2:].zfill(2)}H")
    except ValueError:
        print("Invalid Hex input! Use characters 0-9 and A-F.")
