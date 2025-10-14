import os
import sys

# Target output file
output_file = "MHPSP.bin"

# Size to pad each file to (0x6800 bytes)
PAD_SIZE = 0x6800

# Get all .mib files in current directory, sorted alphabetically
mib_files = sorted(f for f in os.listdir('.') if f.lower().endswith('.mib'))

if not mib_files:
    print("No .mib files found in the current directory.")
    sys.exit(1)

print(f"Found {len(mib_files)} .mib files. Processing in alphabetical order:")

with open(output_file, 'wb') as out_f:
    for idx, mib in enumerate(mib_files, start=1):
        print(f"[{idx}/{len(mib_files)}] Processing file: {mib}")
        with open(mib, 'rb') as in_f:
            data = in_f.read()
            if len(data) > PAD_SIZE:
                print(f"Error: '{mib}' exceeds {PAD_SIZE} bytes. Aborting.")
                sys.exit(1)
            # Pad with zeros if smaller
            if len(data) < PAD_SIZE:
                data += b'\x00' * (PAD_SIZE - len(data))
            out_f.write(data)

print(f"Created '{output_file}' from {len(mib_files)} .mib files successfully.")
