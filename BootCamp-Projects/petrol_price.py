import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn import  linear_model
from sklearn.metrics import mean_squared_error, r2_score

df = pd.read_csv(r'\Users\ashis\OneDrive\Documents\GitHub\Repositories\Python-Projects\BootCamp-Projects\Ahmedabad.csv')

prices = df['rate']
dates = df['date']

plt.title('Petrol Prices')
plt.xlabel('Dates')
plt.ylabel('Closing Price')

plt.plot_date(dates, prices, linestyle = 'solid')

plt.show()

# python -u "C:\Users\ashis\OneDrive\Documents\GitHub\Repositories\Python-Projects\BootCamp-Projects\petrol_price.py"