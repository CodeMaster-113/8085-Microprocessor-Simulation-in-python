def get_opcode(mnemonic):
    m = mnemonic.upper().strip()
    # Extract just the mnemonic token (first word) for startswith checks
    tok = m.split()[0] if m.split() else ""

    # Returns (opcode, bytes)

    # ── A ────────────────────────────────────────────────────────────
    if   tok == "ACI":   return ("CE", 2)
    elif tok == "ADC":
        if   "ADC A"  in m: return ("8F", 1)
        elif "ADC B"  in m: return ("88", 1)
        elif "ADC C"  in m: return ("89", 1)
        elif "ADC D"  in m: return ("8A", 1)
        elif "ADC E"  in m: return ("8B", 1)
        elif "ADC H"  in m: return ("8C", 1)
        elif "ADC L"  in m: return ("8D", 1)
        elif "ADC M"  in m: return ("8E", 1)
    elif tok == "ADD":
        if   "ADD A"  in m: return ("87", 1)
        elif "ADD B"  in m: return ("80", 1)
        elif "ADD C"  in m: return ("81", 1)
        elif "ADD D"  in m: return ("82", 1)
        elif "ADD E"  in m: return ("83", 1)
        elif "ADD H"  in m: return ("84", 1)
        elif "ADD L"  in m: return ("85", 1)
        elif "ADD M"  in m: return ("86", 1)
    elif tok == "ADI":   return ("C6", 2)
    elif tok == "ANA":
        if   "ANA A"  in m: return ("A7", 1)
        elif "ANA B"  in m: return ("A0", 1)
        elif "ANA C"  in m: return ("A1", 1)
        elif "ANA D"  in m: return ("A2", 1)
        elif "ANA E"  in m: return ("A3", 1)
        elif "ANA H"  in m: return ("A4", 1)
        elif "ANA L"  in m: return ("A5", 1)
        elif "ANA M"  in m: return ("A6", 1)
    elif tok == "ANI":   return ("E6", 2)

    # ── C ────────────────────────────────────────────────────────────
    elif tok == "CALL":  return ("CD", 3)
    elif tok == "CC":    return ("DC", 3)
    elif tok == "CM":    return ("FC", 3)
    elif tok == "CMA":   return ("2F", 1)
    elif tok == "CMC":   return ("3F", 1)
    elif tok == "CMP":
        if   "CMP A"  in m: return ("BF", 1)
        elif "CMP B"  in m: return ("B8", 1)
        elif "CMP C"  in m: return ("B9", 1)
        elif "CMP D"  in m: return ("BA", 1)
        elif "CMP E"  in m: return ("BB", 1)
        elif "CMP H"  in m: return ("BC", 1)
        elif "CMP L"  in m: return ("BD", 1)
        elif "CMP M"  in m: return ("BE", 1)
    elif tok == "CNC":   return ("D4", 3)
    elif tok == "CNZ":   return ("C4", 3)
    elif tok == "CP":    return ("F4", 3)
    elif tok == "CPE":   return ("EC", 3)
    elif tok == "CPI":   return ("FE", 2)
    elif tok == "CPO":   return ("E4", 3)
    elif tok == "CZ":    return ("CC", 3)

    # ── D ────────────────────────────────────────────────────────────
    elif tok == "DAA":   return ("27", 1)
    elif tok == "DAD":
        if   "DAD B"  in m: return ("09", 1)
        elif "DAD D"  in m: return ("19", 1)
        elif "DAD H"  in m: return ("29", 1)
        elif "DAD SP" in m: return ("39", 1)
    elif tok == "DCR":
        if   "DCR A"  in m: return ("3D", 1)
        elif "DCR B"  in m: return ("05", 1)
        elif "DCR C"  in m: return ("0D", 1)
        elif "DCR D"  in m: return ("15", 1)
        elif "DCR E"  in m: return ("1D", 1)
        elif "DCR H"  in m: return ("25", 1)
        elif "DCR L"  in m: return ("2D", 1)
        elif "DCR M"  in m: return ("35", 1)
    elif tok == "DCX":
        if   "DCX B"  in m: return ("0B", 1)
        elif "DCX D"  in m: return ("1B", 1)
        elif "DCX H"  in m: return ("2B", 1)
        elif "DCX SP" in m: return ("3B", 1)
    elif tok == "DI":    return ("F3", 1)

    # ── E ────────────────────────────────────────────────────────────
    elif tok == "EI":    return ("FB", 1)

    # ── H ────────────────────────────────────────────────────────────
    elif tok == "HLT":   return ("76", 1)

    # ── I ────────────────────────────────────────────────────────────
    elif tok == "IN":    return ("DB", 2)
    elif tok == "INR":
        if   "INR A"  in m: return ("3C", 1)
        elif "INR B"  in m: return ("04", 1)
        elif "INR C"  in m: return ("0C", 1)
        elif "INR D"  in m: return ("14", 1)
        elif "INR E"  in m: return ("1C", 1)
        elif "INR H"  in m: return ("24", 1)
        elif "INR L"  in m: return ("2C", 1)
        elif "INR M"  in m: return ("34", 1)
    elif tok == "INX":
        if   "INX B"  in m: return ("03", 1)
        elif "INX D"  in m: return ("13", 1)
        elif "INX H"  in m: return ("23", 1)
        elif "INX SP" in m: return ("33", 1)

    # ── J ────────────────────────────────────────────────────────────
    elif tok == "JC":    return ("DA", 3)
    elif tok == "JM":    return ("FA", 3)
    elif tok == "JMP":   return ("C3", 3)
    elif tok == "JNC":   return ("D2", 3)
    elif tok == "JNZ":   return ("C2", 3)
    elif tok == "JP":    return ("F2", 3)
    elif tok == "JPE":   return ("EA", 3)
    elif tok == "JPO":   return ("E2", 3)
    elif tok == "JZ":    return ("CA", 3)

    # ── L ────────────────────────────────────────────────────────────
    elif tok == "LDA":   return ("3A", 3)
    elif tok == "LDAX":
        if   "LDAX B" in m: return ("0A", 1)
        elif "LDAX D" in m: return ("1A", 1)
    elif tok == "LHLD":  return ("2A", 3)
    elif tok == "LXI":
        if   "LXI B"  in m: return ("01", 3)
        elif "LXI D"  in m: return ("11", 3)
        elif "LXI H"  in m: return ("21", 3)
        elif "LXI SP" in m: return ("31", 3)

    # ── M ────────────────────────────────────────────────────────────
    elif tok == "MOV":
        if   "MOV A, A" in m: return ("7F", 1)
        elif "MOV A, B" in m: return ("78", 1)
        elif "MOV A, C" in m: return ("79", 1)
        elif "MOV A, D" in m: return ("7A", 1)
        elif "MOV A, E" in m: return ("7B", 1)
        elif "MOV A, H" in m: return ("7C", 1)
        elif "MOV A, L" in m: return ("7D", 1)
        elif "MOV A, M" in m: return ("7E", 1)
        elif "MOV B, A" in m: return ("47", 1)
        elif "MOV B, B" in m: return ("40", 1)
        elif "MOV B, C" in m: return ("41", 1)
        elif "MOV B, D" in m: return ("42", 1)
        elif "MOV B, E" in m: return ("43", 1)
        elif "MOV B, H" in m: return ("44", 1)
        elif "MOV B, L" in m: return ("45", 1)
        elif "MOV B, M" in m: return ("46", 1)
        elif "MOV C, A" in m: return ("4F", 1)
        elif "MOV C, B" in m: return ("48", 1)
        elif "MOV C, C" in m: return ("49", 1)
        elif "MOV C, D" in m: return ("4A", 1)
        elif "MOV C, E" in m: return ("4B", 1)
        elif "MOV C, H" in m: return ("4C", 1)
        elif "MOV C, L" in m: return ("4D", 1)
        elif "MOV C, M" in m: return ("4E", 1)
        elif "MOV D, A" in m: return ("57", 1)
        elif "MOV D, B" in m: return ("50", 1)
        elif "MOV D, C" in m: return ("51", 1)
        elif "MOV D, D" in m: return ("52", 1)
        elif "MOV D, E" in m: return ("53", 1)
        elif "MOV D, H" in m: return ("54", 1)
        elif "MOV D, L" in m: return ("55", 1)
        elif "MOV D, M" in m: return ("56", 1)
        elif "MOV E, A" in m: return ("5F", 1)
        elif "MOV E, B" in m: return ("58", 1)
        elif "MOV E, C" in m: return ("59", 1)
        elif "MOV E, D" in m: return ("5A", 1)
        elif "MOV E, E" in m: return ("5B", 1)
        elif "MOV E, H" in m: return ("5C", 1)
        elif "MOV E, L" in m: return ("5D", 1)
        elif "MOV E, M" in m: return ("5E", 1)
        elif "MOV H, A" in m: return ("67", 1)
        elif "MOV H, B" in m: return ("60", 1)
        elif "MOV H, C" in m: return ("61", 1)
        elif "MOV H, D" in m: return ("62", 1)
        elif "MOV H, E" in m: return ("63", 1)
        elif "MOV H, H" in m: return ("64", 1)
        elif "MOV H, L" in m: return ("65", 1)
        elif "MOV H, M" in m: return ("66", 1)
        elif "MOV L, A" in m: return ("6F", 1)
        elif "MOV L, B" in m: return ("68", 1)
        elif "MOV L, C" in m: return ("69", 1)
        elif "MOV L, D" in m: return ("6A", 1)
        elif "MOV L, E" in m: return ("6B", 1)
        elif "MOV L, H" in m: return ("6C", 1)
        elif "MOV L, L" in m: return ("6D", 1)
        elif "MOV L, M" in m: return ("6E", 1)
        elif "MOV M, A" in m: return ("77", 1)
        elif "MOV M, B" in m: return ("70", 1)
        elif "MOV M, C" in m: return ("71", 1)
        elif "MOV M, D" in m: return ("72", 1)
        elif "MOV M, E" in m: return ("73", 1)
        elif "MOV M, H" in m: return ("74", 1)
        elif "MOV M, L" in m: return ("75", 1)
    elif tok == "MVI":
        if   "MVI A" in m: return ("3E", 2)
        elif "MVI B" in m: return ("06", 2)
        elif "MVI C" in m: return ("0E", 2)
        elif "MVI D" in m: return ("16", 2)
        elif "MVI E" in m: return ("1E", 2)
        elif "MVI H" in m: return ("26", 2)
        elif "MVI L" in m: return ("2E", 2)
        elif "MVI M" in m: return ("36", 2)

    # ── N ────────────────────────────────────────────────────────────
    elif tok == "NOP":   return ("00", 1)

    # ── O ────────────────────────────────────────────────────────────
    elif tok == "ORA":
        if   "ORA A"  in m: return ("B7", 1)
        elif "ORA B"  in m: return ("B0", 1)
        elif "ORA C"  in m: return ("B1", 1)
        elif "ORA D"  in m: return ("B2", 1)
        elif "ORA E"  in m: return ("B3", 1)
        elif "ORA H"  in m: return ("B4", 1)
        elif "ORA L"  in m: return ("B5", 1)
        elif "ORA M"  in m: return ("B6", 1)
    elif tok == "ORI":   return ("F6", 2)
    elif tok == "OUT":   return ("D3", 2)

    # ── P ────────────────────────────────────────────────────────────
    elif tok == "PCHL":  return ("E9", 1)
    elif tok == "POP":
        if   "POP B"   in m: return ("C1", 1)
        elif "POP D"   in m: return ("D1", 1)
        elif "POP H"   in m: return ("E1", 1)
        elif "POP PSW" in m: return ("F1", 1)
    elif tok == "PUSH":
        if   "PUSH B"   in m: return ("C5", 1)
        elif "PUSH D"   in m: return ("D5", 1)
        elif "PUSH H"   in m: return ("E5", 1)
        elif "PUSH PSW" in m: return ("F5", 1)

    # ── R ────────────────────────────────────────────────────────────
    elif tok == "RAL":   return ("17", 1)
    elif tok == "RAR":   return ("1F", 1)
    elif tok == "RC":    return ("D8", 1)
    elif tok == "RET":   return ("C9", 1)
    elif tok == "RIM":   return ("20", 1)
    elif tok == "RLC":   return ("07", 1)
    elif tok == "RM":    return ("F8", 1)
    elif tok == "RNC":   return ("D0", 1)
    elif tok == "RNZ":   return ("C0", 1)
    elif tok == "RP":    return ("F0", 1)
    elif tok == "RPE":   return ("E8", 1)
    elif tok == "RPO":   return ("E0", 1)
    elif tok == "RRC":   return ("0F", 1)
    elif tok == "RST":
        if   "RST 0"  in m: return ("C7", 1)
        elif "RST 1"  in m: return ("CF", 1)
        elif "RST 2"  in m: return ("D7", 1)
        elif "RST 3"  in m: return ("DF", 1)
        elif "RST 4"  in m: return ("E7", 1)
        elif "RST 5"  in m: return ("EF", 1)
        elif "RST 6"  in m: return ("F7", 1)
        elif "RST 7"  in m: return ("FF", 1)
    elif tok == "RZ":    return ("C8", 1)

    # ── S ────────────────────────────────────────────────────────────
    elif tok == "SBB":
        if   "SBB A"  in m: return ("9F", 1)
        elif "SBB B"  in m: return ("98", 1)
        elif "SBB C"  in m: return ("99", 1)
        elif "SBB D"  in m: return ("9A", 1)
        elif "SBB E"  in m: return ("9B", 1)
        elif "SBB H"  in m: return ("9C", 1)
        elif "SBB L"  in m: return ("9D", 1)
        elif "SBB M"  in m: return ("9E", 1)
    elif tok == "SBI":   return ("DE", 2)
    elif tok == "SHLD":  return ("22", 3)
    elif tok == "SIM":   return ("30", 1)
    elif tok == "SPHL":  return ("F9", 1)
    elif tok == "STA":   return ("32", 3)
    elif tok == "STAX":
        if   "STAX B" in m: return ("02", 1)
        elif "STAX D" in m: return ("12", 1)
    elif tok == "STC":   return ("37", 1)
    elif tok == "SUB":
        if   "SUB A"  in m: return ("97", 1)
        elif "SUB B"  in m: return ("90", 1)
        elif "SUB C"  in m: return ("91", 1)
        elif "SUB D"  in m: return ("92", 1)
        elif "SUB E"  in m: return ("93", 1)
        elif "SUB H"  in m: return ("94", 1)
        elif "SUB L"  in m: return ("95", 1)
        elif "SUB M"  in m: return ("96", 1)
    elif tok == "SUI":   return ("D6", 2)

    # ── X ────────────────────────────────────────────────────────────
    elif tok == "XCHG":  return ("EB", 1)
    elif tok == "XRA":
        if   "XRA A"  in m: return ("AF", 1)
        elif "XRA B"  in m: return ("A8", 1)
        elif "XRA C"  in m: return ("A9", 1)
        elif "XRA D"  in m: return ("AA", 1)
        elif "XRA E"  in m: return ("AB", 1)
        elif "XRA H"  in m: return ("AC", 1)
        elif "XRA L"  in m: return ("AD", 1)
        elif "XRA M"  in m: return ("AE", 1)
    elif tok == "XRI":   return ("EE", 2)
    elif tok == "XTHL":  return ("E3", 1)

    return ("None", 0)


