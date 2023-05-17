numbers = [10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
target = 35

pairs = []

for x in range(len(numbers)):
    for y in range(x + 1, len(numbers)):
        if numbers[x] + numbers[y] == target:
            pair = (numbers[x], numbers[y])
            reverse_pair = (numbers[y], numbers[x])
            pairs.append(pair)
            pairs.append(reverse_pair)

print(f"Знайдені пари: {pairs}")
