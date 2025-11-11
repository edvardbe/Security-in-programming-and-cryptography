from Crypto.Cipher import AES

# --- Data setup ---
K1_hex = "0123456789ABCDEF0123456789ABCDEF"
K2_hex = "1123456789ABCDEF0123456789ABCDEF"
x1_hex = "01000000000000000000000000000000"
x2_hex = "02000000000000000000000000000000"

K1 = bytes.fromhex(K1_hex)
K2 = bytes.fromhex(K2_hex)
x1 = bytes.fromhex(x1_hex)
x2 = bytes.fromhex(x2_hex)

# --- Helper functions ---
def xor_bytes(a: bytes, b: bytes) -> bytes:
    return bytes(x ^ y for x, y in zip(a, b))

def compare_bytes(a: bytes, b: bytes):
    """Return (byte_diffs, bit_diffs)."""
    assert len(a) == len(b)
    byte_diffs = sum(1 for x, y in zip(a, b) if x != y)
    bit_diffs = sum(bin(x ^ y).count("1") for x, y in zip(a, b))
    return byte_diffs, bit_diffs

# --- Cipher B: Affine over Z/(2^128), a=b=key ---
def affine_encrypt(key: bytes, plaintext: bytes) -> bytes:
    a = int.from_bytes(key, "big")
    b = a
    x = int.from_bytes(plaintext, "big")
    y = (a * x + b) % (1 << 128)
    return y.to_bytes(16, "big")

# --- Compute encryptions ---
def run_cipher_tests():
    ciphers = {}

    # OTP
    ciphers["OTP_K1_x1"] = xor_bytes(K1, x1)
    ciphers["OTP_K1_x2"] = xor_bytes(K1, x2)
    ciphers["OTP_K2_x1"] = xor_bytes(K2, x1)

    # Affine
    ciphers["Affine_K1_x1"] = affine_encrypt(K1, x1)
    ciphers["Affine_K1_x2"] = affine_encrypt(K1, x2)
    ciphers["Affine_K2_x1"] = affine_encrypt(K2, x1)


    # AES results from https://legacy.cryptool.org/en/cto/aes-step-by-step
    # --- Cipher C: One round of AES ---
    ciphers["AES1_K1_x1"] = bytes.fromhex("01fcf41f4c13eaaa96747c97c49b6222")
    ciphers["AES1_K1_x2"] = bytes.fromhex("19fcf41f4c13eaaa96747c97c49b6222")
    ciphers["AES1_K2_x1"] = bytes.fromhex("bf5c82a95b8de3b527c4c697cc3bcbfb")

    # --- Cipher D: Full AES ---
    ciphers["AESfull_K1_x1"] = bytes.fromhex("6b86f1a935db65e73e29b6d74dfe9d33")
    ciphers["AESfull_K1_x2"] = bytes.fromhex("29b542fd4719deeacdc6b45ca2eee764")
    ciphers["AESfull_K2_x1"] = bytes.fromhex("ed9d8fd0fd632de93fd5197ed1c37fea")

    return ciphers

# --- Run and compare ---
results = run_cipher_tests()

print("\nPart (a): diffusion when plaintext changes (x1 vs x2, same key K1)")
for name, (c1_key, c2_key) in {
    "OTP": ("OTP_K1_x1", "OTP_K1_x2"),
    "Affine": ("Affine_K1_x1", "Affine_K1_x2"),
    "AES1": ("AES1_K1_x1", "AES1_K1_x2"),
    "AESfull": ("AESfull_K1_x1", "AESfull_K1_x2")
}.items():
    bytes_diff, bits_diff = compare_bytes(results[c1_key], results[c2_key])
    print(f"{name}: {bytes_diff}/16 bytes, {bits_diff}/128 bits changed")

print("\nPart (b): diffusion when key changes (K1 vs K2, same plaintext x1)")
for name, (c1_key, c2_key) in {
    "OTP": ("OTP_K1_x1", "OTP_K2_x1"),
    "Affine": ("Affine_K1_x1", "Affine_K2_x1"),
    "AES1": ("AES1_K1_x1", "AES1_K2_x1"),
    "AESfull": ("AESfull_K1_x1", "AESfull_K2_x1")
}.items():
    bytes_diff, bits_diff = compare_bytes(results[c1_key], results[c2_key])
    print(f"{name}: {bytes_diff}/16 bytes, {bits_diff}/128 bits changed")

# Optional: print ciphertexts
print("\nCiphertexts (for verification):")
for k, v in results.items():
    print(f"{k}: {v.hex().upper()}")
