import numpy as np
from numpy.linalg import pinv
import scipy
import random 

def Linear_Regression(p):
    x = []
    y = []
    n = len(p[0])
    index = n - 1 
    for point in p:
        x.append(np.array(point[:index]))
        y.append(point[index])
    x = np.array(x)
    y = np.array(y)
    xinv = pinv(x)
    return np.dot(xinv, y)

def f(x1,y1,x2,y2):
	m = (y2 - y2) / (x2 - x1)
	b = y1 - (m * x1)
	return m,b

def Error(train,actual):
	count = 0
	n = len(actual[0])
	index = n - 1
	for i in actual : 
		if(np.dot(train,i[:index]) != i[index]):
			count = count + 1
	return count

def function5():
	ein = []
	for trial in range(1000):
		x1 = random.uniform(-1.0,1.0)
		x2 = random.uniform(-1.0,1.0)
		y1 = random.uniform(-1.0,1.0)
		y2 = random.uniform(-1.0,1.0)
		points = []
		for i in range(100):
			t = 1
			x = random.uniform(-1.0,1.0)
			y = random.uniform(-1.0,1.0)
			m , b = f(x1,y1,x2,y2)
			p = (m * x) + b
			if(y >= p):
				t = 1
			else:
				t = -1
			points.append([1,x1,y1,x2,y2,t])
		ein.append((Error(Linear_Regression(points),points))/1000)
	print(np.mean(ein))

def function6():
	eout = []
	count = 0
	for trial in range(1000):
		x1 = random.uniform(-1.0,1.0)
		x2 = random.uniform(-1.0,1.0)
		y1 = random.uniform(-1.0,1.0)
		y2 = random.uniform(-1.0,1.0)
		points = []
		for i in range(1000):
			t = 1
			x = random.uniform(-1.0,1.0)
			y = random.uniform(-1.0,1.0)
			m , b = f(x1,y1,x2,y2)
			p = (m * x) + b
			if(y >= p):
				t = 1
			else:
				t = -1
			points.append([1,x1,y1,x2,y2,t])
		
		w = Linear_Regression(points)
		for i in range(1000):
			p = [1,random.uniform(-1.0,1.0),random.uniform(-1.0,1.0)]
			m , b = f(x1,y1,x2,y2)
			ycord = (m * p[1]) + b
			if(p[2] >= ycord):					
				t = 1
			else:
				t = -1
			if((!np.sign(np.dot(w,p)) and t <= 0) or (np.sign(np.dot(w,p)) and t > 0))
				count = count + 1
		eout.append(float(count/1000))		
	print(np.mean(eout))
		
function5()
function6()