import numpy as np
import matplotlib.pyplot as plt

def detect_turning_points(signal, filename="turning_points.pdf"):
    
    n = signal.size
    
    indices_signal_changes = []
    
    if signal[0] < signal[1]:
        signal_rising = True
    else:
        signal_rising = False
    
    for i in range(1, n-1):
        
        if (signal[i] < signal[i + 1]) != signal_rising:
            indices_signal_changes.append(i)
            signal_rising = not signal_rising
    
    indices = np.array(indices_signal_changes)
    
    marked_values = np.zeros(indices.shape)
    
    for i in range(indices.size):
        marked_values[i] = signal[indices[i]]
    
    plt.plot(signal)
    plt.scatter(range(1, indices.size + 1), marked_values, marker='+', color='red')
    
    plt.savefig(filename)
    plt.show()
    
    return indices
    

detect_turning_points(np.array([1, 4, 2, 5, 3, 6]))
    
