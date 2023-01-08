f1, f2 = 0, 1
# n-> upper limit of the fibonacci series
n = int(input())
sm = 0
while f2 < n:
    if f2 % 2 == 0:
        sm += f2
    f1, f2 = f2, f1 + f2
print(sm)