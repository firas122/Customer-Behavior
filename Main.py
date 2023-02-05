from datetime import datetime, date
import numpy
import pymongo as pymongo
from sklearn import linear_model

#Vars
ages = []
vals = []
b = 0
offer1 = "d43acddc-7e8d-4419-a8b6-8ddb9acf76a8"


client = pymongo.MongoClient("mongo string here")
db = client.Test

#funcs
def calculate_age(born):
    today = date.today()
    return(today.year - born.year - ((today.month, today.day) < (born.month, born.day)))

def logit2prob(logr, X):
    log_odds = logr.coef_ * X + logr.intercept_
    odds = numpy.exp(log_odds)
    probability = odds / (1 + odds)
    return (probability)

#Code

userIds = db.usersData.find({}, {"user_id": 1, "date": 1, "wishlist": 1})
for i in range(200, 550):
    k = "e85b5c4e-663b-425b-b55b-70f04d0c1bcf"
    ages.append(calculate_age(datetime.strptime(userIds[i]["date"], '%Y-%m-%d').date()))
    print(calculate_age(datetime.strptime(userIds[i]["date"], '%Y-%m-%d').date()))

    for a in range(len(userIds[i]["wishlist"])):
        k = userIds[i]["wishlist"][a]["offer_id"]
        if k == offer1:
            b = 1
            break
        else:
            b = 0
    vals.append(b)

X = numpy.array(ages).reshape(-1, 1)
y = numpy.array(vals)
print(X, y)
logr = linear_model.LogisticRegression()
logr.fit(X,y)
predicted = logr.predict(numpy.array([30]).reshape(-1,1))
print("prediction", predicted)
#def logit2prob(logr, X):
#  log_odds = logr.coef_ * X + logr.intercept_
#  odds = numpy.exp(log_odds)
#  probability = (odds**(-2.91+6.26*0.1)) / (1 + (odds**(-2.91+6.26*0.1)))
#  return(probability)

#print(logit2prob(logr, X))
