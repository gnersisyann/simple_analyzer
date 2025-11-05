import time
import random
from analyzer import Analyzer

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

analyzer = Analyzer()

while 1:
    random_number = random.randint(1, 100)
    print("Generated number:", random_number)
    
    analyzer.add_number(random_number)
    
    if len(analyzer.numbers) > sequence_length:
        analyzer.numbers.pop(0)
    
    print("Even numbers:", analyzer.even_count())
    print("Odd numbers:", analyzer.odd_count())
    print("Highest number:", analyzer.highest_number())
    print("Increasing pairs:", analyzer.increasing_pairs())
    print("Total numbers:", len(analyzer.numbers))
    print("---")
    
    current_time = time.localtime()
    current_seconds = current_time.tm_sec
    
    if len(analyzer.numbers) == sequence_length and current_seconds == 0:
        print("Stopping: reached sequence length and full minute")
        break
    
    time.sleep(interval)