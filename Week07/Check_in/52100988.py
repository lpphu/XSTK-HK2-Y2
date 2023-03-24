# 52100988 Lữ Phúc Phú

# Imports
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
sns.set()
import warnings
warnings.simplefilter("ignore", UserWarning)

# Let's create an array of random numbers from uniform distribution
uniform = np.random.uniform(-4,4,1000000)

# Let's create an array of random numbers from normal distribution
normal = np.random.randn(1000000)

# Let's plot them
ax = sns.distplot(uniform, label='Uniform Distribution')
bx = sns.distplot(normal, label= 'Normal Distribution')
legend = plt.legend()
plt.show()