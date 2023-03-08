import os
path = input()
#"C:\pp2"
exists = os.access(path, os.F_OK)
reads = os.access(path, os.R_OK)
writes = os.access(path, os.W_OK)
executes = os.access(path, os.X_OK)
print("Existence:", exists)
print("Readable:", reads)
print("Writable:", writes)
print("Executable:", executes)