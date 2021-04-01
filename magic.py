n = int(input("Введите число размерности матрицы n x n:\n"))
mat = [[0]*n for i in range(n)]
firstN = 1
m = 0

mat[n//2][n//2]= n * n
for j in range(n // 2):
    #Верхная горизонтальная матрица
    for i in range(n-m):
        mat[j][i + j] = firstN
        firstN += 1

    #Правая вертикальная матрица
    for i in range(j + 1, n - j):
        mat[i][-j - 1] = firstN
        firstN += 1

    #Нижняя горизонтальная матрица
    for i in range(j + 1, n - j):
        mat[-j - 1][-i - 1] = firstN
        firstN += 1

    #Левая вертикальная матрица
    for i in range(j + 1, n - (j + 1)):
        mat[-i-1][j] = firstN
        firstN += 1
    m += 2

for i in mat:
    print(*i)