import pandas as pd
import matplotlib.pyplot as plt
#series   1 dimension
#dataframe 2 dimension
s=pd.Series([1,2,3,4,5,6])
print(s)
df=pd.DataFrame({'name':['hamii', 'sami', 'zabii'],
                 'mark':['78', '62', '87']})
print(df)


df=pd.read_csv('week4/Iris.csv')
print(df.head(5))
print(df.tail(5))
print(df.describe())
print(df.info())

#data selecton

print(df['Id'])
print(type(df['Id']))
print(df[['Id','SepalLengthCm']])
print(df.iloc[0])

#remove row where missing data
df.dropna()
#change original dataset (not use )
df.fillna(0,inplace=True)
#nan change with 0
df.fillna(0)

#change column name
print(df.rename(columns={'SepalLengthCm':'SL'},inplace=True))
#change the data type
df['SL']=df['SL'].astype(int)

print(df)
print(df.info())
# we create a new column of (sl square) whwere we cal a square of Sl column 
def fx(a):
    return a*a
df['SL square']=df['SL'].apply(fx)

print(df)

df.to_csv('week4/Iris_updated.csv',index=False)

# concatenate 2 dataset
df1=pd.DataFrame({'name':['hammad', 'sami', 'zohaib','ali','raza','burhan'],
                 'mark':[78, 62, 87,9,55,90]})

df2=pd.DataFrame({'name':['faheem', 'khalid', 'raftaar','ikka','mc stan','anjum'],
                 'mark':[7, 62, 97,99,75,50]})


print(pd.concat([df1,df2]))


#merge based on matching thing like name ,id

df1=pd.DataFrame({'name':['faheem', 'khalid'],
                 'mark':[37, 62 ]})
df2=pd.DataFrame({'name':['faheem', 'khalid'],
                 'roll no':[635, 624]})

print(pd.merge(df1,df2,on='name'))

#.......................................matplotlib

days=['mon','tues','wed','thurs','fri','sat','sun']
temp=[25,28,32,36,22,28,16]
plt.plot(days,temp)
plt.xlabel('Weekday')
plt.ylabel('Temperatures')
plt.title('Aversge temperature over a week')
plt.figure(figsize=(3,3))
plt.show()


days=['mon','tues','wed','thurs','fri','sat','sun']
temp=[25,28,32,36,22,28,16]
plt.bar(days,temp)
plt.xlabel('Weekday')
plt.ylabel('Temperatures')
plt.title('Aversge temperature over a week')
plt.figure(figsize=(3,3))
plt.show()

#days=['mon','tues','wed','thurs','fri','sat','sun']
temp=[25,28,32,36,22,28,16]
plt.hist(temp)
plt.xlabel('Temperatures')
plt.ylabel('frequency')
plt.title('Aversge temperature over a week')
plt.figure(figsize=(3,3))
plt.show()