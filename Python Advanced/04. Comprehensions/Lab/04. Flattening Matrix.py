n = int(input())
matrix = [[int(x) for x in input().split(", ")] for _ in range(n)]

flatten = [x for row in matrix for x in row]
print(flatten)