maxV = {
    "r": 12,
    "g": 13,
    "b": 14
}

def possible(l):
    for w in l.split(","):
        count, color = w.strip().split(" ")
        count = int(count)
        if count > maxV[color[0]]:
            return False
    return True

sum_val = 0

file_path = "day2.input"  

with open(file_path, 'r') as file:
    for line in file:
        line = line.strip()
        if not line:
            continue  
        game, x = line.split(':')
        game = int(game[5:])
        result = all([possible(k.strip()) for k in x.split(";")])
        sum_val += game if result else 0

print(sum_val)



