import numpy as np

a=np.array([1,2,3,4,5])

print(a)

print(a.shape)

b=np.array([[1,2,3],[4,5,6],[7,8,9]])
print(b)

print(b.shape)
print(b[0,2])

c=np.zeros((2,2))
print(c)

d=np.ones((1,1))
print(d)

e=np.random.random((2,2))
print(e)


row1=b[1,:]
row2=b[1:3,:]

print(row1)
print(row2)

col1=b[:,1]
col2=b[:,1:2]

print(col1)
print(col2)

bol=(b>2)
print(bol)

print(np.sqrt(b))