import os
from datetime import datetime, date

import numpy
import pymongo
from sklearn import linear_model

# Config
MONGO_URI = os.environ.get("MONGO_URI", "mongodb://localhost:27017")
TARGET_OFFER_ID = "d43acddc-7e8d-4419-a8b6-8ddb9acf76a8"
USER_RANGE_START = 200
USER_RANGE_END = 550
PREDICTION_AGE = 30

client = pymongo.MongoClient(MONGO_URI)
db = client.Test


def calculate_age(born):
    today = date.today()
    return today.year - born.year - ((today.month, today.day) < (born.month, born.day))


ages = []
liked_target_offer = []

users = db.usersData.find({}, {"user_id": 1, "date": 1, "wishlist": 1})
for i in range(USER_RANGE_START, USER_RANGE_END):
    try:
        user = users[i]
        age = calculate_age(datetime.strptime(user["date"], "%Y-%m-%d").date())
    except (IndexError, KeyError, ValueError):
        continue

    liked_target = 0
    for item in user.get("wishlist", []):
        if item.get("offer_id") == TARGET_OFFER_ID:
            liked_target = 1
            break

    ages.append(age)
    liked_target_offer.append(liked_target)

X = numpy.array(ages).reshape(-1, 1)
y = numpy.array(liked_target_offer)

model = linear_model.LogisticRegression()
model.fit(X, y)

prediction = model.predict(numpy.array([PREDICTION_AGE]).reshape(-1, 1))
print(f"Predicted interest in offer {TARGET_OFFER_ID} for age {PREDICTION_AGE}: {prediction}")
