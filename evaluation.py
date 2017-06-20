from __future__ import print_function
import pickle
import random
from sklearn import svm


def test(slice, data):
    """
    Performs a evaluation.
    :param slice: slice data value
    :param data: data
    :return: train data size
            test data size,
            positive,
            negative,
            precision male,
            recall male,
            precision female,
            recall female
    """
    gender = svm.SVC()

    random.shuffle(data)
    train_data = data[:slice]
    test_data = data[slice:]

    gender.fit(map(lambda (k, (r, d)): r, train_data), map(lambda (k, (r, d)): d['gender'], train_data))

    pred_result = map(lambda (k, (r, d)): str(gender.predict(r.reshape(1, -1))[0]), test_data)
    test_result = map(lambda (k, (r, d)): str(d['gender']), test_data)

    positive = filter(lambda (x, y): x == y, zip(pred_result, test_result))
    negative = filter(lambda (x, y): x != y, zip(pred_result, test_result))

    ConfusionMatrix = [[0, 0], [0, 0]]
    ConfusionMatrix[0][0] = float(
        len(filter(lambda (x, y): x == 'male' and y == 'male', zip(pred_result, test_result))))
    ConfusionMatrix[0][1] = float(
        len(filter(lambda (x, y): x == 'male' and y == 'female', zip(pred_result, test_result))))
    ConfusionMatrix[1][0] = float(
        len(filter(lambda (x, y): x == 'female' and y == 'male', zip(pred_result, test_result))))
    ConfusionMatrix[1][1] = float(
        len(filter(lambda (x, y): x == 'female' and y == 'female', zip(pred_result, test_result))))

    precision_male = 0.0
    recall_male = 0.0
    precision_female = 0.0
    recall_female = 0.0

    try:
        precision_male = ConfusionMatrix[0][0] / (ConfusionMatrix[0][0] + ConfusionMatrix[0][1])
        recall_male = ConfusionMatrix[0][0] / (ConfusionMatrix[0][0] + ConfusionMatrix[1][0])
        precision_female = ConfusionMatrix[1][1] / (ConfusionMatrix[1][1] + ConfusionMatrix[1][0])
        recall_female = ConfusionMatrix[1][1] / (ConfusionMatrix[1][1] + ConfusionMatrix[0][1])
    except:
        pass

    return (slice,
            len(pred_result),
            len(positive),
            len(negative),
            precision_male,
            recall_male,
            precision_female,
            recall_female)


def Fmeasure(precision, recall):
    """
    Evaluates Fmeasure by precision and recall.
    :param precision: precision value
    :param recall: recall value
    :return: Fmeasure
    """
    result = 0.0
    try:
        result = 2 * (precision * recall) / (precision_male + recall_male)
    except:
        pass
    return result


with open('MyFlaskApp/data/data.pkl', 'rb') as input:
    data = pickle.load(input)
data = data.items()

total = filter(lambda (k, (r, d)): 'gender' in d, data)
male = filter(lambda (k, (r, d)): d['gender'] == 'male', total)
female = filter(lambda (k, (r, d)): d['gender'] == 'female', total)

print("{:s} {:s} {:s} {:s} {:s} {:s} {:s} {:s} {:s} {:s} {:s}".format(
    "train_size",
    "test_size",
    "positive",
    "negative",
    "accuracy",
    "precision_male",
    "recall_male",
    "Fmeasure_male",
    "precision_female",
    "recall_female",
    "Fmeasure_female"))

for slice_position in range(100, 1300, 50):
    for _ in range(5):
        train_size, \
        test_size, \
        positive, \
        negative, \
        precision_male, \
        recall_male, \
        precision_female, \
        recall_female \
            = test(slice_position, total)
        print("{:d} {:d} {:d} {:d} {:f} {:f} {:f} {:f} {:f} {:f} {:f}".format(
            train_size,
            test_size,
            positive,
            negative,
            float(positive) / float(test_size),
            precision_male,
            recall_male,
            Fmeasure(precision_male, recall_male),
            precision_female,
            recall_female,
            Fmeasure(precision_female, recall_female)))
