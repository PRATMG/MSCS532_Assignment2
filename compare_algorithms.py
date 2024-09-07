import time
import random
import tracemalloc
from merge_sort import merge_sort
from quick_sort import quick_sort

# Testing datasets
sorted_data = list(range(10000))
reversed_sorted_data = list(range(10000, 0, -1))
random_data = random.sample(range(10000), 10000)

#Function for measuring time and memory
def memory_test(func, data):
    tracemalloc.start()
    start_time = time.time()
    func(data)
    execution_time = time.time() - start_time
    current, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    return execution_time, peak / 10**6 #converting memory to MB

#testing merge sort
print("Merge Sort Resut: ")
for data, name in zip([sorted_data, reversed_sorted_data, random_data], ["Sorted", "Reverse Sorted", "Random"]):
    time_taken, mem_used = memory_test(merge_sort, data[:])
    print(f"{name}: Time = {time_taken: .6f} sec, Peak Memory = {mem_used:.2f} MB")

#testing quick sort
print("\nQuick Sort Results: ")
for data, name in zip([sorted_data, reversed_sorted_data, random_data], ["Sorted", "Reverse Sorted", "Random"]):
    time_taken, mem_used = memory_test(quick_sort, data[:])
    print(f"{name}: Time = {time_taken: .6f} sec, Peak Memory = {mem_used: .2f} MB")