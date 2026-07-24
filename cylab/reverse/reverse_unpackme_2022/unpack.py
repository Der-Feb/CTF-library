# Simple UPX unpacker if it's actually UPX
import sys
with open("unpackme-upx", "rb") as f:
    data = f.read()
    
# Find UPX! magic
idx = data.find(b"UPX!")
if idx != -1:
    # Extract from UPX! to end
    unpacked = data[idx:]
    with open("unpacked", "wb") as f:
        f.write(unpacked)
    print("Extracted UPX section")