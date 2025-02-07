import numpy as np;

array = np.random.randint(1, 100, (5, 5));  
print("Matrix:\n", array);

row_wise_sums = np.sum(array, axis=1);  
print("Row-wise sums:", row_wise_sums);
