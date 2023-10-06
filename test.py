results = []
matrix = [[1,2,3], [4,5,6], [7,8,9]]

for row in matrix:
    for n in row:
        if n % 2 == 0:
            results.append(n)

print(results)

