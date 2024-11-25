import time

my_time = int(input("Enter the time in Seconds: "))

for i in range(my_time, 0, -1):
    
    seconds = i % 60
    minutes = int(i/60) % 60 
    hours = int(i/3600) % 24
    
    print(f"{hours:02}:{minutes:02}:{seconds}")
    time.sleep(1)
print("Time is UP!!!")    