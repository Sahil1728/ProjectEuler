# n-> number till which we have to find the sum of multiples of 3 and 5, n is included
n = int(input())
# sum of multiples of 3
threes = (n//3)*(2*3+(n//3-1)*3)//2
# sum of multiples of 5
fives = (n//5)*(2*5+(n//5-1)*5)//2
# sum of multiples of 15
fifteens = (n//15)*(2*15+(n//15-1)*15)//2
# sum of multiples of 3 and 5
print(threes+fives-fifteens)