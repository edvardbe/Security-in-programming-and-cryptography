class LFSR:
    def __init__(self, seed, taps, num_bits=None):
        self.seed = seed
        self.state = seed
        self.taps = taps
        self.num_bits = num_bits if num_bits is not None else seed.bit_length()

    def next_bit(self):                
        feedback_bit = 0
        for tap in self.taps:
            feedback_bit ^= (self.state >> (tap - 1)) & 1

        self.state = ((self.state << 1) | feedback_bit) & ((1 << self.num_bits) - 1)
        return feedback_bit

    def generate_sequence(self, length):
        sequence = []
        mapping = {}
        for _ in range(length):
            state_key = bin(self.state)[2:].zfill(self.num_bits)
            bit = self.next_bit()
            mapping[state_key] = bit
            sequence.append(bit)
        return sequence, mapping

# A 4-bit LFSR with taps at positions 1 and 4 
# representing C = (1, 0, 0, 1) or z_4 = (z_1 + z_3) mod 2
# Seed: 0b1000 (decimal 8)
print("-- K = 1000: --")
lfsr = LFSR(seed=0b1000, taps=[1, 4], num_bits=4)
sequence, map = lfsr.generate_sequence(30) # Generate 30 bits
print("Map:", map)
print("Sequence:", sequence)
print("Periods:", len(map), "\n")



"""
1000 : 1
0001 : 1
0011 : 1
0111 : 1
1111 : 0
1110 : 1
1101 : 0
1010 : 1
0101 : 1
1011 : 1
0110 : 0
1100 : 1
1001 : 0
0010 : 0
0100 : 0
1000 : 1 -- Period
"""

print("-- K = 0011: --")
lfsr = LFSR(seed=0b0011, taps=[4, 1], num_bits=4)
sequence, map = lfsr.generate_sequence(30) # Generate 30 bits
print("Map:", map)
print("Sequence:", sequence)
print("Periods:", len(map), "\n")

print("-- K = 1111: --")
lfsr = LFSR(seed=0b1111, taps=[4, 1], num_bits=4)
sequence, map = lfsr.generate_sequence(30) # Generate 30 bits
print("Map:", map)
print("Sequence:", sequence)
print("Periods:", len(map), "\n")
