import numpy as np

def approx_real_root(coeffs, interval):
    a, b, c, d = coeffs[3], coeffs[2], coeffs[1], coeffs[0]
    
    x1 = np.linspace(interval[0], interval[1], 100)
    delta1 = x1[1] - x1[0]
    y1 = a * x1**3 + b * x1**2 + c * x1 + d
        
    yr1 = np.min(np.abs(y1))
    
    for i in range(100):
        if (abs(y1[i]) == yr1):
            index1 = i
    
    r1 = x1[index1]
    
    for i in range(7):
        x = np.linspace(r1 - delta1, r1 + delta1, 10**(i+1))
        delta = x[1] - x[0]
        y = a * x**3 + b * x**2 + c * x + d
            
        yr = np.min(np.abs(y))
        
        for i in range(10**(i+1)):
            if (abs(y[i]) == yr):
                index = i
        
        r_approx = x[index]
    
    return r_approx

print(approx_real_root((1, -4, 1, 4), (-5, 0)))