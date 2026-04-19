from memory import flags, registers, memory


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
