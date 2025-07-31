f = open("demo.txt", "w")
f.write("Python file handling example.")
f.close()

f = open("demo.txt", "r")
print(f.read(6))     # Output: Python
f.seek(0)            # Move pointer to beginning
print(f.read(4))     # Output: Pyth
f.seek(7)            # Move to 7th byte
print(f.read(4))     # Output: file
f.close()
