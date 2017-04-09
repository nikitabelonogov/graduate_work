from __future__ import print_function

import argparse

from MyFlaskApp import init

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("-H", "--Host", type=str, help='specify host', default='0.0.0.0')
    parser.add_argument("-P", "--Port", type=int, help='specify port', default=8000)
    parser.add_argument("-D", "--Data", type=str, help='specify data', default='data.pkl')
    parser.add_argument("--network_model", type=str, help='network_model')
    parser.add_argument("--dlib_path", type=str, help='dlib')
    args = parser.parse_args()

    init(args.dlib_path, args.network_model, args.Data)

    from MyFlaskApp import app

    app.run(host=args.Host, port=args.Port)
