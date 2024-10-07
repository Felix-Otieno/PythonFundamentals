import time

# Get the current time in seconds since epoch
currentTime = time.time()

# Convert to integer to get total seconds
totalSecond = int(currentTime)

# Get the current second
currentSecond = totalSecond % 60

# Convert total seconds to total minutes
totalMinute = totalSecond // 60

# Get the current minute
currentMinute = totalMinute % 60

# Convert total minutes to total hours
totalHour = totalMinute // 60

# Get the current hour (in 24-hour format)
currentHour = totalHour % 24

# Print the current time in GMT
print("Current time is", currentHour, ":", currentMinute, ":", currentSecond, "GMT")
