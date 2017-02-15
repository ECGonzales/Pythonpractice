"""
Simple demo of a horizontal bar chart.
"""
import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
from matplotlib import rcParams
rcParams['font.family'] = 'serif'
rcParams['font.serif'] = ['Times New Roman']
mpl.rcParams['font.size']= '18'


# Example data
people = ('Betty', 'Dan', 'Harry', 'Slim')
x_pos = np.arange(len(people))
performance = 3 + 10 * np.random.rand(len(people))
error = np.random.rand(len(people))


plt.bar(x_pos, performance, yerr=error, align='center', facecolor='mediumspringgreen', alpha=0.8)
plt.xticks(x_pos, people)
plt.xlabel('competitors')
plt.ylabel('Time [seconds]')
plt.title('Race Length amougst four competitors')

plt.show()

