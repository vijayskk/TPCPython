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
### ?
While playing an RPG game, you were assigned to complete one of the hardest quests in this game.
There are n monsters you'll need to defeat in this quest. Each monster i is described with two integer
numbers - poweri and bonusi. To defeat this monster, you'll need at least poweri experience points. If
you try fighting this monster without having enough experience points, you lose immediately. You will
also gain bonusi experience points if you defeat this monster. You can defeat monsters in any order.
The quest turned out to be very hard - you try to defeat the monsters but keep losing repeatedly. Your
friend told you that this quest is impossible to complete. Knowing that, you're interested, what is the
maximum possible number of monsters you can defeat? (Question difficulty level: Hardest)
Input:
The first line contains an integer, n, denoting the number of monsters.
The next line contains an integer, e, denoting your initial experience.
Each line i of the n subsequent lines (where 0 ≤ i < n) contains an integer, poweri, which represents
power of the corresponding monster.
Each line i of the n subsequent lines (where 0 ≤ i < n) contains an integer, bonusi, which represents
bonus for defeating the corresponding monster.
soln:
```python
times = 0
n = int(input())
e = int(input())
powers = []
bonuses = []
for i in range(n):
    powers.append(int(input()))

for j in range(n):
    bonuses.append(int(input()))

for j in range(n):
    for i in range(0,n-j-1):
        if powers[i]>powers[i+1]:
            powers[i],powers[i+1] = powers[i+1],powers[i]
            bonuses[i],bonuses[i+1] = bonuses[i+1],bonuses[i]

for i in range(n):
    if e >= powers[i] and bonuses[i]>=0:
        e+=bonuses[i]
        times+=1
        

for j in range(n):
    for i in range(0,n-j-1):
        if bonuses[i]<bonuses[i+1]:
            powers[i],powers[i+1] = powers[i+1],powers[i]
            bonuses[i],bonuses[i+1] = bonuses[i+1],bonuses[i]

for i in range(n):
    if e >= powers[i] and bonuses[i]<0:
        e+=bonuses[i]
        times+=1
print(times)
```

## Modules in python
in calcmodule.py:
```python
def calc(a,b,c):
    return a+b+c
```
in main.py:
```python
from calcmodule import calc
print(calc(10,10,10))
```

## Roadmaps
- linkedlist
- stack
- queue
- trees 
- hashing and hashmap
- graph
- dynamic programming 
- note: Hashmap , backtracking , important algorithms

