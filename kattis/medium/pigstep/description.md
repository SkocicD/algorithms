this problem was a binary search problem

To figure it out I broke I started at looking how I would do a binary search for a single response, figuring out how the range should shift around. After, I added the other response in and saw that if they are the same, you can obviously do the same thing as a binary search for a single one, and if one was greater than the other, you could get just as much information by taking the smart half of the range. If you always kept the rightmost minimum of the leftmost range and vice versa to create your range, you can independently do binary searches for each