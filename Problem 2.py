import numpy as np
A=np.arange(1,101)
a=np.reshape(A,(10,10))
A=A**2
div_by_3=A[A%3==0]