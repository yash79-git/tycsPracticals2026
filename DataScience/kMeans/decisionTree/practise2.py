import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.tree import DecisionTreeClassifier
df=pd.read_csv("data/iris.csv")
lb=LabelEncoder()
df["species"]=lb.fit_transform(df["species"])
x=df[["sepal_length","sepal_width","petal_length","petal_width"]].values
y=df["species"].values
dt=DecisionTreeClassifier()
dt.fit(x,y)
yPredicted=dt.predict([[3,1,2,7]])
match yPredicted:
    case 0:
        print("Sentosa")
    case 1:
        print("versicolor")
    case 2:
        print("virginca")
    case _:
        print("failed to predict")
        
print(yPredicted)


