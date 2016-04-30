#work with my partner Yitian Zhang


Description of my implementation for flood.py: 
let the function go through flooded_list and determine whether or not the tile in the current index have adjacent tiles which share same color with flooded_list and the color be chosen by player. Then, if the adjacent tile is not out of bounds, add the coordinates of the tile into flooded_list.


Answer for analysis question: Function f(n)=nlgn or the positive side of f(n)=n^2 roughly fit the graph of execution time.


Does the graph look like you expected?
Yes, i suppose that as time increased, the program would go through more data than previous step in loop.


What is the rate of growth of the execution time?
We think the rate is not stable.


What parts of your algorithm do you think are contributing the most to the execution time?The ‘if’ statement