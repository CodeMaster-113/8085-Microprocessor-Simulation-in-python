
registers = {
    'A': 0,
    'B': 0, 'C': 0,
    'D': 0, 'E': 0,
    'H': 0, 'L': 0,
    'PC': 0x0000,
    'SP': 0xFFFF
}

flags = {
    'S': 0,   # Sign
    'Z': 0,   # Zero
    'AC': 0,  # Auxiliary Carry
    'P': 0,   # Parity
    'CY': 0   # Carry
}

memory = bytearray(65536)  # 64 KB