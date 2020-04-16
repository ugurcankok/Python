import pandas as pd
import matplotlib as plt


df=pd.read_csv("/Users/ugurcan/Downloads/iris.csv")
print(df)
print(df.columns)
print(df.Species.unique())
print(df.info())
print(df.describe())

setosa=df[df.Species == "Iris-setosa"]
versi=df[df.Species=="Iris-versicolor"]

print(setosa.describe())
print(versi.describe())


df1=df.drop(["Id"],axis=1)
print(df1)

df1.plot()
plt.show()

plt.plot(setosa.Id,setosa.PetalLengthCm,color="red",label="setosa")
plt.xlabel("Id")
plt.ylabel("PetalLengthCm")
plt.legend()


df1.plot(grid=True,alpha=0.5)#alpha opacity linestyle=":"
plt.show()
