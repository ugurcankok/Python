import pandas as pd

dictinary={"NAME":["ugurcan","kerem","ilayda","irem"],
           "AGE":[23,30,25,20],
           "SALARY":[100,150,200,250]}


dataFrame=pd.DataFrame(dictinary)

print(dataFrame)

head=dataFrame.head(2)
tail=dataFrame.tail(3)

print(head)
print(tail)

#pandas basic

print(dataFrame.columns)
print(dataFrame.info())
print(dataFrame.dtypes)
print(dataFrame.describe()) #just numeric value

#indexing slicing

print(dataFrame["NAME"])
print(dataFrame.AGE)

dataFrame["yeni_frame"]=[1,2,3,4]
print(dataFrame)
print(dataFrame.loc[:,"AGE"])
print(dataFrame.loc[:3,"AGE"])
print(dataFrame.loc[:3,"AGE":"NAME"])
print(dataFrame.loc[::-1,:])
print(dataFrame.iloc[:,2])

#filtering

filter1=dataFrame.SALARY >=150
print(filter1)

filter2=dataFrame[filter1]
print(filter2)

filter3=dataFrame.AGE >20
print(dataFrame[filter1 & filter3])

print(dataFrame[dataFrame.AGE==20])

#list comprehension

import numpy as np

average=dataFrame.SALARY.mean()
print(average)
average1=np.mean(dataFrame.SALARY)
print(average1)

dataFrame["check salary"]=["low" if average > each else "high" for each in dataFrame.SALARY]
print(dataFrame)

dataFrame.columns=[each1.lower() for each1 in dataFrame.columns]
print(dataFrame)

dataFrame.columns=[each2.split()[0]+"_"+each2.split()[1] if (len(each2.split())>1) else each2 for each2 in dataFrame.columns]
print(dataFrame)

#concaneting data

dataFrame.drop(["yeni_frame"],axis=1,inplace=True)
print(dataFrame)
#data1=dataFrame.drop(["yeni_frame"],axis=1)

data1=dataFrame.head()
data2=dataFrame.tail()
data3=pd.concat([data1,data2],axis=0)

print(data3)

salary1=dataFrame.salary
age1=dataFrame.age

concat1=pd.concat([salary1,age1],axis=1)
print(concat1)

#transforming data

#dataFrame["multiple_age"]=[each4*2 for each4 in dataFrame.age]
#print(dataFrame)

def multiple(number):
    return number*2


dataFrame["apply_multiple"]=dataFrame.age.apply(multiple)
print(dataFrame)
