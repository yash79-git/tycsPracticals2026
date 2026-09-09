import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error,r2_score
from sklearn.preprocessing import LabelEncoder

df=pd.read_csv("data/dataHousing.csv")
#data as some columns which are in string but ml
#accepts only numeric value
le=LabelEncoder()
df["mainroad"]=le.fit_transform(df["mainroad"])
df["guestroom"]=le.fit_transform(df["guestroom"])
df["basement"]=le.fit_transform(df["basement"])
df["hotwaterheating"]=le.fit_transform(df["hotwaterheating"])
df["airconditioning"]=le.fit_transform(df["airconditioning"])
df["prefarea"]=le.fit_transform(df["prefarea"])
df["furnishingstatus"]=le.fit_transform(df["furnishingstatus"])
x=df[["area","bathrooms","stories","parking","bedrooms","furnishingstatus"]].values
y=df[["price"]].values
xTrain,xTest,yTrain,yTest=train_test_split(x,y,test_size=0.2,random_state=42)
reg=LinearRegression()
reg.fit(xTrain,yTrain)
yPredicted=reg.predict(xTest)
mse=mean_squared_error(yTest,yPredicted)
r2=r2_score(yTest,yPredicted)
predictedPrice=reg.predict([[7420,1,2,2,4,0]])
print(predictedPrice)                       
print(r2)