# ─────────────────────────────────────────────
#  Global State
# ─────────────────────────────────────────────

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

# ─────────────────────────────────────────────
#  Flag Helpers
# ─────────────────────────────────────────────

def calc_parity(value):
    """Returns 1 if number of set bits in value is even, else 0."""
    value &= 0xFF
    count = bin(value).count('1')
    return 1 if count % 2 == 0 else 0

def update_flags(result, skip_carry=False, skip_ac=False, prev_a=0, operand=0):
    """Update S, Z, P, CY (and optionally AC) flags after an operation."""
    byte_result = result & 0xFF
    flags['Z']  = 1 if byte_result == 0 else 0
    flags['S']  = 1 if (byte_result & 0x80) else 0
    flags['P']  = calc_parity(byte_result)
    if not skip_carry:
        flags['CY'] = 1 if (result > 0xFF or result < 0) else 0
    if not skip_ac:
        flags['AC'] = 1 if ((prev_a & 0x0F) + (operand & 0x0F)) > 0x0F else 0

def pack_flags():
    """Pack individual flags into a single byte. Format: S Z 0 AC 0 P 1 CY"""
    flag_byte = 0
    if flags['S']:  flag_byte |= 0x80
    if flags['Z']:  flag_byte |= 0x40
    if flags['AC']: flag_byte |= 0x10
    if flags['P']:  flag_byte |= 0x04
    flag_byte |= 0x02
    if flags['CY']: flag_byte |= 0x01
    return flag_byte

