from Crypto.Util.number import long_to_bytes, bytes_to_long

# Known plaintext
message = b"Our counter agencies have intercepted your messages and a lot "
message += b"of your agent's identities have been exposed. In a matter of "
message += b"days all of them will be captured"

# Data from out.txt
iv_hex = "c4a66edfe80227b4fa24d431"
encrypted_message_hex = "7aa34395a258f5893e3db1822139b8c1f04cfab9d757b9b9cca57e1df33d093f07c7f06e06bb6293676f9060a838ea138b6bc9f20b08afeb73120506e2ce7b9b9dcd9e4a421584cfaba2481132dfbdf4216e98e3facec9ba199ca3a97641e9ca9782868d0222a1d7c0d3119b867edaf2e72e2a6f7d344df39a14edc39cb6f960944ddac2aaef324827c36cba67dcb76b22119b43881a3f1262752990"
encrypted_flag_hex = "7d8273ceb459e4d4386df4e32e1aecc1aa7aaafda50cb982f6c62623cf6b29693d86b15457aa76ac7e2eef6cf814ae3a8d39c7"

# Convert hex to bytes
encrypted_message = bytes.fromhex(encrypted_message_hex)
encrypted_flag = bytes.fromhex(encrypted_flag_hex)

# Ensure lengths match (the keystream is the same length as the plaintext)
# The known message is longer than the flag, so we only need the first len(flag) bytes of keystream
keystream = bytes([m ^ c for m, c in zip(message, encrypted_message)])
flag = bytes([k ^ c for k, c in zip(keystream, encrypted_flag)])

print(flag.decode())