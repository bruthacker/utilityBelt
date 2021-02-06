import re
path = r'C:\Users\eric\Desktop\CTF\test.2'
invalid_chars = ["ste", "ets", "tev", "vet", "eve", "557", "775", "ve5", "5ev", "55e", "e55"]

with open(path, 'r') as file:
    for line in file:
        if any(substring in line for substring in invalid_chars):
            #print("jackpot %s " % line)
            continue
        else:
            if len(re.findall(r'\d+', line)) > 2:
                print(line)

