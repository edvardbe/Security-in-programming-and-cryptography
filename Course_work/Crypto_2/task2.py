from Crypto.Cipher import AES

K1 = bytes.fromhex("0123456789ABCDEF0123456789ABCDEF")
K2 = bytes.fromhex("1123456789ABCDEF0123456789ABCDEF")

x1 = bytes.fromhex("01000000000000000000000000000000")
x2 = bytes.fromhex("02000000000000000000000000000000")

def xor(message, key):
  encrypted_message = []
  for i in range(len(message)):
    message_byte = message[i]
    key_byte = key[i]
    encrypted_byte = message_byte ^ key_byte
    encrypted_message.append(encrypted_byte)
  return bytes(encrypted_message)



# AES results from https://legacy.cryptool.org/en/cto/aes-step-by-step
# a)
x1_aes_one = bytes.fromhex("01fcf41f4c13eaaa96747c97c49b6222")
x2_aes_one = bytes.fromhex("01fcf41f4c13eaaa96747c97c49b6222")

x1_aes_full = bytes.fromhex("01fcf41f4c13eaaa96747c97c49b6222")
x2_aes_full = bytes.fromhex("01fcf41f4c13eaaa96747c97c49b6222")

# b)
K1_aes_one = bytes.fromhex("01fcf41f4c13eaaa96747c97c49b6222")
K2_aes_one = bytes.fromhex("01fcf41f4c13eaaa96747c97c49b6222")

K1_aes_full = bytes.fromhex("01fcf41f4c13eaaa96747c97c49b6222")
K2_aes_full = bytes.fromhex("01fcf41f4c13eaaa96747c97c49b6222")



if __name__ == "__main__":
  print(" -- Subtask a) -- \n")
  print(f"XOR message x1: \n {xor(x1, K1).hex()}\n")
  print(f"XOR message x2: \n {xor(x2, K1).hex()}")
  
  