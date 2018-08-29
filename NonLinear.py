import numpy as np
from numpy.linalg import pinv
import scipy
import random 

def f(x1,x2):
    return np.sign((x1**2) + (x2**2) - 0.6)

def transform(p):
    return ([1,p[1],p[2],p[1]*p[2],p[1]**2,p[2]**2,p[3]])

def transpoints(points):
    res = []
    for i in points : 
        res.append(transform(i))
    return res

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

def Error(w,actual):
    count = 0
    n = len(actual[0])
    index = n - 1
    for i in actual : 
        if(np.dot(w,i[:index]) != i[index]):
            count = count + 1
    return count

def function8():
    ans = []
    for trial in range(1000):
        sample = []
        for i in range(1000):
            x = random.uniform(-1.0,1.0)
            y = random.uniform(-1.0,1.0)
            points = []
            points.append([1,x,y,f(x,y)])
        count = 0
        random.shuffle(points)
        for p in points:
            if(count < 1000):
                p[3] = p[3] * (-1)
            sample.append(p)
            count = count + 1
        w = Linear_Regression(sample)
        ans.append(Error(w,sample))
    print(np.mean(ans))

def function9():
    ans = []
    hyp = {
        'a': [-1.0, -.05, .08, .13, 1.5, 1.5],
        'b': [-1.0, -.05, .08, .13, 1.5, 15.0],
        'c': [-1.0, -.05, .08, .13, 15.0, 1.5],
        'd': [-1.0, -1.5, .08, .13, .05, .05],
        'e': [-1.0, -.05, .08, 1.5, .15, .15]
        }
    for trial in range(1000):
        sample = []
        for i in range(1000):
            x = random.uniform(-1.0,1.0)
            y = random.uniform(-1.0,1.0)
            points = []
            points.append([1,x,y,f(x,y)])
        count = 0
        random.shuffle(points)
        for p in points:
            if(count < 1000):
                p[3] = p[3] * (-1)
            sample.append(p)
            count = count + 1
        sample = transpoints(sample)
        w = Linear_Regression(sample)
        for key, value in hyp.items():
            count = 0
            for point in points:
                if(np.sign(np.dot(w,point[:6])) != np.sign(np.dot(value, point[:6]))):
                    count = count + 1
            print(key +" : " + str(1 - count/float(len(sample)))

function8()
function9()
