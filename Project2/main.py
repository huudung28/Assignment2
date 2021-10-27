with open("steps.txt") as f:
    steps_in_356d = [int(e.strip()) for e in f]

months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

k = 0
for i, v in enumerate(months):
    print(f"Month {i + 1}, average: {sum(steps_in_356d[k:k + v]) // v} steps")
    k += v


