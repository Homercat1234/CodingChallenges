#A solution to the 100 doors problem

doors = [0] * 100
    
def toggle(n):
    if(n == 101):
        return
    for i in range(100):
        if (i + 1) % n == 0:
            doors[i] = 0 if doors[i] else 1
    toggle(n + 1)
    
toggle(1)

[print('' if door == 0 else index + 1, end=' ' if door == 1 else '') for index, door in enumerate(doors)]