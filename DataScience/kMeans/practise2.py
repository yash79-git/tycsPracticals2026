import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler
from sklearn.cluster import KMeans

df=pd.read_csv("data/iris.csv")
mm=MinMaxScaler()
df["sepal_length"]=mm.fit_transform(df[["sepal_length"]])
df["sepal_width"]=mm.fit_transform(df[["sepal_width"]])
df["petal_length"]=mm.fit_transform(df[["petal_length"]])
df["petal_width"]=mm.fit_transform(df[["petal_width"]])

km=KMeans(n_clusters=4)
x=df[["sepal_length","sepal_width","petal_length","petal_width"]].values
yPredicted=km.fit_predict(x)
df["cluster"]=yPredicted
print(df)
centroids=km.cluster_centers_
print(centroids)
cluster1=df[df["cluster"]==0]
cluster2=df[df["cluster"]==1]
cluster3=df[df["cluster"]==2]
cluster4=df[df["cluster"]==3]
plt.scatter(cluster1["petal_length"],cluster1["petal_width"],color="red")
plt.scatter(cluster2["petal_length"],cluster2["petal_width"],color="blue")
plt.scatter(cluster3["petal_length"],cluster3["petal_width"],color="green")
plt.scatter(cluster4["petal_length"],cluster4["petal_width"],color="yellow")
plt.scatter(centroids[:,2],centroids[:,3],marker="*")
plt.xlabel("petal_length")
plt.ylabel("petal_width")
plt.show()

rng=range(1,10)
ssw=[]
for k in rng:
    km=KMeans(n_clusters=k)
    km.fit(x)
    ssw.append(km.inertia_)
plt.plot(rng,ssw,color="red")
plt.show()
