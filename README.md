# MSCS532_Assignment2
### Overview
This repository contains Python implementations of two classic divide-and-conquer algorithms: Merge Sort and Quick Sort. The algorithms are compared based on their performance on various datasets (sorted, reverse sorted, and random data).

### Algorithms Implemented
1. Merge Sort
    Time Complexity: Best, Average, and Worst Case: O(n log n)
    Space Complexity: O(n)
Merge Sort is a stable, divide-and-conquer algorithm that recursively divides the array into halves, sorts them, and merges the sorted halves.

2. Quick Sort
    Time Complexity:
        Best and Average Case: O(nlogn)
        Worst Case: O(n^2) (if the pivot is poorly chosen)
    Space Complexity: O(logn)

Quick Sort is an in-place sorting algorithm that selects a pivot, partitions the array into subarrays, and recursively sorts the subarrays. The performance of Quick Sort is heavily influenced by the pivot selection method.

### Datasets Used for Testing
1. Sorted data, Reverse sorted data, and Random data.

### Performance Metrics
Merge Sort
Dataset       | Time (sec)|	Peak Memory (MB)|
------------- | --------- |  ---------------|
Sorted        |	  0.276525|	            0.16|
Reverse Sorted|	  0.257001|	            0.16|
Random	      |   0.278727|	            0.16|

Quick Sort
Dataset        | time (sec)| Peak Memory (MB)|
-------------- |  --------- |--------------- |
Sorted         |   0.142253 |	        0.25 |
Reverse Sorted |	0.093818|	         0.25|
Random	       |    0.117909|	         0.32|

### Observations
1. Quick Sort outperformed Merge Sort in terms of execution time on all datasets, particularly on sorted and reverse sorted data.

2. Merge Sort exhibited consistent performance across all datasets, adhering to its theoretical time complexity of 
O(nlogn).

3. Memory usage for Quick Sort was higher on random data compared to sorted and reverse sorted datasets, potentially due to deeper recursion.

### Conclusion
    Quick Sort is more efficient for random datasets and performs well even on sorted datasets, suggesting the use of a randomized or middle-element pivot selection strategy.

    Merge Sort, while stable in its time complexity, uses more memory due to the additional space required for merging.

Overall, both algorithms exhibit their theoretical behaviors, with Quick Sort being more efficient in practice for most datasets.