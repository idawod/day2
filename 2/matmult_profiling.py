# Program to multiply two matrices using nested loops
import random
import multiprocessing

multiprocessing.cpu_count()

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
@profile
def createResult(N):
	result = []
	for i in range(N):
	    result.append([0] * (N+1))
	return result


# iterate through rows of X
@profile
def matrix(result, X, Y, N):
	#result = []
	#for i in range(N):
	 #   result.append([0] * (N+1))
	for i in range(len(X)):
	    # iterate through columns of Y
	    for j in range(len(Y[0])):
		# iterate through rows of Y
		for k in range(len(Y)):
		    result[i][j] += X[i][k] * Y[k][j]
	return result

#createResult(N)
result = matrix(createResult(N),xfunc(N),yfunc(N), N)

for r in result:
    print(r)



# line by line profiling kernprof -l -v matmult.py	
# line by line memory profiling python -m memory_profiler matmult.py
