import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from pandas.plotting import scatter_matrix

house = pd.read_csv("housing.csv")

house.head(5)

house.info()
house['ocean_proximity'].value_counts()

house.hist(bins = 50, figsize = (20,15))

house.plot(kind='scatter',x='longitude',y='latitude', alpha = 0.1)
house.plot(kind='scatter',x='longitude',y='latitude', alpha = 0.5,
           s=house['population']/100,
           c='median_house_value', cmap=plt.get_cmap('jet'),
           colorbar = True
           )

attributes = ['median_house_value', 'median_income', 'total_rooms', 'housing_median_age']
scatter_matrix(house[attributes], sigsize=(8,6))

#creates new attributes using pre-made attributes
house['rooms_per_household'] = house['total_bedrooms'] / house['households']
house['bedrooms_per_room'] = house['total_bedrooms'] / house['total_rooms']
house['population_per_house'] = house['population'] / house['households']

#changing to numeric only ensures that we only use numbers and not strings
corr_matrix = house.corr(numeric_only=True)
corr_matrix['median_house_value'].sort_values(ascending=False)
