import numpy as np;

array = np.random.rand(100);
min_val = np.min(array);
max_val = np.max(array);

normalized_array = (array - min_val) / (max_val - min_val);
print(normalized_array);
