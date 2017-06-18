from __future__ import print_function

import pickle
import threading

import names
from MyGoogleAPI import MyGoogleAPI
from MyOpenFace import MyOpenFace

from MyFlaskApp import helpers

google_api_key = 'AIzaSyAbXvzhgQj-NVxRpn77JpLXlyuttGpvLyg'
dlib_path = '/root/openface/models/dlib/shape_predictor_68_face_landmarks.dat'
network_model = '/root/openface/models/openface/nn4.small2.v1.t7'


googleAPI = MyGoogleAPI(google_api_key)
openFace = MyOpenFace(dlib_path, network_model)


def worker(num, query):
    googleAPI = MyGoogleAPI(google_api_key)
    openFace = MyOpenFace(dlib_path, network_model)
    print('%s %s' % (num, query))
    people_document = googleAPI.search(query, max_results=50)
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
                    print('%s parse %s' % (num, person['url']))
                except Exception as e:
                    print('%s skip  %s' % (num, person['url']))
        dump_data = data.copy()
        with open('data.pkl', 'wb') as output:
            pickle.dump(dump_data, output, pickle.HIGHEST_PROTOCOL)

    return


with open('data.pkl', 'rb') as input:
    data = pickle.load(input)

threads = []

t = threading.Thread(target=worker, args=(0, 'russia'))
t.start()

for i in range(5):
     name = names.get_first_name()
     t = threading.Thread(target=worker, args=(i, 'name',))
     threads.append(t)
     t.start()



# print('end')


# while len(data) < 1000:
#     name = names.get_first_name()
#     print('parsing ' + name)
#     people_document = googleAPI.search(name, max_results=50)
#     if 'items' in people_document:
#         for person in people_document['items']:
#             if not data.get(person['id'], None):
#                 try:
#                     described_person = googleAPI.get(person['id'])
#                     image_url = described_person.get('image', None).get('url', None)[:-6]
#                     image = helpers.url_to_image(image_url)
#                     aligned_face = openFace.face_align(image)
#                     rep = openFace.forward(aligned_face)
#                     data[person['id']] = (rep, described_person)
#                     print('parse ' + person['id'])
#                 except Exception as e:
#                     print('skip  ' + person['id'])
#
#         print('writing ' + str(len(data)))
#
#         with open('data.pkl', 'wb') as output:
#             pickle.dump(data, output, pickle.HIGHEST_PROTOCOL)
#             exec_in_terminal('rm -rf all files, \'*\'');
