file = open("config/config.txt", "r")
lines = file.readlines()
file.close()

interval = 0
sequence_length = 0

for line in lines:
    line = line.strip()
    
    if line.startswith("interval="):
        interval = int(line.split("=")[1])
    
    if line.startswith("sequence_length="):
        sequence_length = int(line.split("=")[1])

print("interval =", interval)
print("sequence_length =", sequence_length)