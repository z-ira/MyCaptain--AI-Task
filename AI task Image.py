
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
get_ipython().run_line_magic('matplotlib', 'inline')#%matplotlib inline

data=pd.read_csv('mnist.csv')

data.head()

#Extracting data from data set and viweing them up close
a=data.iloc[3,1:].values

#reshaping the the extracted data into reasonable size
a=a.reshape(28,28).astype('uint8')
plt.imshow(a)

#Preparing the data
#Seperating data and label values
df_x=data.iloc[:,1:]
df_y=data.iloc[:,0]

#Creating test and train size batches
x_train, x_test, y_train, y_test= train_test_split(df_x,df_y,test_size=0.2, random_state=4)

x_train.head()

y_train.head()

#Call Random Forest Classifier
rf = RandomForestClassifier(n_estimators=100)
#fit the model
rf.fit(x_train, y_train)

#Prediction on test data
pred=rf.predict(x_test)
pred

#check the prediction accuracy
s=y_test.values
#calculate number of correctly predicted values
count=0
for i in range(len(pred)):
    if pred[i]==s[i]:
        count=count+1

count

#total values on which the prediction was run on
total_values=len(pred)
total_values

#Accuracy value
Accuracy=count/total_values
Accuracy
