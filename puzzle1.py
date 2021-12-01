with open("input_files/puzzle1input.txt", "r") as f:
    data = [int(line.strip()) for line in f.readlines()]

increases = 0

for i in range(len(data) - 1):
    if data[i] < data[i + 1]:
        increases += 1

print(increases)

increased_windows = 0

for i in range(len(data) - 2):
    if sum(data[i:i + 3]) < sum(data[i + 1:i + 4]):
        increased_windows += 1

print(increased_windows)
