import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns #statistical graphic
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn import metrics #find performance of the model
from xgboost import XGBRegressor#k-fold cross validation

"""data collection and analysis

"""

#loading dataset to pandas from csv
big_mart_data=pd.read_csv('/content/Train.csv')
big_mart_data.head()

big_mart_data.shape

big_mart_data.info()

"""categorical features:
- Item_Identifier
- Item_Fat_Content
- Item_Type
- Outlet_Identifier
- Outlet_Size
- Outlet_Location_Type	
- Outlet_Type


"""

big_mart_data.isnull().sum()

"""handling missing values
- mean()values
- mode() unvalued
"""

#mean
mean=big_mart_data['Item_Weight'].mean()
mean

"""filling the missing value in item weight"""

big_mart_data['Item_Weight'].fillna(mean,inplace=True)

big_mart_data.isnull().sum()

mode_of_Outlet_size = big_mart_data.pivot_table(values='Outlet_Size', columns='Outlet_Type', aggfunc=(lambda x: x.mode()[0]))

mode_of_Outlet_size

miss_values = big_mart_data['Outlet_Size'].isnull()

miss_values

big_mart_data.loc[miss_values, 'Outlet_Size'] = big_mart_data.loc[miss_values,'Outlet_Type'].apply(lambda x: mode_of_Outlet_size[x])

big_mart_data.isnull().sum()

big_mart_data.info()

big_mart_data.info()

big_mart_data.isnull().sum()

"""data analysiss part

"""

big_mart_data.describe()

"""numerical plot analysis:"""

sns.set()
plt.figure(figsize=(6,6))
sns.distplot(big_mart_data['Item_Weight'])
plt.show()

sns.set()
plt.figure(figsize=(6,6))
sns.distplot(big_mart_data['Item_Visibility'])
plt.show()

sns.set()
plt.figure(figsize=(6,6))
sns.distplot(big_mart_data['Item_MRP'])
plt.show()

sns.set()
plt.figure(figsize=(6,6))
sns.distplot(big_mart_data['Item_Outlet_Sales'])
plt.show()

#Outlet_Establishment_Year
sns.set()
plt.figure(figsize=(6,6))
sns.countplot(x='Outlet_Establishment_Year',data=big_mart_data)
plt.show()

"""categorical featuress:

"""

#Item_Fat_Content
sns.set()
plt.figure(figsize=(6,6))
sns.countplot(x='Item_Fat_Content',data=big_mart_data)

#Item_Type
sns.set()
plt.figure(figsize=(25,6))
sns.countplot(x='Item_Type',data=big_mart_data)

sns.set()
  plt.figure(figsize=(6,6))
  sns.countplot(x='Outlet_Size',data=big_mart_data)

big_mart_data.replace({'Item_Fat_Content' : {'low fat': 'Low Fat','LF':'Low Fat','reg':'Regular'}},inplace=True)

big_mart_data['Item_Fat_Content'].value_counts()

#Item_Fat_Content
sns.set()
plt.figure(figsize=(6,6))
sns.countplot(x='Item_Fat_Content',data=big_mart_data)

"""**label encoder**"""

encoder=LabelEncoder()

big_mart_data.info()

big_mart_data['Item_Identifier']=encoder.fit_transform(big_mart_data['Item_Identifier'])
big_mart_data['Item_Fat_Content']=encoder.fit_transform(big_mart_data['Item_Fat_Content'])
big_mart_data['Item_Type']=encoder.fit_transform(big_mart_data['Item_Type'])
big_mart_data['Outlet_Identifier']=encoder.fit_transform(big_mart_data['Outlet_Identifier'])
big_mart_data['Outlet_Size']=encoder.fit_transform(big_mart_data['Outlet_Size'])
big_mart_data['Outlet_Location_Type']=encoder.fit_transform(big_mart_data['Outlet_Location_Type'])
big_mart_data['Outlet_Type']=encoder.fit_transform(big_mart_data['Outlet_Type'])

big_mart_data.head()

X=big_mart_data.drop('Item_Outlet_Sales',axis=1)
Y=big_mart_data['Item_Outlet_Sales']
print(X)
print(Y)

"""## **splitting the data into training and testing types:**"""

X_train,X_test,Y_train,Y_test=train_test_split(X,Y,test_size=0.2,random_state=2)

print(X.shape,X_train.shape,X_test.shape)

"""# machine learning model trainng"""

regressor=XGBRegressor()
regressor.fit(X_train,Y_train)
regressor.fit(X_test,Y_test)

train_data_predict=regressor.predict(X_train)
r2_score=metrics.r2_score(Y_train,train_data_predict)
print(r2score)

test_data_prediction = regressor.predict(X_test)
r2_test = metrics.r2_score(Y_test, test_data_prediction)
print(r2_test)

