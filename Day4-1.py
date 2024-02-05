sum_val = 0
file_path = "day4.input"  
with open(file_path, 'r') as file:
    for line in file:
        cards = line.strip().split(": ")[1].split(" | ")
        win = set(cards[0].split(" "))
        if '' in win:
            win.remove('')
        mine = set(cards[1].split(" "))
        points = len(win.intersection(mine)) - 1
        sum_val += 2 ** points if points >= 0 else 0

print(sum_val)
