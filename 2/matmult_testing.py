# Program to multiply two matrices using nested loops
import random
import multiprocessing

numProc = multiprocessing.cpu_count()
pool = Pool(processes=numProc)              # start 4 worker processes

N = 50

# NxN matrix

@profile
def xfunc(N):
	X = []
	for i in range(N):
	    X.append([random.randint(0,100) for r in range(N)])
	return X

# Nx(N+1) matrix
@profile
def yfunc(N):
	Y = []
	for i in range(N):
	    Y.append([random.randint(0,100) for r in range(N+1)])
	return Y

# result is Nx(N+1)

def createResult(N):
	result = []
	for i in range(N):
	    result.append([0] * (N+1))

def multiply():

	for k in range(len(Y)):
	    result[i][j] += X[i][k] * Y[k][j]


# iterate through rows of X
@profile
def matrix(X, Y, N):
	result = []
	for i in range(N):
	    result.append([0] * (N+1))
	for i in range(len(X)):
	    # iterate through columns of Y
	         # runs in *only* one process

	    for j in range(len(Y[0])):
		# iterate through rows of Y
 		for num in numProc:
  		    res = pool.apply_async(f, (20,))

		for k in range(len(Y)):
		    result[i][j] += X[i][k] * Y[k][j]

	return result

#createResult(N)
result = matrix(xfunc(N),yfunc(N), N)

for r in result:
    print(r)
