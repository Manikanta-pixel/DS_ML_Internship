import numpy as np
stdl = ([[78,51,67],[98,98,56],[65,85,55],[60,56,76],[93,62,73]])

stdl_avg = np.mean(stdl, axis = 0)
print(stdl_avg)
sml = stdl-stdl_avg
print(stdl)
print(sml)


#task 2

rs = np.arange(24)
print(rs)
rs.reshape(4,3,2)
rs.reshape(4,2,3)