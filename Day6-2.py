import math
file_path = "day6.input"  
with open(file_path, 'r') as file:
    lines = [l.split(":")[1].strip() for l in file]

time = [int(lines[0].replace(" ", ""))]
distance = [int(lines[1].replace(" ", ""))]

result = 1

for i in range(len(time)):
    b = time[i]
    c = distance[i]

    delta = math.sqrt(b*b - 4*c)

    minR = math.floor(((b - delta) / 2) + 1)
    maxR = math.ceil(((b + delta) / 2) - 1)
    diff = maxR - minR + 1
    result = result * diff

print(result)
