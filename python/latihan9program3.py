import os
os.system('cls')

baris = int(input("user input : "))

def segitiga(n):
  if n == 1:
    return [1]
  else:
    line = [1]
    previous_line = segitiga(n-1)
    for i in range(len(previous_line)-1):
      line.append(previous_line[i] + previous_line[i+1])
    line += [1]
  return line

for i in range(baris):
  print(segitiga(i+1))