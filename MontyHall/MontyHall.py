import random
import matplotlib.pyplot as plt

def sort_prize(n):
    doors = [0]*n
    prize_index = random.randrange(n)
    doors[prize_index] = 1
    return doors, prize_index

def choose_door(n):
    door_index = random.randrange(n)
    return door_index

def open_doors(n, prize_index, selected_door):
    open_doors = []
    for i in range(n):
        if (i != prize_index) and (i != selected_door):
            open_doors.append(i)
    if len(open_doors)> (n-2):
        open_doors.pop(random.randrange(len(open_doors)))
    return open_doors
    
def def_available_doors(n, open_doors):
    available_doors = list(range(n))
    for ele in sorted(open_doors, reverse = True):  
        del available_doors[ele] 
    return available_doors

def switch_door(available_doors, selected_door):
    for i in available_doors:
        if i != selected_door:
            selected_door = i
            break
    return selected_door      

N = 10 #number of samples
n = 3 #number of doors

number_hits = 0 #Number of times a person gets the right door, without trading the door
prize_hits_with_no_change = 0
prize_hits_with_change = 0
loses_with_no_change = 0
loses_with_change = 0

for i in range(N):
    door_list, prize_index = sort_prize(n)

    selected_door = choose_door(n)

    doors_to_open = open_doors(n, prize_index, selected_door)

    available_doors = def_available_doors(n, doors_to_open)

    if prize_index == selected_door:
        prize_hits_with_no_change = prize_hits_with_no_change + 1
    else:
        loses_with_no_change = loses_with_no_change + 1     

    new_door = switch_door(available_doors, selected_door)
    if prize_index == new_door:
        prize_hits_with_change = prize_hits_with_change + 1
    else:
        loses_with_change = loses_with_change + 1

print("Perncentage of hits without changing the door: ", (prize_hits_with_no_change*100/N))
print("Perncentage of hits by changing the door: ", (prize_hits_with_change*100/N))
