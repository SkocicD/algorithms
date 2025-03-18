Tags: Binary Search, Root Finding

This problem used the fact that the function f(x) = xcosh(1/x)-x is always decresing and approaches inf as x->0 from the right

This means that there is always a root between a small enough A and a large enough B for A,B in (0,inf)

As a result, you can do a binary search to find this root for a small enough tolerance
