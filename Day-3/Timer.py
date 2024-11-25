import time

my_time = int(input("Enter the time in Seconds: "))

for i in range(my_time, 0, -1):
    print(i)
    time.sleep(1)
print("Time is UP!!!")    