location_x = 0
location_y = 0
aim = 0


with open("input_files/puzzle2input.txt", "r") as file:
    for line in file:
        command = line.strip().split()
        direction = command[0]
        distance = int(command[1])
        if direction == "forward":
            location_x += distance
            location_y += (distance * aim)
        elif direction == "up":
            aim -= distance
        elif direction == "down":
            aim += distance

print(location_x * location_y)
