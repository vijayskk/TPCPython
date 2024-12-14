from prob import generate_combinations

n = int(input())
k = int(input())
times = 0

arrays = generate_combinations(n,k)

print(arrays)
print(f"Total arrays: {len(arrays)}")
