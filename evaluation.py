from __future__ import print_function
import pickle
import random
from sklearn import svm


def test(slice, data):
    gender = svm.SVC()

    random.shuffle(data)
    train_data = data[:slice]
    test_data = data[slice:]

    gender.fit(map(lambda (k, (r, d)): r, train_data), map(lambda (k, (r, d)): d['gender'], train_data))

    result = map(lambda (k, (r, d)): gender.predict(r.reshape(1, -1)) == d['gender'], test_data)

    return (slice, len(result), len(filter(lambda x: x, result)), len(filter(lambda x: not x, result)))


with open('data/data.pkl', 'rb') as input:
    data = pickle.load(input)
data = data.items()

total = filter(lambda (k, (r, d)): 'gender' in d, data)
male = filter(lambda (k, (r, d)): d['gender'] == 'male', total)
female = filter(lambda (k, (r, d)): d['gender'] == 'female', total)

print("{:s} {:s} {:s} {:s} {:s}".format(
    "train_size",
    "test_size",
    "positive",
    "negative",
    "true_positive",
    "false_positive",
    "false_negative",
    "true_negative",
    "accuracy",
    "precision",
    "recall"))

for slice_position in range(10, 1300, 100):
    for _ in range(5):
        train_size, test_size, positive, negative = test(slice_position, total)
        print("{:d} {:d} {:d} {:d} {:f}".format(
            train_size,
            test_size,
            positive,
            negative,
            float(positive) / float(test_size)))
