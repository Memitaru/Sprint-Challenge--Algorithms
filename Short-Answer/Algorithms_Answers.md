#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a) This block would be O(n). The number of times it is run will increase linearally with the size of n.


b) This block will be O(n^2). The block inside of the loops is O(1). Both loops would be O(n) which makes the total runtime of the block O(n^2)


c) This block would be O(n). Since it is only recursing once and decrimenting n by 1 each time the runtime increases linerally with the size of n.

## Exercise II

Find the middle floor and drop an egg.

Top floor is n
Bottom floor is 0

If this egg breaks, set this as the temporary top floor.
If this egg does not break, set this as the temporary bottom floor.

If temp top floor - top bottom floor is 1, return the temp top floor as the first floor an egg breaks

If it doesn't equal one, find the halfway point between temp top floor and temp bottom floor and repeat until it does equal 1.
        
The runtime complexity would be O(log(n)) because we are splitting the amount of values to search through each time using a binary search.