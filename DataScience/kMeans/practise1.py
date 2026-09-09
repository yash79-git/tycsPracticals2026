import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler
from sklearn.cluster import KMeans
df=pd.read_csv("data/income.csv")
mm=MinMaxScaler()
df["Age"]=mm.fit_transform(df[["Age"]])
df["Income"]=mm.fit_transform(df[["Income"]])
km=KMeans(n_clusters=3)
x=df[["Age","Income"]]
yPredicted=km.fit_predict(x)
print(yPredicted)
df["cluster"]=yPredicted
print(df)
centroids=km.cluster_centers_
print(centroids)
cluster1=df[df["cluster"]==0]
cluster2=df[df["cluster"]==1]
cluster3=df[df["cluster"]==2]
plt.scatter(cluster1["Age"],cluster1["Income"],color="red")
plt.scatter(cluster2["Age"],cluster2["Income"],color="green")
plt.scatter(cluster3["Age"],cluster3["Income"],color="blue")
plt.scatter(centroids[:,0],centroids[:,1],marker="*",color="yellow")
plt.xlabel("Age")
plt.ylabel("Income")
plt.show()

rng=range(1,10)
#distance from centroids
sse=[]
for k in rng:
    km=KMeans(n_clusters=k)
    km.fit(x)
    sse.append(km.inertia_)
plt.plot(rng,sse)
plt.xlabel("Age")
plt.ylabel("Income")
plt.show()

