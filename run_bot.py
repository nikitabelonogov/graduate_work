import argparse

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("-t", "--token", type=str, help='specify token')
    parser.add_argument("-D", "--Data", type=str, help='specify data', default='data.pkl')
    parser.add_argument("--network_model", type=str, help='network_model')
    parser.add_argument("--dlib_path", type=str, help='dlib')
    dlib_path = '/root/openface/models/dlib/shape_predictor_68_face_landmarks.dat'
    network_model = '/root/openface/models/openface/nn4.small2.v1.t7'
    data_path = 'data.pkl'
    args = parser.parse_args()

    import MyTelegramBot

    MyTelegramBot.main(args.token)
