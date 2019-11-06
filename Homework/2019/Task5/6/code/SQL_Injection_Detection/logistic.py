import numpy as np
import pandas as pd
from sklearn import metrics
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
import joblib


feature = pd.read_csv("./Data/all_data.csv")
arr=feature.values
data = np.delete(arr, -1, axis=1) #删除最后一列
#print(arr)
target=arr[:,6]
#随机划分训练集和测试集
X_train,X_test,y_train,y_test = train_test_split(data,target,test_size=0.3,random_state=3)
#模型
clf=LogisticRegression(solver='liblinear',multi_class='auto')#创建分类器对象，
clf.fit(X_train,y_train)#训练模型
joblib.dump(clf, './Model/logistic.model')
print("Logistic.model 被保存到：'/Model/logistic.model'目录下")

y_pred=clf.predict(X_test)#预测
print("Logistic:")
print("y_pred:%s"%y_pred)
print("y_test:%s"%y_test)

print('Precision:%.3f' %metrics.precision_score(y_true=y_test,y_pred=y_pred))
print('Recall:%.3f' %metrics.recall_score(y_true=y_test,y_pred=y_pred))

