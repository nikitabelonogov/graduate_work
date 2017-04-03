from __future__ import print_function

import argparse

import cv2

import helpers
from MyGoogleAPI import MyGoogleAPI
from MyOpenFace import MyOpenFace

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('google_api_key', help='Google API key')
    args = parser.parse_args()

    googleAPI = MyGoogleAPI(args.google_api_key)
    openFace = MyOpenFace('/root/openface/models/dlib/shape_predictor_68_face_landmarks.dat',
                          '/root/openface/models/openface/nn4.small2.v1.t7')

    # people_document = googleAPI.search("John", max_results=1)
    # if 'items' in people_document:
    #     for person in people_document['items']:
    #         described_person = googleAPI.get(person['id'])
    #         image_url = described_person.get('image',    None).get('url', None)[:-6]
    #         image = helpers.url_to_image(image_url)
    #         aligned_face = openFace.face_align(image)
    #         rep = openFace.forward(aligned_face)
    #         cv2.imwrite(person['id'] + '.jpg', aligned_face)
    #         print(rep)
