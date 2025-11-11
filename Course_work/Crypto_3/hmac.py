def midsquare_hash(x):
    squared = x * x
    squared &= 0xFF
    
    middle = (squared >> 2) & 0b1111
    return middle

def hmac(message, key, ipad, opad):
    inner_input = (key ^ ipad) ^ message
    inner_hash = midsquare_hash(inner_input)

    outer_input = (key ^ opad) ^ inner_hash
    outer_hash = midsquare_hash(outer_input)

    return outer_hash

# Given parameters
K = 0b1001
ipad = 0b0011
opad = 0b0101

# a) Message 0110
message_a = 0b0110
hmac_a = hmac(message_a, K, ipad, opad)
print("-- a) --")
print("HMAC for 0110:", bin(hmac_a)[2:].zfill(4))

# b) Message 0111 with HMAC 0100
message_b = 0b0111
received_hmac = 0b0100
calculated_hmac = hmac(message_b, K, ipad, opad)
print("\n-- b) --")
print("Calculated HMAC for 0111:", bin(calculated_hmac)[2:].zfill(4))
print("Is message authentic?", calculated_hmac == received_hmac)