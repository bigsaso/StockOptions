# PART 1: Data Pre-Processing
# Step 0: Fire the system
import datetime as dt
from dateutil.relativedelta import relativedelta
from keras.callbacks import EarlyStopping,ReduceLROnPlateau,ModelCheckpoint, TensorBoard
from yahoo_fin.stock_info import get_data
from gather_data import gather_data
# Step 1: Read data
today = dt.date.today()
last_year = (dt.datetime.now()-relativedelta(years=1))
ticker = 'AMD'
data = get_data(ticker, start_date = last_year, end_date = today, index_as_date = True, interval = '1d')
company = gather_data(data)
company.index.name = 'Date'
#company.dropna(inplace=True)
print(company.head())

# Select features to be involved in training and prediction
features = list(company[['open','high','low','volume','upper_KC','lower_KC','bollinger_up','bollinger_down','MA','momentum','close']])
# Extract dates (will be used in visualiation)
datelist_train = list(company.index)
datelist_train = [date.strftime('%Y-%m-%d') for date in datelist_train]
print('Training set shape == {}'.format(company.shape))
print('All timestamps == {}'.format(len(datelist_train)))
print('Features selected: {}'.format(features))
# Step 2: Data Pre-processing
company = company[features].astype(str)
for i in features:
    for j in range(0,len(company)):
        company[i][j] = company[i][j].replace(',','')
company = company.astype(float)
# Using multiple predictors (features)
training_set = company.values
print('Shape of training set == {}.'.format(training_set.shape))
print(training_set)