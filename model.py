import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.ensemble import ExtraTreesRegressor

insurance_data=pd.read_csv('assets/insurance.csv')
	#transform categorical data
le_sex = LabelEncoder()
le_smoker = LabelEncoder()
le_region = LabelEncoder()
	
insurance_data['sex'] = le_sex.fit_transform(insurance_data['sex'])
insurance_data['smoker'] = le_smoker.fit_transform(insurance_data['smoker'])
insurance_data['region'] = le_region.fit_transform(insurance_data['region'])

def read(sex, y_n, location, age, bmi, kids):
	print('Model training and evaluating\n\n')

	
	variables = ['sex','smoker','region','age','bmi','children']
	
	X = insurance_data[variables]
	sc = StandardScaler()
	X = sc.fit_transform(X) 
	Y = insurance_data['expenses']
	X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.3)
	
	#train model
	regressor = ExtraTreesRegressor(n_estimators = 200)
	regressor.fit(X_train,y_train)
	

	#prediction and evaluation
	y_train_pred = regressor.predict(X_train)
	y_test_pred = regressor.predict(X_test)
	
	print('Predicting on new data\n\n')
	

	
	user = [ sex, y_n, location,int(age),float(bmi), int(kids)]
	print('user - ',str(user))
	
	user[0] = le_sex.transform([user[0]])[0] 
	user[1] = le_smoker.transform([user[1]])[0] 
	user[2] = le_region.transform([user[2]])[0] 
	
	X = sc.transform([user])

	cost_for_user = regressor.predict(X)[0]
	print('Cost for user = ',cost_for_user,'\n\n')   
	print(type(cost_for_user))
	finalcost = []
	finalcost = "{:.2f}".format(cost_for_user)
	return finalcost

	


# male='male'
# southwest='southwest'
# yes='yes'
# read(male, yes, southwest, 20, 30.5, 0)
