import numpy as np

x = np.linspace(0, 10, 100)
y = np.sin(x)

print(x)
print(y)
#xmax = np.argmax(x)



# find the index of the maximum value in y

ymax_idx = np.argmax(y)

# get the x-value corresponding to the maximum value in y
xmax = np.argmax(x)

print(ymax_idx)

print(xmax)