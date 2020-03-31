# Program to multiply two matrices using nested loops
import random
import time
import numpy as np

start = time.clock()

N = 250
# NxN matrix
X = []
Y = []

# NxN matrix
X = []
for i in range(N):
    X.append([random.randint(0,100) for r in range(N)])

# Nx(N+1) matrix
Y = []
for i in range(N):
    Y.append([random.randint(0,100) for r in range(N+1)])

result1 =[]

for row in X:
	result1.append([sum(row*col for row, col in zip(row,col)) for col in zip(*Y)])

time_new = time.clock()-start

print 'New version took: {0}'.format(time_new)

start_old = time.clock()

X = []
for i in range(N):
    X.append([random.randint(0,100) for r in range(N)])

# Nx(N+1) matrix
Y = []
for i in range(N):
    Y.append([random.randint(0,100) for r in range(N+1)])


# result is Nx(N+1)
result = []
for i in range(N):
    result.append([0] * (N+1))

# iterate through rows of X
for i in range(len(X)):
    # iterate through columns of Y
    for j in range(len(Y[0])):
        # iterate through rows of Y
        for k in range(len(Y)):
            result[i][j] += X[i][k] * Y[k][j]


time_old = time.clock()-start_old

print 'Old version took: {0}'.format(time_old)
print 'This many times faster: {0}'.format(time_old/time_new)



## Checking the outputs are equal:

print 'Running both versions again to check if the outputs are equal given same inputs...'

N = 250
# NxN matrix
X = []
Y = []

# NxN matrix
X = []
for i in range(N):
    X.append([random.randint(0,100) for r in range(N)])

# Nx(N+1) matrix
Y = []
for i in range(N):
    Y.append([random.randint(0,100) for r in range(N+1)])

result1 =[]

for row in X:
	result1.append([sum(row*col for row, col in zip(row,col)) for col in zip(*Y)])

time_new = time.clock()-start

# result is Nx(N+1)
result = []
for i in range(N):
    result.append([0] * (N+1))

# iterate through rows of X
for i in range(len(X)):
    # iterate through columns of Y
    for j in range(len(Y[0])):
        # iterate through rows of Y
        for k in range(len(Y)):
            result[i][j] += X[i][k] * Y[k][j]


time_old = time.clock()-start_old

print result1==result





