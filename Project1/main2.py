with open("video_running_times.txt", "r") as f:
    running_times = [float(e) for e in f]

print("Running times:")

for i, v in enumerate(running_times, start=1):
    print(f"Video {i}: {v} second(s)")

print(f"The total running time of all the segments: {sum(running_times)} seconds")
