# C343Fall2015

partner: Yitian Zhang(username: yitizhan)

We create a table which is a dictionary to store the coordinates and value. I added the coordinates of
sides first because they are constant. Then, I compare the (i,i) with (i-1,j), (i-1, j-1), (i,j-1) to get the value of (i,i). After that, we get the whole table. Then, we traceback from the very last coordinates with the surrounding coordinates(just the reverse procedure), if they have same value,
then add character or gap depends on the position of the coordinates. Finally, we can get the actual sequences.
