### Problem statement ###

If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.<br>
Find the sum of all the multiples of 3 or 5 below 1000.


### Approach 1 ###
We will iterate over all the numbers from 1 to 999 and check if they are divisible by 3 or 5. If they are, we will add them to the sum.

### Approach 2 ###
### Arithmetic Progression ###
We can first find the sum of all multiples of 3, 5 and 15 till the number we want to check for and then add the sum of all multiples of 3 and 5 and subtract the sum of all multiples of 15. This is because the sum of all multiples of 15 will be added twice in the sum of all multiples of 3 and 5.