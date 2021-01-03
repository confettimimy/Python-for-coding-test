result = []

for _ in range(10):
    n = int(input())
    result.append(n % 42)

result = list(set(result))

print(len(result))
