import math

file_path = "day6.input"  

with open(file_path, 'r') as file:
    lines = [l.split(":")[1].strip() for l in file]

time = [int(x) for x in lines[0].split()]
distance = [int(x) for x in lines[1].split()]

result = 1
for i in range(len(time)):
    b = time[i]
    c = distance[i]

    delta = b*b - 4*c

    if delta < 0:
        print(f"No real solutions for equation {i+1}")
        continue

    delta_sqrt = math.sqrt(delta)

    minR = math.floor((b - delta_sqrt) / 2 + 1)
    maxR = math.ceil((b + delta_sqrt) / 2 - 1)
    diff = maxR - minR + 1
    result = result * diff

print(result)
