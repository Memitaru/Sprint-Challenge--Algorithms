#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a) O(n) runtime will grow in a linear fashion with n


b) The outer loop will run n times. Inside of the while loop j is increasing each iteration. The while loop is O(log n).

Multiply those together because they are nested loops and it will be O(n log n)


c) Runtime goes up in a linear fashion with n. O(n)

## Exercise II

Go to the middle floor and drop an egg

If the egg breaks:
    Go down one floor and drop an egg
        If it doesn't break then the floor above you is floor f

        If it breaks then this floor now becomes the temporary top floor. Find the middle point between the current top floor and bottom floor to repeat.

If the egg doesn't break:
    Go up one floor and drop an egg
        If it breaks then you are on floor f

        If it doesn't break then this floor now becomes the temporary bottom floor. Find the middle point between the current top and bottom floors and repeat.

The runtime would be O(log n) because you're going to be cutting the number of remaining options in half each time.