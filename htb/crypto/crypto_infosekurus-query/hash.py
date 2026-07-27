from Crypto.Cipher import AES
from Crypto.Util.number import long_to_bytes, bytes_to_long
from hashlib import md5
import itertools

# Your hash outputs
hash_outputs = {
    "00" * 16: bytes.fromhex("6474fe8f6eb7e35201c7cca307e3654b"),
    "01" * 16: bytes.fromhex("8b3a274982cbb5c50f3818a76b6e2e90"),
    "02" * 16: bytes.fromhex("8cadf1c0344b93c2859e6a7402aaae0e"),
}

# Known inputs as bytes
known_inputs = {
    "00" * 16: b"\x00" * 16,
    "01" * 16: b"\x01" * 16,
    "02" * 16: b"\x02" * 16,
}

# The hash_digest function:
# to_hash = pad(key + extra + message)
# seed = b"\xff" * 16
# blocks = [b"\xfe" * 16] + [to_hash[i:i+16] ...]
# for b in range(1, len(blocks)):
#     cipher = AES.new(blocks[b], AES.MODE_ECB)
#     seed = bxor(cipher.encrypt(blshift(seed, blocks[b-1])), seed)

# For 16-byte input, the blocks are:
# block0 = key[0:16]
# block1 = key[16:32]
# block2 = key[32:48]
# block3 = extra[0:16]
# block4 = message + padding (16 bytes + padding)

# The padding for 16-byte message:
# message + b"\x80" + zeros until length % 32 == 28 + length (4 bytes)
# 16 + 1 + 11 + 4 = 32 bytes, so block4 is 16 bytes of message + padding

print("[*] Reversing the hash function...")

# Try to recover the key by brute forcing small parts
# The key is 48 bytes, extra is 16 bytes = 64 bytes total
# We can try to recover them by analyzing the AES encryption

# For a known input, we know the final seed (the hash output)
# We can work backwards through the blocks

# Start from the last block
for input_hex, input_bytes in known_inputs.items():
    print(f"\n[*] Analyzing input: {input_hex[:10]}...")
    
    # The hash output is the final seed
    final_seed = hash_outputs[input_hex]
    print(f"    Final seed: {final_seed.hex()[:16]}...")
    
    # Working backwards:
    # seed_before_last = bxor(AES_decrypt(final_seed), seed_before_last)
    # But we need to know the previous seed
    
    # This requires reversing AES-ECB encryption without the key
    # Since we don't have the key, we need to find a different approach
    
print("\n[!] Cannot reverse AES without the key")
print("[!] Need to find a vulnerability in the hash construction")

# The vulnerability: the blocks are used as AES keys
# If we can control a block to be a known value, we can get AES encryption
# of the seed under that key

# For 32-byte input:
# block0 = key[0:16]
# block1 = key[16:32]
# block2 = key[32:48]
# block3 = extra[0:16]
# block4 = message[0:16]
# block5 = message[16:32] + padding

# If we send a 32-byte message where message[0:16] = known value,
# then block4 = known value, and we get AES encryption under that key!

print("\n[*] Send a 32-byte message to Option 2:")
print('    {"hash": "00" * 32}')
print('    {"hash": "01" * 32}')
print('    {"hash": "02" * 32}')

print("\n[!] This will reveal the AES encryption under known keys")
print("[!] Then we can recover the key by reversing the XOR operations")