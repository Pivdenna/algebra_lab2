import numpy as np

matrix = np.array([[1,2,3],[3,2,1],[1,0,-1]])
print(matrix)
print("")


def eigen():
    evalue, evect = np.linalg.eig(matrix)
    print(evect)
    print("")
    print(evalue)
    return evect, evalue


def check():
    evectors, evalues = eigen()
    u = evectors[:, 1]
    lam = evalues[1]
    first_part = np.dot(matrix, u)
    second_part = np.dot(lam, u)
    print(first_part, second_part)
    return first_part, second_part

check()