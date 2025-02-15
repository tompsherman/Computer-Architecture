"""CPU functionality."""

import sys

# opcodes:
HLT =  0b00000001
LDI =  0b10000010
PRN =  0b01000111
MUL =  0b10100010

class CPU:
    """Main CPU class."""

    def __init__(self):
        """Construct a new CPU.
        program count
        ram
        registers
        def ram.read
        ram.write
        inspec
        """

        self.ram = [0]*256
        self.pc = 0
        self.registers = [0] * 8
        
    def ram_read(self, address):
        return self.ram[address]
            

    def ram_write(self, value, address):
        self.ram[address] = value


    def load(self, filename):
        """Load a program into memory."""

        try:
            address = 0
            with open(filename) as f:
                for line in f:
                    comment_split = line.split('#')
                    data = comment_split[0].strip()
                    if data == '':
                        continue
                    val = int(data, 2)
                    self.ram[address] = val
                    address += 1
        except FileNotFoundError:
            print (f"{sys.argv[0]}: {sys.argv[1]} not found")
            sys.exit(2)
        # For now, we've just hardcoded a program:

        # program = [
        #     # From print8.ls8
        #     0b10000010, # LDI R0,8
        #     0b00000000,
        #     0b00001000,
        #     0b01000111, # PRN R0
        #     0b00000000,
        #     0b00000001, # HLT
        # ]

        # for instruction in program:
        #     self.ram[address] = instruction
        #     address += 1


    def alu(self, op, reg_a, reg_b):
        """ALU operations."""

        if op == "ADD":
            self.reg[reg_a] += self.reg[reg_b]
        #elif op == "SUB": etc
        else:
            raise Exception("Unsupported ALU operation")

    def trace(self):
        """
        Handy function to print out the CPU state. You might want to call this
        from run() if you need help debugging.
        """

        print(f"TRACE: %02X | %02X %02X %02X |" % (
            self.pc,
            #self.fl,
            #self.ie,
            self.ram_read(self.pc),
            self.ram_read(self.pc + 1),
            self.ram_read(self.pc + 2)
        ), end='')

        for i in range(8):
            print(" %02X" % self.reg[i], end='')

        print()

    def run(self):
        """Run the CPU.
        while loop, 
        check conditional, 
        close to copy and paste of what we did (may have to do self.pc etc.)
        """
        while True:
            #FETCH
            instruction = self.ram[self.pc]

            #DECODE
            if instruction == HLT:
                #EXECUTE
                break
            #DECODE
            elif instruction == LDI:
                #EXECUTE
                reg_index = self.ram[self.pc + 1]
                num = self.ram[self.pc+2]
                self.registers[reg_index] = num
                self.pc += 3
            #DECODE
            elif instruction == PRN:
                #EXECUTE
                reg_index = self.ram[self.pc + 1]
                num = self.registers[reg_index]
                print(num)
                self.pc += 2
            #DECODE
            elif instruction == MUL:
                #EXECUTE
                reg_index_A = self.ram[self.pc + 1]
                reg_index_B = self.ram[self.pc +2]
                num = self.registers[reg_index_A] * self.registers[reg_index_B]
                self.registers[reg_index_A] = num
                self.pc += 3
            #DECODE
            else:
                #EXECUTE
                print("We got a big f#c%in problem, Morty!")
        
