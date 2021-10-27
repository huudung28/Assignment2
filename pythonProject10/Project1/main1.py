videos = int(input("Enter the number of videos: "))

running_times = []

for i in range(videos):
    video_time = float(input(f"Enter the running time (in seconds) of video {i + 1}: "))

    running_times.append(video_time)


with open("video_running_times.txt", "a+") as f:
    text = "\n".join(str(e) for e in running_times)
    f.write(text + "\n")
