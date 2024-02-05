def possible(l):
    maxV = {
        "r": 0,
        "g": 0,
        "b": 0
    }
    for w in l.split(","):
        count, color = w.strip().split(" ")
        count = int(count)
        color = color[0]
        maxV[color] = max(maxV[color], count)
    return maxV

sum_val = 0

file_path = "day2.input"

with open(file_path, 'r') as file:
    for line in file:
        line = line.strip()
        if not line:
            continue  
        game, x = line.split(':')
        game = int(game[5:])
        result = [possible(k.strip()) for k in x.split(";")]
        r = g = b = 0
        for i in result:
            r = max(r, i['r'])
            g = max(g, i['g'])
            b = max(b, i['b'])
        sum_val += (r * g * b)

print(sum_val)