def unpack_flags(flag_byte):
    """Unpack a byte into individual flags (used by POP PSW)."""
    flags['S']  = 1 if (flag_byte & 0x80) else 0
    flags['Z']  = 1 if (flag_byte & 0x40) else 0
    flags['AC'] = 1 if (flag_byte & 0x10) else 0
    flags['P']  = 1 if (flag_byte & 0x04) else 0
    flags['CY'] = 1 if (flag_byte & 0x01) else 0

# ─────────────────────────────────────────────
#  Helper: Get M register address (HL pair)
# ─────────────────────────────────────────────

def get_hl_addr():
    return (registers['H'] << 8) | registers['L']

# ─────────────────────────────────────────────
#  Data Transfer Instructions
# ─────────────────────────────────────────────

def exec_mov(dest, src):
    val = memory[get_hl_addr()] if src == 'M' else registers[src]
    if dest == 'M':
        memory[get_hl_addr()] = val
    else:
        registers[dest] = val

def exec_mvi(reg, data):
    if reg == 'M':
        memory[get_hl_addr()] = data & 0xFF
    else:
        registers[reg] = data & 0xFF

def exec_lxi(reg_pair, high_byte, low_byte):
    if reg_pair == 'B':
        registers['B'], registers['C'] = high_byte, low_byte
    elif reg_pair == 'D':
        registers['D'], registers['E'] = high_byte, low_byte
    elif reg_pair == 'H':
        registers['H'], registers['L'] = high_byte, low_byte
    elif reg_pair == 'SP':
        registers['SP'] = (high_byte << 8) | low_byte

def exec_lda(address):
    registers['A'] = memory[address]

def exec_sta(address):
    memory[address] = registers['A']

def exec_lhld(address):
    registers['L'] = memory[address]
    registers['H'] = memory[address + 1]

def exec_shld(address):
    memory[address] = registers['L']
    memory[address + 1] = registers['H']

def exec_ldax(reg_pair):
    if reg_pair == 'B':
        addr = (registers['B'] << 8) | registers['C']
    else:
        addr = (registers['D'] << 8) | registers['E']
    registers['A'] = memory[addr]

def exec_stax(reg_pair):
    if reg_pair == 'B':
        addr = (registers['B'] << 8) | registers['C']
    else:
        addr = (registers['D'] << 8) | registers['E']
    memory[addr] = registers['A']

def exec_xchg():
    registers['D'], registers['H'] = registers['H'], registers['D']
    registers['E'], registers['L'] = registers['L'], registers['E']

# ─────────────────────────────────────────────
#  Arithmetic Instructions
# ─────────────────────────────────────────────

def exec_add(reg):
    operand = memory[get_hl_addr()] if reg == 'M' else registers[reg]
    prev_a = registers['A']
    res = prev_a + operand
    registers['A'] = res & 0xFF
    update_flags(res, prev_a=prev_a, operand=operand)

def exec_adi(data):
    prev_a = registers['A']
    res = prev_a + data
    registers['A'] = res & 0xFF
    update_flags(res, prev_a=prev_a, operand=data)

def exec_adc(reg):
    operand = memory[get_hl_addr()] if reg == 'M' else registers[reg]
    prev_a = registers['A']
    res = prev_a + operand + flags['CY']
    registers['A'] = res & 0xFF
    update_flags(res, prev_a=prev_a, operand=operand + flags['CY'])

def exec_aci(data):
    prev_a = registers['A']
    res = prev_a + data + flags['CY']
    registers['A'] = res & 0xFF
    update_flags(res, prev_a=prev_a, operand=data + flags['CY'])

