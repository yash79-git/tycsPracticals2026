import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.tree import DecisionTreeClassifier

df=pd.read_csv("data/salary.csv")
lb=LabelEncoder()
df["company"]=lb.fit_transform(df["company"])
df["job"]=lb.fit_transform(df["job"])
df["degree"]=lb.fit_transform(df["degree"])
print(df)
x=df[["company","job","degree"]].values
y=df["salary_more_then_100k"].values
print(y)
dt=DecisionTreeClassifier()
dt.fit(x,y)
yPredicted=dt.predict([[2,0,0]])
print(yPredicted)

