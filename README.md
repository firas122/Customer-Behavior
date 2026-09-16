# Customer Behavior Prediction

A small script that predicts whether a customer is likely to be interested in
a given offer, based on their age. It pulls user records (date of birth +
wishlist) from MongoDB, derives each user's age, labels them by whether their
wishlist contains a target offer, and fits a scikit-learn logistic regression
model on age → interest.

## How it works

1. Connects to MongoDB and reads a slice of `usersData` (`user_id`, `date`,
   `wishlist`).
2. Computes each user's age from their date of birth.
3. Labels each user `1` if their wishlist contains the target offer ID, else
   `0`.
4. Fits a `LogisticRegression` model on `age → interested_in_offer`.
5. Prints a prediction for a sample age.

## Setup

```sh
git clone https://github.com/firas122/Customer-Behavior
cd Customer-Behavior
pip install -r requirements.txt
```

Set the MongoDB connection string via an environment variable (defaults to
`mongodb://localhost:27017` if unset):

```sh
export MONGO_URI="mongodb://<user>:<password>@<host>/<db>"
```

## Usage

```sh
python Main.py
```

Output is a single printed line with the predicted label (0 or 1) for the
configured sample age, e.g.:

```
Predicted interest in offer d43acddc-7e8d-4419-a8b6-8ddb9acf76a8 for age 30: [1]
```

The target offer ID, the slice of users to train on, and the sample
prediction age are configured as constants at the top of `Main.py`.

## Note

This is a small proof-of-concept script, not a served API — there's no
Flask/HTTP layer here, just a script you run directly. Because it's trained
on a small slice of records with a single feature (age), treat its output as
illustrative rather than production-grade.

## License

MIT — see [LICENSE](LICENSE).
