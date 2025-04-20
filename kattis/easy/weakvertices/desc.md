To solve this problem, I ended up converting the adjacency matrix to an adjaceny list where each element had the set of all neighboring vertices.
Then, in order to find what is weak and whats not, I looped over each vertex, then found the intersection of its own set with the intersection of the set of each neighbor (so the intersection between the current set and the set of each element in the current set)
if the intersection was empty, then they could not be a triangle since a triangle is defined by having two vertices neighbor a third vertex, so if the intersection was empty for each neighbor, then it was a part of no triangle and thus a weak vertex.

Also, I learned the best way to print space separated things is to add them all to a list 'l' then call print(*l)
