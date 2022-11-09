import datetime
from dateutil.relativedelta import relativedelta

from yahoo_fin.stock_info import get_data
from src.data.gather_data import gather_data

today = datetime.date.today()
last_year = (datetime.datetime.now()-relativedelta(years=1))

ticker = 'AMD'

data = get_data(ticker, start_date = last_year, end_date = today, index_as_date = True, interval = '1d')
company = gather_data(data)
print(company.tail())
company.describe()
company.dropna(inplace=True)
company.describe()

# Select feature columns
features = list(company[['open','high','low','volume','upper_KC','lower_KC','bollinger_up','bollinger_down','MA','momentum']])
# Construct decision tree for target
from sklearn import tree
import matplotlib.pyplot as plt
y = company["close"]
X = company[features]
from sklearn import preprocessing
label_encoder = preprocessing.LabelEncoder()
y = label_encoder.fit_transform(y)
clf = tree.DecisionTreeClassifier()
clf = clf.fit(X,y)
fig = plt.figure(figsize=(25,20))
fig = tree.plot_tree(clf,feature_names=features,class_names='Closing Price',filled=True)
fig.savefig("decistion_tree.png")

# from sklearn import preprocessing

# y = company["close"]
# X = company[features]

# label_encoder = preprocessing.LabelEncoder()
# y = label_encoder.fit_transform(y)

# # Construct decision forest
# from sklearn.ensemble import RandomForestClassifier

# clf = RandomForestClassifier(n_estimators=10)
# clf = clf.fit(X, y)

# #Predict if will close higher
# print (clf.predict([[62.93,63.53,61.40,61068666,66.45,56.06,61.92,56.52,59.22,5]]))