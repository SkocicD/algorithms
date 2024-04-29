This algorithm is a divide and conquer way to find the largest and the smallest value from a list.

the idea is to cut the list in half, find the largest and smallest from that list and return it in a tuple (done recursively)

The runtime of this algorithm is the same as the brute force version. Proven in CIS 390 Homework for the chapter on divide and conquer

    C(n) = 2n - 2

where n is the number of elements in the list.
