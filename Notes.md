# Notes

## Map
```python
l,b = map(int,input().split())
# Input : 5 4
# l = 5 , b = 4
```
## Questions
find multiples of 3,5 from 1,N
```python
print(n//3 + n//5 - n//15)
```

traingle validation problem
```python
A,B,C = map(int, input().split())
if A+B>C and B+C>A and A+C>B:
    print("Yes")
else:
    print("No")
```

missing number problem 
```python
n = 100
inp = list(map(int,input().split()))
actualsum = n*(n+1)/2
summ = sum(inp)

print(actualsum-summ)
```
cheff pass of fail question 
```python
T = int(input())

for i in range(T):
    N,X,P = list(map(int,input().split()))
    if X*3+(N-X)*-1 >= P:
        print("PASS")
    else:
        print("FAIL")
```
```Output:
3
5 2 3
PASS
5 2 4
FAIL
4 0 0
FAIL
```

N children k apple problem 
```python
n,k = list(map(int,input().split()))
print(k%n)
# OUT:
# 3 14
# 2
```
pizza splitting problem 
```python
from math import ceil
T = int(input())

for i in range(T):
    N,X = map(int,input().split())
    print(ceil((N*X)/4))
```

chef and candies problem 
```python
# cook your dish here
from math import ceil
T = int(input())

for i in range(T):
    N,X = map(int,input().split())
    needed_candies = N-X
    if needed_candies <1:
        print(0)
    else:
        print(ceil(needed_candies/4))
```
## Libraries
- Third party libraries
    - numpy
    - kiwi

? Sam is having 75 candies. He is giving half to his friend angel. Since angel loves sam a lot, She gives back half. WAP to find how much sam holds and angel holds  
Soln:
```python
N = int(input())
print(N - N/4,N/4)
```
?Task
Given an integer, , perform the following conditional actions:
If  is odd, print Weird
If  is even and in the inclusive range of  to , print Not Weird
If  is even and in the inclusive range of  to , print Weird
If  is even and greater than , print Not Weird
Input Format
A single line containing a positive integer, .
Constraints

Output Format
Print Weird if the number is weird. Otherwise, print Not Weird.
Soln:
```python
n = int(input())

if (n%2==0 and n>=2 and n<=5) or (n%2==0 and n>20):
    print("Not weird")
else:
    print("Wierd")
```
? I decided to go to a temple and give offering to god. I decided to offer lemons to goddess. There are three goddes in that temple. Constraint is only 7 lemons has to be offered to eah goddess. Take number of lemons hand from the user as input. 
Soln:
```python
def offerGod(N):
    ins = 21-N
    for i in range(1,4):
        if N>7:
            print(f"God{i}: offered 7")
            N=N-7
        elif N>=1 and N<7:
            print(f"God{i}: Can offer {N} want {7-N}")
            N=0
        else:
            print(f"God{i}: want 7")
            # ins = 21
    if N>0:
        print(f"Surplus: {N}")
    else:
        print(f"Insufficient {ins}")

    print("God Bless You")
N = int(input())
if N<=0:
    N=0
offerGod(N)
```