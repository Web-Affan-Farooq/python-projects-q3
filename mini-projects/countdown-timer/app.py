import time
# print(time.asctime()) # shows time in  Wed Apr  2 20:04:46 2025
# print(time.localtime(time.time())) # shows time in time.struct_time(tm_year=2025, tm_mon=4, tm_mday=2, tm_hour=20, tm_min=14, tm_sec=46, tm_wday=2, tm_yday=92, tm_isdst=0)


extime = time.time()
user_time = int(input("Enter time in seconds "))
time_to_reach = extime + user_time # user adds count down of 10 seconds
rng = int(time_to_reach - extime)
while extime < time_to_reach: 
    rng -= 1
    print(rng, end="\r")
    time.sleep(1)
    extime+=1

print("countdown ends ")

# Easy countdown logic _______
# extime = 60 
# time_to_reach = extime+ 20 # user adds count down of 10 seconds
# rng = time_to_reach - extime
# while extime < time_to_reach: 
#     rng -= 1
#     print(rng, end="\r")
#     time.sleep(1)
#     extime+=1

# print("countdown ends ")