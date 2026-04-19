from memory import flags, registers, memory
from flags import calc_parity, update_flags, pack_flags,unpack_flags
from instructions import (
    get_hl_addr,

    exec_mov, exec_mvi, exec_lxi, exec_lda, exec_sta,
    exec_lhld, exec_shld, exec_ldax, exec_stax, exec_xchg,

    exec_add, exec_adi, exec_adc, exec_aci, exec_sub,
    exec_sui, exec_sbb, exec_sbi, exec_inr, exec_dcr,
    exec_inx, exec_dcx, exec_dad, exec_daa,

    exec_ana, exec_ani, exec_ora, exec_ori, exec_xra,
    exec_xri, exec_cma, exec_cmc, exec_stc, exec_cmp, exec_cpi,

    exec_rlc, exec_rrc, exec_ral, exec_rar,

    exec_jmp, exec_jc, exec_jnc, exec_jz, exec_jnz,
    exec_jm, exec_jp, exec_jpe, exec_jpo,

    _push_ret_addr, exec_call, exec_cc, exec_cnc, exec_cz,
    exec_cnz, exec_cm, exec_cp, exec_cpe, exec_cpo,

    _pop_ret_addr, exec_ret, exec_rc, exec_rnc, exec_rz,
    exec_rnz, exec_rm, exec_rp, exec_rpe, exec_rpo,

    exec_rst,

    exec_push, exec_pop, exec_xthl, exec_sphl, exec_pchl,

    exec_in, exec_out, exec_nop, exec_di, exec_ei,
    exec_rim, exec_sim
)






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
