import numpy as np
import matplotlib.pyplot as plt

def column_range_plot(A, filename="column_ranges.pdf"):
    
    column_ranges = np.zeros(A.shape[1])
    
    for i in range(A.shape[1]):
        column_ranges[i] = np.max(A[:, i]) - np.min(A[:, i])
    
    plt.bar(range(A.shape[1]), column_ranges)
    plt.savefig(filename)
    plt.show()
    
    return column_ranges
    
A = np.array([[1., 4., 9.],
              [3., 1., 5.],
              [7., 2., 8.]])

column_range_plot(A)