def exec_sub(reg):
    operand = memory[get_hl_addr()] if reg == 'M' else registers[reg]
    prev_a = registers['A']
    res = prev_a - operand
    registers['A'] = res & 0xFF
    update_flags(res, prev_a=prev_a, operand=(~operand + 1) & 0xFF)

def exec_sui(data):
    prev_a = registers['A']
    res = prev_a - data
    registers['A'] = res & 0xFF
    update_flags(res, prev_a=prev_a, operand=(~data + 1) & 0xFF)

def exec_sbb(reg):
    operand = memory[get_hl_addr()] if reg == 'M' else registers[reg]
    prev_a = registers['A']
    res = prev_a - operand - flags['CY']
    registers['A'] = res & 0xFF
    update_flags(res)

def exec_sbi(data):
    prev_a = registers['A']
    res = prev_a - data - flags['CY']
    registers['A'] = res & 0xFF
    update_flags(res)

def exec_inr(reg):
    if reg == 'M':
        addr = get_hl_addr()
        prev = memory[addr]
        res = prev + 1
        memory[addr] = res & 0xFF
        update_flags(res, skip_carry=True, prev_a=prev, operand=1)
    else:
        prev = registers[reg]
        res = prev + 1
        registers[reg] = res & 0xFF
        update_flags(res, skip_carry=True, prev_a=prev, operand=1)

def exec_dcr(reg):
    if reg == 'M':
        addr = get_hl_addr()
        prev = memory[addr]
        res = prev - 1
        memory[addr] = res & 0xFF
        update_flags(res, skip_carry=True)
    else:
        prev = registers[reg]
        res = prev - 1
        registers[reg] = res & 0xFF
        update_flags(res, skip_carry=True)

def exec_inx(reg_pair):
    if reg_pair == 'B':
        val = ((registers['B'] << 8) | registers['C']) + 1
        registers['B'], registers['C'] = (val >> 8) & 0xFF, val & 0xFF
    elif reg_pair == 'D':
        val = ((registers['D'] << 8) | registers['E']) + 1
        registers['D'], registers['E'] = (val >> 8) & 0xFF, val & 0xFF
    elif reg_pair == 'H':
        val = ((registers['H'] << 8) | registers['L']) + 1
        registers['H'], registers['L'] = (val >> 8) & 0xFF, val & 0xFF
    elif reg_pair == 'SP':
        registers['SP'] = (registers['SP'] + 1) & 0xFFFF

def exec_dcx(reg_pair):
    if reg_pair == 'B':
        val = ((registers['B'] << 8) | registers['C']) - 1
        registers['B'], registers['C'] = (val >> 8) & 0xFF, val & 0xFF
    elif reg_pair == 'D':
        val = ((registers['D'] << 8) | registers['E']) - 1
        registers['D'], registers['E'] = (val >> 8) & 0xFF, val & 0xFF
    elif reg_pair == 'H':
        val = ((registers['H'] << 8) | registers['L']) - 1
        registers['H'], registers['L'] = (val >> 8) & 0xFF, val & 0xFF
    elif reg_pair == 'SP':
        registers['SP'] = (registers['SP'] - 1) & 0xFFFF

def exec_dad(reg_pair):
    hl = (registers['H'] << 8) | registers['L']
    if reg_pair == 'B':
        rp = (registers['B'] << 8) | registers['C']
    elif reg_pair == 'D':
        rp = (registers['D'] << 8) | registers['E']
    elif reg_pair == 'H':
        rp = (registers['H'] << 8) | registers['L']
    elif reg_pair == 'SP':
        rp = registers['SP']
    res = hl + rp
    flags['CY'] = 1 if res > 0xFFFF else 0
    res &= 0xFFFF
    registers['H'], registers['L'] = (res >> 8) & 0xFF, res & 0xFF

def exec_daa():
    a = registers['A']
    correction = 0
    if (a & 0x0F) > 9 or flags['AC']:
        correction |= 0x06
    if (a > 0x99) or flags['CY']:
        correction |= 0x60
        flags['CY'] = 1
    res = a + correction
    flags['AC'] = 1 if ((a & 0x0F) + (correction & 0x0F)) > 0x0F else 0
    registers['A'] = res & 0xFF
    flags['Z'] = 1 if registers['A'] == 0 else 0
    flags['S'] = 1 if (registers['A'] & 0x80) else 0
    flags['P'] = calc_parity(registers['A'])

# ─────────────────────────────────────────────
#  Logical Instructions
# ─────────────────────────────────────────────

def exec_ana(reg):
    operand = memory[get_hl_addr()] if reg == 'M' else registers[reg]
    flags['AC'] = 1 if ((registers['A'] | operand) & 0x08) else 0
    registers['A'] &= operand
    flags['CY'] = 0
    flags['Z']  = 1 if registers['A'] == 0 else 0
    flags['S']  = 1 if (registers['A'] & 0x80) else 0
    flags['P']  = calc_parity(registers['A'])

def exec_ani(data):
    flags['AC'] = 1 if ((registers['A'] | data) & 0x08) else 0
    registers['A'] &= data
    flags['CY'] = 0
    flags['Z']  = 1 if registers['A'] == 0 else 0
    flags['S']  = 1 if (registers['A'] & 0x80) else 0
    flags['P']  = calc_parity(registers['A'])

def exec_ora(reg):
    operand = memory[get_hl_addr()] if reg == 'M' else registers[reg]
    registers['A'] |= operand
    flags['CY'] = 0
    flags['AC'] = 0
    flags['Z']  = 1 if registers['A'] == 0 else 0
    flags['S']  = 1 if (registers['A'] & 0x80) else 0
    flags['P']  = calc_parity(registers['A'])

def exec_ori(data):
    registers['A'] |= data
    flags['CY'] = 0
    flags['AC'] = 0
    flags['Z']  = 1 if registers['A'] == 0 else 0
    flags['S']  = 1 if (registers['A'] & 0x80) else 0
    flags['P']  = calc_parity(registers['A'])

def exec_xra(reg):
    operand = memory[get_hl_addr()] if reg == 'M' else registers[reg]
    registers['A'] ^= operand
    flags['CY'] = 0
    flags['AC'] = 0
    flags['Z']  = 1 if registers['A'] == 0 else 0
    flags['S']  = 1 if (registers['A'] & 0x80) else 0
    flags['P']  = calc_parity(registers['A'])

def exec_xri(data):
    registers['A'] ^= data
    flags['CY'] = 0
    flags['AC'] = 0
    flags['Z']  = 1 if registers['A'] == 0 else 0
    flags['S']  = 1 if (registers['A'] & 0x80) else 0
    flags['P']  = calc_parity(registers['A'])

def exec_cma():
    registers['A'] = (~registers['A']) & 0xFF

def exec_cmc():
    flags['CY'] ^= 1

def exec_stc():
    flags['CY'] = 1

