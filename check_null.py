import os
for root, dirs, files in os.walk('.'):
    for f in files:
        if f.endswith('.py'):
            path = os.path.join(root, f)
            try:
                if b'\x00' in open(path, 'rb').read():
                    print(f"FOUND NULL BYTES: {path}")
            except Exception as e:
                print(f"Error reading {path}: {e}")
