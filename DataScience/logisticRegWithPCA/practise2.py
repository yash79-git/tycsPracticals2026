import pandas as pd
from sklearn.preprocessing import StandardScaler,LabelEncoder
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.decomposition import PCA
df=pd.read_csv("data/titanic.csv")
lb=LabelEncoder()
ss=StandardScaler()
df["Age"]=df["Age"].fillna(df["Age"].median())
df["Cabin"]=df["Cabin"].fillna("Unknown")
df["Cabin"]=lb.fit_transform(df["Cabin"])
df[["Age","Cabin","Pclass"]]=ss.fit_transform(df[["Age","Cabin","Pclass"]])
x=df[["Age","Cabin","Pclass"]].values
y=df["Survived"]

pca=PCA(n_components=2)
xPca=pca.fit_transform(x)
xTrain,xTest,yTrain,yTest=train_test_split(xPca,y)
lr=LogisticRegression()
lr.fit(xTrain,yTrain)
'''yPredicted=lr.predict(xTest)'''
yPredicted=lr.predict([[0.60,1.0]])
if yPredicted == 0:
    print("Not Survived")
else:
    print("Survived")
print(yPredicted)
