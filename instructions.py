from memory import flags, registers, memory
from flags import calc_parity, update_flags, pack_flags,unpack_flags



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
