import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
data = {
    "height": [170, 165, 180, 155, 175, 160, 182, 158, 168, 178],
    "weight": [65, 55, 80, 50, 72, 58, 85, 52, 62, 75],
    "age":    [25, 22, 30, 21, 28, 24, 32, 23, 26, 29],
    "gender": [1, 0, 1, 0, 1, 0, 1, 0, 0, 1]
}
df=pd.DataFrame(data)
x=df.drop(["gender"],axis=1)
y=df["gender"]
ss=StandardScaler()
x_scaled=ss.fit_transform(x)
pca=PCA(n_components=2)
xPca=pca.fit_transform(x_scaled)
print(xPca)
xTrain,xTest,yTrain,yTest=train_test_split(xPca,y,test_size=0.3,random_state=42)
lr=LogisticRegression()
lr.fit(xTrain,yTrain)
'''yPredicted=lr.predict(xTest)
print(yPredicted)'''
yPredicted=lr.predict([[0.55,0.66]])
if yPredicted==0:
    print("Male")
else:
    print("Female")
    print(yPredicted)
