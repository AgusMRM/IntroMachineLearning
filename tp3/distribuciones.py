import numpy as np 
import pandas as pd

def diagonal(d,n,C):
    
    center1 = np.ones(d)
    mcov1   = np.eye(d)*(C*np.sqrt(d))**2
    
    center2 = np.ones(d)*-1
    mcov2   = np.eye(d)*(C*np.sqrt(d))**2
    
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
    mcov1   = np.eye(d)*C**2
    
    
    center2 = np.zeros(d)
    center2[0] = -1
    mcov2   = np.eye(d)*C**2
    
    points1 = np.random.multivariate_normal(center1, mcov1, int(n/2))
    points2 = np.random.multivariate_normal(center2, mcov2, int(n/2))
    
    points = np.concatenate([points1,points2])
    df = pd.DataFrame(points)
    
    class1 = np.ones(int(n/2))
    class2 = np.ones(int(n/2))*0
    
    clases = np.concatenate([class1,class2])
    df['clases'] = clases.astype(int)


    return df

def espirales_anidadas(n):

    r2    = np.random.uniform(0, 1, n)
    r = np.sqrt(r2)
    tita = np.random.uniform(-2*np.pi, 4*np.pi, n)
    x = r * np.cos(tita)
    y = r * np.sin(tita)
    
  
    
    sel, = np.where((r > tita/(4*np.pi)) & (r < (tita + np.pi)/(4*np.pi)))
    
    # ---- esto es una chanchada ...
    sel2, = np.where((r > (tita+2*np.pi)/(4*np.pi)) & (r < ((tita+2*np.pi) + np.pi)/(4*np.pi)))
    sel3, = np.where((r > (tita+4*np.pi)/(4*np.pi)) & (r < ((tita+4*np.pi) + np.pi)/(4*np.pi)))
    sel4, = np.where((r > (tita-2*np.pi)/(4*np.pi)) & (r < ((tita-2*np.pi) + np.pi)/(4*np.pi)))
    sel5, = np.where((r > (tita-4*np.pi)/(4*np.pi)) & (r < ((tita-4*np.pi) + np.pi)/(4*np.pi)))
    
    sel = np.concatenate([sel,sel2,sel3,sel4,sel5])
    # ------------------------------
    
    clases = np.ones(n)
    clases[sel] = 0
    
    df = pd.DataFrame({'x' : x, 'y' : y, 'r' : r, 'tita' : tita})
    df['clases'] = clases.astype(int)
    
    return df #x[sel],y[sel]
    
