from dynadown import register_plugin

class BrainfuckPlugin:
    def __init__(self):
        pass
    def evaluate(self, block):
        # Some variables we'll use
        num_registers = 30000
        registers = [0] * num_registers
        output = ''
        current_register = 0
        pos = 0
        jump_positions = []

        # Brainfuck interpreting!
        while pos < len(block):
            char = block[pos]

            if char == '>':
                current_register = (current_register + 1) % num_registers

            elif char == '<':
                current_register = (current_register - 1) % num_registers

            elif char == ',':
                raise Exception("Can't take input while parsing")

            elif char == '.':
                output += chr(registers[current_register])

            elif char == '[':
                if registers[current_register] == 0:
                    pos = find_jump_end(block, pos)
                else:
                    jump_positions.append(pos - 1)  # -1 to counter pointer inc

            elif char == ']':
                matching_brace = jump_positions.pop()
                if registers[current_register] == 0:
                    pass
                else:
                    pos = matching_brace

            elif char == '+':
                registers[current_register] += 1

            elif char == '-':
                registers[current_register] -= 1

            pos += 1

        return output

def find_jump_end(block, pos):
    char = block[pos]
    while char != ']':
        pos += 1
        char = block[pos]
    return pos

register_plugin('brainfuck', BrainfuckPlugin)
