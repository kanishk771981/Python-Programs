import time
#function for finding elapsed time

def elapsed_time(start,end):
    start = time.time()
    end = time.time()

    return end - start

#askig user for input
start = input("enter to start time of stopwatch")
end = input("enter to end time of stopwatch")

elapsedtime = elapsed_time(start,end)

print(f"Elapsed time is {elapsedtime} seconds")