def exec_cmp(reg):
    operand = memory[get_hl_addr()] if reg == 'M' else registers[reg]
    res = registers['A'] - operand
    flags['Z']  = 1 if (res & 0xFF) == 0 else 0
    flags['S']  = 1 if (res & 0x80) else 0
    flags['CY'] = 1 if res < 0 else 0
    flags['AC'] = 1 if (registers['A'] & 0x0F) < (operand & 0x0F) else 0
    flags['P']  = calc_parity(res & 0xFF)

def exec_cpi(data):
    res = registers['A'] - data
    flags['Z']  = 1 if (res & 0xFF) == 0 else 0
    flags['S']  = 1 if (res & 0x80) else 0
    flags['CY'] = 1 if res < 0 else 0
    flags['AC'] = 1 if (registers['A'] & 0x0F) < (data & 0x0F) else 0
    flags['P']  = calc_parity(res & 0xFF)

# ─────────────────────────────────────────────
#  Rotate Instructions
# ─────────────────────────────────────────────

def exec_rlc():
    a = registers['A']
    flags['CY'] = (a >> 7) & 1
    registers['A'] = ((a << 1) | flags['CY']) & 0xFF

def exec_rrc():
    a = registers['A']
    flags['CY'] = a & 1
    registers['A'] = ((a >> 1) | (flags['CY'] << 7)) & 0xFF

def exec_ral():
    a = registers['A']
    new_cy = (a >> 7) & 1
    registers['A'] = ((a << 1) | flags['CY']) & 0xFF
    flags['CY'] = new_cy

def exec_rar():
    a = registers['A']
    new_cy = a & 1
    registers['A'] = ((a >> 1) | (flags['CY'] << 7)) & 0xFF
    flags['CY'] = new_cy

# ─────────────────────────────────────────────
#  Branch Instructions
# ─────────────────────────────────────────────

def exec_jmp(address):   return address
def exec_jc(address):    return address if flags['CY'] else None
def exec_jnc(address):   return address if not flags['CY'] else None
def exec_jz(address):    return address if flags['Z'] else None
def exec_jnz(address):   return address if not flags['Z'] else None
def exec_jm(address):    return address if flags['S'] else None
def exec_jp(address):    return address if not flags['S'] else None
def exec_jpe(address):   return address if flags['P'] else None
def exec_jpo(address):   return address if not flags['P'] else None

def _push_ret_addr(ret_addr):
    registers['SP'] -= 1
    memory[registers['SP']] = (ret_addr >> 8) & 0xFF
    registers['SP'] -= 1
    memory[registers['SP']] = ret_addr & 0xFF

def exec_call(pc, address):
    _push_ret_addr(pc + 3)
    return address

def exec_cc(pc, address):
    if flags['CY']: _push_ret_addr(pc + 3); return address
    return None

def exec_cnc(pc, address):
    if not flags['CY']: _push_ret_addr(pc + 3); return address
    return None

def exec_cz(pc, address):
    if flags['Z']: _push_ret_addr(pc + 3); return address
    return None

def exec_cnz(pc, address):
    if not flags['Z']: _push_ret_addr(pc + 3); return address
    return None

def exec_cm(pc, address):
    if flags['S']: _push_ret_addr(pc + 3); return address
    return None

def exec_cp(pc, address):
    if not flags['S']: _push_ret_addr(pc + 3); return address
    return None

def exec_cpe(pc, address):
    if flags['P']: _push_ret_addr(pc + 3); return address
    return None

def exec_cpo(pc, address):
    if not flags['P']: _push_ret_addr(pc + 3); return address
    return None

def _pop_ret_addr():
    low = memory[registers['SP']]; registers['SP'] += 1
    high = memory[registers['SP']]; registers['SP'] += 1
    return (high << 8) | low

def exec_ret():          return _pop_ret_addr()
def exec_rc():           return _pop_ret_addr() if flags['CY'] else None
def exec_rnc():          return _pop_ret_addr() if not flags['CY'] else None
def exec_rz():           return _pop_ret_addr() if flags['Z'] else None
def exec_rnz():          return _pop_ret_addr() if not flags['Z'] else None
def exec_rm():           return _pop_ret_addr() if flags['S'] else None
def exec_rp():           return _pop_ret_addr() if not flags['S'] else None
def exec_rpe():          return _pop_ret_addr() if flags['P'] else None
def exec_rpo():          return _pop_ret_addr() if not flags['P'] else None

def exec_rst(n, pc):
    _push_ret_addr(pc + 1)
    return n * 8

# ─────────────────────────────────────────────
#  Stack Instructions
# ─────────────────────────────────────────────

def exec_push(reg_pair):
    if reg_pair == 'PSW':
        registers['SP'] -= 1; memory[registers['SP']] = registers['A']
        registers['SP'] -= 1; memory[registers['SP']] = pack_flags()
    elif reg_pair == 'B':
        registers['SP'] -= 1; memory[registers['SP']] = registers['B']
        registers['SP'] -= 1; memory[registers['SP']] = registers['C']
    elif reg_pair == 'D':
        registers['SP'] -= 1; memory[registers['SP']] = registers['D']
        registers['SP'] -= 1; memory[registers['SP']] = registers['E']
    elif reg_pair == 'H':
        registers['SP'] -= 1; memory[registers['SP']] = registers['H']
        registers['SP'] -= 1; memory[registers['SP']] = registers['L']

def exec_pop(reg_pair):
    if reg_pair == 'PSW':
        flag_byte = memory[registers['SP']]; registers['SP'] += 1
        registers['A'] = memory[registers['SP']]; registers['SP'] += 1
        unpack_flags(flag_byte)
    elif reg_pair == 'B':
        registers['C'] = memory[registers['SP']]; registers['SP'] += 1
        registers['B'] = memory[registers['SP']]; registers['SP'] += 1
    elif reg_pair == 'D':
        registers['E'] = memory[registers['SP']]; registers['SP'] += 1
        registers['D'] = memory[registers['SP']]; registers['SP'] += 1
    elif reg_pair == 'H':
        registers['L'] = memory[registers['SP']]; registers['SP'] += 1
        registers['H'] = memory[registers['SP']]; registers['SP'] += 1

def exec_xthl():
    l_val = memory[registers['SP']];     h_val = memory[registers['SP'] + 1]
    memory[registers['SP']]     = registers['L']
    memory[registers['SP'] + 1] = registers['H']
    registers['L'] = l_val;             registers['H'] = h_val

def exec_sphl():
    registers['SP'] = (registers['H'] << 8) | registers['L']

def exec_pchl():
    return (registers['H'] << 8) | registers['L']

# ─────────────────────────────────────────────
#  I/O and Machine Control
# ─────────────────────────────────────────────

def exec_in(port):
    print(f"[IN] Reading from port {hex(port)} — simulated, A set to 0x00")
    registers['A'] = 0x00

def exec_out(port):
    print(f"[OUT] Port {hex(port)} <- A = {hex(registers['A'])}")

