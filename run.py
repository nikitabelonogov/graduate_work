from __future__ import print_function

import argparse

from MyFlaskApp import init

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('google_api_key', type=str, help='Google API key')
    parser.add_argument("-p", "--port", type=int, help="specify port to run app")
    parser.add_argument("--network_model", type=str, help="network_model")
    parser.add_argument("--dlib_path", type=str, help="dlib")
    args = parser.parse_args()

    init(args.google_api_key, args.dlib_path, args.network_model)

    from MyFlaskApp import app

    app.run(host='0.0.0.0', port=args.port)

    # app.config['google_api_key'] = args.google_api_key
    # app.config['dlib_path'] = args.dlib_path
    # app.config['network_model'] = args.network_model

    # googleAPI = MyGoogleAPI(app.config['google_api_key'])
    # openFace = MyOpenFace(app.config['dlib_path'], app.config['network_model'])

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
