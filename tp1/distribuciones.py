import numpy as np 
import pandas as pd

def diagonal(d,n,C):
    
    center1 = np.ones(d)
    mcov1   = np.eye(d)*C*np.sqrt(d)
    
    center2 = np.ones(d)*-1
    mcov2   = np.eye(d)*C*np.sqrt(d)
    
    points1 = np.random.multivariate_normal(center1, mcov1, int(n/2))
    points2 = np.random.multivariate_normal(center2, mcov2, int(n/2))
    
    class1 = np.ones(int(n/2))
    class2 = np.ones(int(n/2))*0
    
    clases = np.concatenate([class1,class2])
    
    points = np.concatenate([points1,points2])
    df = pd.DataFrame(points)
    
    df['clases'] = clases.astype(int)

    return df

def paralelo(d,n,C):
    
    center1 = np.zeros(d)
    center1[0] = 1
    mcov1   = np.eye(d)*C
    
    
    center2 = np.zeros(d)
    center2[0] = -1
    mcov2   = np.eye(d)*C
    
    points1 = np.random.multivariate_normal(center1, mcov1, int(n/2))
    points2 = np.random.multivariate_normal(center2, mcov2, int(n/2))
    
    points = np.concatenate([points1,points2])
    df = pd.DataFrame(points)
    
    class1 = np.ones(int(n/2))
    class2 = np.ones(int(n/2))*0
    
    clases = np.concatenate([class1,class2])
    df['clases'] = clases.astype(int)


    return df
    
