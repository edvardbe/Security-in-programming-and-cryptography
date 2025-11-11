def e_caesar(x):
    return (x + 3) & 0xFF

def cbc_mac(message_blocks):
    C = 0
    for block in message_blocks:
        C = e_caesar(block ^ C)
    return C

x_blocks = [0b11011111, 0b10100001]

x_prime_blocks = [0b00101100, 0b00011111]

mac_x = cbc_mac(x_blocks)
mac_x_prime = cbc_mac(x_prime_blocks)

print(f"CBC-MAC for x = {bin(mac_x)[2:].zfill(8)}")
print(f"CBC-MAC for x' = {bin(mac_x_prime)[2:].zfill(8)}")
