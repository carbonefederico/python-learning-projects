import time

timer = int(input("Input the timer in seconds: "))

for i in range (0,timer):
    print (f"Time remaining: {timer - i} seconds")
    time.sleep(1)
    

print ("Time's up")