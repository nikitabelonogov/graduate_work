from __future__ import print_function

import argparse

import helpers
from GoogleAPI import GoogleAPI
from OpenFace import OpenFace

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('google_api_key', help='Google API key')
    args = parser.parse_args()

    googleAPI = GoogleAPI(args.google_api_key)
    openFace = OpenFace('/root/openface/models/dlib/shape_predictor_68_face_landmarks.dat', '/root/openface/models/openface/nn4.small2.v1.t7')

    people_document = googleAPI.search("John", max_results=1)
    if 'items' in people_document:
        for person in people_document['items']:
            described_person = googleAPI.get(person['id'])
            image_url = described_person.get('image',    None).get('url', None)[:-6]
            image = helpers.url_to_image(image_url)
            rep = openFace.forward(openFace.face_align(image))
            print(rep)
            # print(described_person.get('gender',   None))
            # print(described_person.get('birthday', None))
            # print(described_person.get('url',      None))
