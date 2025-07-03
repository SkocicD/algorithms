This was a brute force problem where you had to realize that there are 384 ways that this deck could be sorted 
(4! for order of suits and 2^4 for combinations of reverse suits), and that the deck is only 52 cards so it wouldnt take long
to count the number of required moves to sort. The final thing was finding how many moves it would take to sort a list using the
longest increasing subsequence (so like [1,2,7,4,3] would have [1,2,3] as its longest subsequence. The number of moves is then
the length of the list (5 here) minus the length of the subsequence (3 here) so in this case it would take 2 moves. You then 
just had to calculate this for every possible way to sort and take a minimum
