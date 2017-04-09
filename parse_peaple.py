from __future__ import print_function
import pickle
from sklearn import svm

import helpers
from MyGoogleAPI import MyGoogleAPI
from MyOpenFace import MyOpenFace

google_api_key = 'AIzaSyAbXvzhgQj-NVxRpn77JpLXlyuttGpvLyg'
dlib_path = '/root/openface/models/dlib/shape_predictor_68_face_landmarks.dat'
network_model = '/root/openface/models/openface/nn4.small2.v1.t7'

googleAPI = MyGoogleAPI(google_api_key)
openFace = MyOpenFace(dlib_path, network_model)

# clf = svm.SVC()

with open('data.pkl', 'rb') as input:
    data = pickle.load(input)

people_document = googleAPI.search("Nikita", max_results=50)
if 'items' in people_document:
    for person in people_document['items']:
        if not data.get(person['id'], None):
            try:
                described_person = googleAPI.get(person['id'])
                image_url = described_person.get('image', None).get('url', None)[:-6]
                image = helpers.url_to_image(image_url)
                aligned_face = openFace.face_align(image)
                rep = openFace.forward(aligned_face)
                data[person['id']] = (rep, described_person)
                # cv2.imwrite(person['id'] + '.jpg', aligned_face)
                # if described_person.get('gender', None):
                #     gender = described_person.get('gender', None)
                #     reps.append(rep)
                #     y.append(gender)
            except Exception as e:
                print('skip ' + person['id'])
    # clf.fit(reps, y)

    with open('data.pkl', 'wb') as output:
        pickle.dump(data, output, pickle.HIGHEST_PROTOCOL)

# people_document = googleAPI.search("Jhon", max_results=5)
# if 'items' in people_document:
#     for person in people_document['items']:
#         try:
#             described_person = googleAPI.get(person['id'])
#             image_url = described_person.get('image', None).get('url', None)[:-6]
#             image = helpers.url_to_image(image_url)
#             aligned_face = openFace.face_align(image)
#             rep = openFace.forward(aligned_face)
#             gender = clf.predict([rep])
#             print(image_url, gender)
#         except Exception as e:
#             print(e)
