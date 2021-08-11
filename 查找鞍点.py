
def jvzhen(matrix):
    rowmins = []
    rowmaxs = []
    colmins = []
    colmaxs = []

    for i, row in enumerate(matrix):
        m = min(row)
        M = max(row)
        for j, x in enumerate(row):
            if x == m:
                rowmins.append((i, j))
            if x == M:
                rowmaxs.append((i, j))

    t = [list(i) for i in zip(*matrix)]

    for j, col in enumerate(t):
        m = min(col)
        M = max(col)
        for i,x in enumerate(col):
            if x == m:
                colmins.append((i, j))
            if x == M:
                colmaxs.append((i, j))

    return (set(rowmins) & set(colmaxs)) | (set(rowmaxs) & set(colmins))

M = [
    [10, 14, 9, 15],
    [7, 4, 8, 10],
    [6, 8, 4, 9],
    [8, 51, 10, 23]
]

print(jvzhen(M))

