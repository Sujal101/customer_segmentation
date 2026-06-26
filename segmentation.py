# import libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import pickle as pkl
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
df= pd.read_csv("Mall_Customers.csv")
print(df.head())
print(df.isnull().sum())
x = df[["Annual Income (k$)","Spending Score (1-100)","Age"]]
scaler = StandardScaler()
x_scaled = scaler.fit_transform(x)
wcss = []
for i in range(1,11):
    model = KMeans(n_clusters=i)
    model.fit(x_scaled)
    wcss.append(model.inertia_)
plt.plot(range(1,11), wcss)
plt.show()
kmeans = KMeans(n_clusters=3)
cluster =kmeans.fit_predict(x_scaled)
df['Cluster'] = cluster
print(df['Cluster'])
with open("Mall_Customers_0.pkl","wb") as f:
    pkl.dump(kmeans,f)
with open("Mall_Customers_1.pkl", "wb") as f:
        pkl.dump(scaler, f)
