times = 0
n = int(input())
e = int(input())
powers = []
bonuses = []
for i in range(n):
    powers.append(int(input()))

for j in range(n):
    bonuses.append(int(input()))

for i in range(n-1):
    for j in range(n-1):
        if powers[i]>powers[i+1]:
            powers[i],powers[i+1] = powers[i+1],powers[i]
            bonuses[i],bonuses[i+1] = bonuses[i+1],bonuses[i]
print(powers,bonuses)

for i in range(n):
    if e >= powers[i]:
        e+=bonuses[i]
        times+=1
    else:
        break

print(times)
# 4
# 50
# 20
# 100
# 20
# -150
# 20
# -200
# 10
# -60

# 3