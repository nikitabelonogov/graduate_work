import pickle

from sklearn import svm


class MyClassificator:
    def __init__(self, data_path):
        """

        :param data_path:
        """
        self.gender = svm.SVC()
        self.place = svm.SVC()
        with open(data_path, 'rb') as input:
            data = pickle.load(input)
        gender_reps = []
        gender_y = []
        place_reps = []
        place_y = []
        for k, v in data.items():
            rep, description = v
            if description.has_key('gender'):
                gender_rep = rep
                gender = description['gender']
                gender_reps.append(gender_rep)
                gender_y.append(gender)
            if description.has_key('placesLived'):
                place_rep = rep
                place = description['placesLived'][0]['value']
                place_reps.append(place_rep)
                place_y.append(place)

        self.gender.fit(gender_reps, gender_y)
        self.place.fit(place_reps, place_y)