def exec_nop():  pass
def exec_di():   pass
def exec_ei():   pass
def exec_rim():  registers['A'] = 0x00
def exec_sim():  pass

# ─────────────────────────────────────────────
#  Main Execution Engine
# ─────────────────────────────────────────────

def fetch_address(addr):
    return (memory[addr + 1] << 8) | memory[addr]

def execute_program(start_addr=0x0000):
    pc = start_addr
    termination_opcodes = {0x76, 0xC7, 0xCF, 0xD7, 0xDF, 0xE7, 0xEF, 0xF7, 0xFF}
    max_steps = 100000

    print(f"\nExecuting program from {hex(pc).upper()}...")

    for _ in range(max_steps):
        opcode = memory[pc]

        if opcode in termination_opcodes:
            print(f"Program terminated at {hex(pc).upper()}H (opcode {hex(opcode).upper()})")
            break

        if   opcode == 0x7F: exec_mov('A','A');  pc += 1
        elif opcode == 0x78: exec_mov('A','B');  pc += 1
        elif opcode == 0x79: exec_mov('A','C');  pc += 1
        elif opcode == 0x7A: exec_mov('A','D');  pc += 1
        elif opcode == 0x7B: exec_mov('A','E');  pc += 1
        elif opcode == 0x7C: exec_mov('A','H');  pc += 1
        elif opcode == 0x7D: exec_mov('A','L');  pc += 1
        elif opcode == 0x7E: exec_mov('A','M');  pc += 1
        elif opcode == 0x47: exec_mov('B','A');  pc += 1
        elif opcode == 0x40: exec_mov('B','B');  pc += 1
        elif opcode == 0x41: exec_mov('B','C');  pc += 1
        elif opcode == 0x42: exec_mov('B','D');  pc += 1
        elif opcode == 0x43: exec_mov('B','E');  pc += 1
        elif opcode == 0x44: exec_mov('B','H');  pc += 1
        elif opcode == 0x45: exec_mov('B','L');  pc += 1
        elif opcode == 0x46: exec_mov('B','M');  pc += 1
        elif opcode == 0x4F: exec_mov('C','A');  pc += 1
        elif opcode == 0x48: exec_mov('C','B');  pc += 1
        elif opcode == 0x49: exec_mov('C','C');  pc += 1
        elif opcode == 0x4A: exec_mov('C','D');  pc += 1
        elif opcode == 0x4B: exec_mov('C','E');  pc += 1
        elif opcode == 0x4C: exec_mov('C','H');  pc += 1
        elif opcode == 0x4D: exec_mov('C','L');  pc += 1
        elif opcode == 0x4E: exec_mov('C','M');  pc += 1
        elif opcode == 0x57: exec_mov('D','A');  pc += 1
        elif opcode == 0x50: exec_mov('D','B');  pc += 1
        elif opcode == 0x51: exec_mov('D','C');  pc += 1
        elif opcode == 0x52: exec_mov('D','D');  pc += 1
        elif opcode == 0x53: exec_mov('D','E');  pc += 1
        elif opcode == 0x54: exec_mov('D','H');  pc += 1
        elif opcode == 0x55: exec_mov('D','L');  pc += 1
        elif opcode == 0x56: exec_mov('D','M');  pc += 1
        elif opcode == 0x5F: exec_mov('E','A');  pc += 1
        elif opcode == 0x58: exec_mov('E','B');  pc += 1
        elif opcode == 0x59: exec_mov('E','C');  pc += 1
        elif opcode == 0x5A: exec_mov('E','D');  pc += 1
        elif opcode == 0x5B: exec_mov('E','E');  pc += 1
        elif opcode == 0x5C: exec_mov('E','H');  pc += 1
        elif opcode == 0x5D: exec_mov('E','L');  pc += 1
        elif opcode == 0x5E: exec_mov('E','M');  pc += 1
        elif opcode == 0x67: exec_mov('H','A');  pc += 1
        elif opcode == 0x60: exec_mov('H','B');  pc += 1
        elif opcode == 0x61: exec_mov('H','C');  pc += 1
        elif opcode == 0x62: exec_mov('H','D');  pc += 1
        elif opcode == 0x63: exec_mov('H','E');  pc += 1
        elif opcode == 0x64: exec_mov('H','H');  pc += 1
        elif opcode == 0x65: exec_mov('H','L');  pc += 1
        elif opcode == 0x66: exec_mov('H','M');  pc += 1
        elif opcode == 0x6F: exec_mov('L','A');  pc += 1
        elif opcode == 0x68: exec_mov('L','B');  pc += 1
        elif opcode == 0x69: exec_mov('L','C');  pc += 1
        elif opcode == 0x6A: exec_mov('L','D');  pc += 1
        elif opcode == 0x6B: exec_mov('L','E');  pc += 1
        elif opcode == 0x6C: exec_mov('L','H');  pc += 1
        elif opcode == 0x6D: exec_mov('L','L');  pc += 1
        elif opcode == 0x6E: exec_mov('L','M');  pc += 1
        elif opcode == 0x77: exec_mov('M','A');  pc += 1
        elif opcode == 0x70: exec_mov('M','B');  pc += 1
        elif opcode == 0x71: exec_mov('M','C');  pc += 1
        elif opcode == 0x72: exec_mov('M','D');  pc += 1
        elif opcode == 0x73: exec_mov('M','E');  pc += 1
        elif opcode == 0x74: exec_mov('M','H');  pc += 1
        elif opcode == 0x75: exec_mov('M','L');  pc += 1
        elif opcode == 0x3E: exec_mvi('A', memory[pc+1]); pc += 2
        elif opcode == 0x06: exec_mvi('B', memory[pc+1]); pc += 2
        elif opcode == 0x0E: exec_mvi('C', memory[pc+1]); pc += 2
        elif opcode == 0x16: exec_mvi('D', memory[pc+1]); pc += 2
        elif opcode == 0x1E: exec_mvi('E', memory[pc+1]); pc += 2
        elif opcode == 0x26: exec_mvi('H', memory[pc+1]); pc += 2
        elif opcode == 0x2E: exec_mvi('L', memory[pc+1]); pc += 2
        elif opcode == 0x36: exec_mvi('M', memory[pc+1]); pc += 2
        elif opcode == 0x01: exec_lxi('B',  memory[pc+2], memory[pc+1]); pc += 3
        elif opcode == 0x11: exec_lxi('D',  memory[pc+2], memory[pc+1]); pc += 3
        elif opcode == 0x21: exec_lxi('H',  memory[pc+2], memory[pc+1]); pc += 3
        elif opcode == 0x31: exec_lxi('SP', memory[pc+2], memory[pc+1]); pc += 3
        elif opcode == 0x3A: exec_lda(fetch_address(pc+1));  pc += 3
        elif opcode == 0x32: exec_sta(fetch_address(pc+1));  pc += 3
        elif opcode == 0x2A: exec_lhld(fetch_address(pc+1)); pc += 3
        elif opcode == 0x22: exec_shld(fetch_address(pc+1)); pc += 3
        elif opcode == 0x0A: exec_ldax('B'); pc += 1
        elif opcode == 0x1A: exec_ldax('D'); pc += 1
        elif opcode == 0x02: exec_stax('B'); pc += 1
        elif opcode == 0x12: exec_stax('D'); pc += 1
        elif opcode == 0xEB: exec_xchg();    pc += 1
        elif opcode == 0x87: exec_add('A'); pc += 1
        elif opcode == 0x80: exec_add('B'); pc += 1
        elif opcode == 0x81: exec_add('C'); pc += 1
        elif opcode == 0x82: exec_add('D'); pc += 1
        elif opcode == 0x83: exec_add('E'); pc += 1
        elif opcode == 0x84: exec_add('H'); pc += 1
        elif opcode == 0x85: exec_add('L'); pc += 1
        elif opcode == 0x86: exec_add('M'); pc += 1
        elif opcode == 0xC6: exec_adi(memory[pc+1]); pc += 2
        elif opcode == 0x8F: exec_adc('A'); pc += 1
        elif opcode == 0x88: exec_adc('B'); pc += 1
        elif opcode == 0x89: exec_adc('C'); pc += 1
        elif opcode == 0x8A: exec_adc('D'); pc += 1
        elif opcode == 0x8B: exec_adc('E'); pc += 1
        elif opcode == 0x8C: exec_adc('H'); pc += 1
        elif opcode == 0x8D: exec_adc('L'); pc += 1
        elif opcode == 0x8E: exec_adc('M'); pc += 1
        elif opcode == 0xCE: exec_aci(memory[pc+1]); pc += 2
        elif opcode == 0x97: exec_sub('A'); pc += 1
        elif opcode == 0x90: exec_sub('B'); pc += 1
        elif opcode == 0x91: exec_sub('C'); pc += 1
        elif opcode == 0x92: exec_sub('D'); pc += 1
        elif opcode == 0x93: exec_sub('E'); pc += 1
        elif opcode == 0x94: exec_sub('H'); pc += 1
        elif opcode == 0x95: exec_sub('L'); pc += 1
        elif opcode == 0x96: exec_sub('M'); pc += 1
        elif opcode == 0xD6: exec_sui(memory[pc+1]); pc += 2
        elif opcode == 0x9F: exec_sbb('A'); pc += 1
        elif opcode == 0x98: exec_sbb('B'); pc += 1
        elif opcode == 0x99: exec_sbb('C'); pc += 1
        elif opcode == 0x9A: exec_sbb('D'); pc += 1
        elif opcode == 0x9B: exec_sbb('E'); pc += 1
        elif opcode == 0x9C: exec_sbb('H'); pc += 1
        elif opcode == 0x9D: exec_sbb('L'); pc += 1
        elif opcode == 0x9E: exec_sbb('M'); pc += 1
        elif opcode == 0xDE: exec_sbi(memory[pc+1]); pc += 2
        elif opcode == 0x3C: exec_inr('A'); pc += 1
        elif opcode == 0x04: exec_inr('B'); pc += 1
        elif opcode == 0x0C: exec_inr('C'); pc += 1
        elif opcode == 0x14: exec_inr('D'); pc += 1
        elif opcode == 0x1C: exec_inr('E'); pc += 1
        elif opcode == 0x24: exec_inr('H'); pc += 1
        elif opcode == 0x2C: exec_inr('L'); pc += 1
        elif opcode == 0x34: exec_inr('M'); pc += 1
        elif opcode == 0x3D: exec_dcr('A'); pc += 1
        elif opcode == 0x05: exec_dcr('B'); pc += 1
        elif opcode == 0x0D: exec_dcr('C'); pc += 1
        elif opcode == 0x15: exec_dcr('D'); pc += 1
        elif opcode == 0x1D: exec_dcr('E'); pc += 1
        elif opcode == 0x25: exec_dcr('H'); pc += 1
        elif opcode == 0x2D: exec_dcr('L'); pc += 1
        elif opcode == 0x35: exec_dcr('M'); pc += 1
        elif opcode == 0x03: exec_inx('B');  pc += 1
        elif opcode == 0x13: exec_inx('D');  pc += 1
        elif opcode == 0x23: exec_inx('H');  pc += 1
        elif opcode == 0x33: exec_inx('SP'); pc += 1
        elif opcode == 0x0B: exec_dcx('B');  pc += 1
        elif opcode == 0x1B: exec_dcx('D');  pc += 1
        elif opcode == 0x2B: exec_dcx('H');  pc += 1
        elif opcode == 0x3B: exec_dcx('SP'); pc += 1
        elif opcode == 0x09: exec_dad('B');  pc += 1
        elif opcode == 0x19: exec_dad('D');  pc += 1
        elif opcode == 0x29: exec_dad('H');  pc += 1
        elif opcode == 0x39: exec_dad('SP'); pc += 1
        elif opcode == 0x27: exec_daa(); pc += 1
        elif opcode == 0xA7: exec_ana('A'); pc += 1
        elif opcode == 0xA0: exec_ana('B'); pc += 1
        elif opcode == 0xA1: exec_ana('C'); pc += 1
        elif opcode == 0xA2: exec_ana('D'); pc += 1
        elif opcode == 0xA3: exec_ana('E'); pc += 1
        elif opcode == 0xA4: exec_ana('H'); pc += 1
        elif opcode == 0xA5: exec_ana('L'); pc += 1
        elif opcode == 0xA6: exec_ana('M'); pc += 1
        elif opcode == 0xE6: exec_ani(memory[pc+1]); pc += 2
        elif opcode == 0xB7: exec_ora('A'); pc += 1
        elif opcode == 0xB0: exec_ora('B'); pc += 1
        elif opcode == 0xB1: exec_ora('C'); pc += 1
        elif opcode == 0xB2: exec_ora('D'); pc += 1
        elif opcode == 0xB3: exec_ora('E'); pc += 1
        elif opcode == 0xB4: exec_ora('H'); pc += 1
        elif opcode == 0xB5: exec_ora('L'); pc += 1
        elif opcode == 0xB6: exec_ora('M'); pc += 1
        elif opcode == 0xF6: exec_ori(memory[pc+1]); pc += 2
        elif opcode == 0xAF: exec_xra('A'); pc += 1
        elif opcode == 0xA8: exec_xra('B'); pc += 1
        elif opcode == 0xA9: exec_xra('C'); pc += 1
        elif opcode == 0xAA: exec_xra('D'); pc += 1
        elif opcode == 0xAB: exec_xra('E'); pc += 1
        elif opcode == 0xAC: exec_xra('H'); pc += 1
        elif opcode == 0xAD: exec_xra('L'); pc += 1
        elif opcode == 0xAE: exec_xra('M'); pc += 1
        elif opcode == 0xEE: exec_xri(memory[pc+1]); pc += 2
        elif opcode == 0x2F: exec_cma(); pc += 1
        elif opcode == 0x3F: exec_cmc(); pc += 1
        elif opcode == 0x37: exec_stc(); pc += 1
        elif opcode == 0xBF: exec_cmp('A'); pc += 1
        elif opcode == 0xB8: exec_cmp('B'); pc += 1
        elif opcode == 0xB9: exec_cmp('C'); pc += 1
        elif opcode == 0xBA: exec_cmp('D'); pc += 1
        elif opcode == 0xBB: exec_cmp('E'); pc += 1
        elif opcode == 0xBC: exec_cmp('H'); pc += 1
        elif opcode == 0xBD: exec_cmp('L'); pc += 1
        elif opcode == 0xBE: exec_cmp('M'); pc += 1
        elif opcode == 0xFE: exec_cpi(memory[pc+1]); pc += 2
        elif opcode == 0x07: exec_rlc(); pc += 1
        elif opcode == 0x0F: exec_rrc(); pc += 1
        elif opcode == 0x17: exec_ral(); pc += 1
        elif opcode == 0x1F: exec_rar(); pc += 1
        elif opcode == 0xC3:
            pc = exec_jmp(fetch_address(pc+1))
        elif opcode == 0xDA:
            res = exec_jc(fetch_address(pc+1));   pc = res if res is not None else pc + 3
        elif opcode == 0xD2:
            res = exec_jnc(fetch_address(pc+1));  pc = res if res is not None else pc + 3
        elif opcode == 0xCA:
            res = exec_jz(fetch_address(pc+1));   pc = res if res is not None else pc + 3
        elif opcode == 0xC2:
            res = exec_jnz(fetch_address(pc+1));  pc = res if res is not None else pc + 3
        elif opcode == 0xFA:
            res = exec_jm(fetch_address(pc+1));   pc = res if res is not None else pc + 3
        elif opcode == 0xF2:
            res = exec_jp(fetch_address(pc+1));   pc = res if res is not None else pc + 3
        elif opcode == 0xEA:
            res = exec_jpe(fetch_address(pc+1));  pc = res if res is not None else pc + 3
        elif opcode == 0xE2:
            res = exec_jpo(fetch_address(pc+1));  pc = res if res is not None else pc + 3
        elif opcode == 0xCD:
            pc = exec_call(pc, fetch_address(pc+1))
        elif opcode == 0xDC:
            res = exec_cc(pc,  fetch_address(pc+1));  pc = res if res is not None else pc + 3
        elif opcode == 0xD4:
            res = exec_cnc(pc, fetch_address(pc+1));  pc = res if res is not None else pc + 3
        elif opcode == 0xCC:
            res = exec_cz(pc,  fetch_address(pc+1));  pc = res if res is not None else pc + 3
        elif opcode == 0xC4:
            res = exec_cnz(pc, fetch_address(pc+1));  pc = res if res is not None else pc + 3
        elif opcode == 0xFC:
            res = exec_cm(pc,  fetch_address(pc+1));  pc = res if res is not None else pc + 3
        elif opcode == 0xF4:
            res = exec_cp(pc,  fetch_address(pc+1));  pc = res if res is not None else pc + 3
        elif opcode == 0xEC:
            res = exec_cpe(pc, fetch_address(pc+1));  pc = res if res is not None else pc + 3
        elif opcode == 0xE4:
            res = exec_cpo(pc, fetch_address(pc+1));  pc = res if res is not None else pc + 3
        elif opcode == 0xC9: pc = exec_ret()
        elif opcode == 0xD8:
            res = exec_rc();  pc = res if res is not None else pc + 1
        elif opcode == 0xD0:
            res = exec_rnc(); pc = res if res is not None else pc + 1
        elif opcode == 0xC8:
            res = exec_rz();  pc = res if res is not None else pc + 1
        elif opcode == 0xC0:
            res = exec_rnz(); pc = res if res is not None else pc + 1
        elif opcode == 0xF8:
            res = exec_rm();  pc = res if res is not None else pc + 1
        elif opcode == 0xF0:
            res = exec_rp();  pc = res if res is not None else pc + 1
        elif opcode == 0xE8:
            res = exec_rpe(); pc = res if res is not None else pc + 1
        elif opcode == 0xE0:
            res = exec_rpo(); pc = res if res is not None else pc + 1
        elif opcode == 0xC5: exec_push('B');   pc += 1
        elif opcode == 0xD5: exec_push('D');   pc += 1
        elif opcode == 0xE5: exec_push('H');   pc += 1
        elif opcode == 0xF5: exec_push('PSW'); pc += 1
        elif opcode == 0xC1: exec_pop('B');    pc += 1
        elif opcode == 0xD1: exec_pop('D');    pc += 1
        elif opcode == 0xE1: exec_pop('H');    pc += 1
        elif opcode == 0xF1: exec_pop('PSW');  pc += 1
        elif opcode == 0xE3: exec_xthl();      pc += 1
        elif opcode == 0xF9: exec_sphl();      pc += 1
        elif opcode == 0xE9: pc = exec_pchl()
        elif opcode == 0xC7: pc = exec_rst(0, pc); break
        elif opcode == 0xCF: pc = exec_rst(1, pc); break
        elif opcode == 0xD7: pc = exec_rst(2, pc); break
        elif opcode == 0xDF: pc = exec_rst(3, pc); break
        elif opcode == 0xE7: pc = exec_rst(4, pc); break
        elif opcode == 0xEF: pc = exec_rst(5, pc); break
        elif opcode == 0xF7: pc = exec_rst(6, pc); break
        elif opcode == 0xFF: pc = exec_rst(7, pc); break
        elif opcode == 0xDB: exec_in(memory[pc+1]);  pc += 2
        elif opcode == 0xD3: exec_out(memory[pc+1]); pc += 2
        elif opcode == 0x00: exec_nop(); pc += 1
        elif opcode == 0xF3: exec_di();  pc += 1
        elif opcode == 0xFB: exec_ei();  pc += 1
        elif opcode == 0x20: exec_rim(); pc += 1
        elif opcode == 0x30: exec_sim(); pc += 1
        else:
            print(f"Unknown opcode {hex(opcode)} at {hex(pc)} — halting.")
            break
    else:
        print("Max steps reached — possible infinite loop, halting.")

    print("\n--- Final Register State ---")
    for reg, val in registers.items():
        if reg in ('SP', 'PC'):
            print(f"  {reg} : {hex(val).upper()}")
        else:
            print(f"  {reg}  : {hex(val).upper()} ({val})")
    print("\n--- Flags ---")
    for f, v in flags.items():
        print(f"  {f} = {v}")


# ─────────────────────────────────────────────
#  Assembly / Load Phase
# ─────────────────────────────────────────────

termination_opcodes = ["76", "C7", "CF", "D7", "DF", "E7", "EF", "F7", "FF"]

pc = 0x0000

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