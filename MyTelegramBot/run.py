import argparse

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("-t", "--token", type=str, help='specify token', required=True)
    parser.add_argument("-H", "--host", type=str, help='back-end host', required=True)
    parser.add_argument("-p", "--port", type=int, help='back-end port', required=True)

    args = parser.parse_args()

    import TelegramBot

    backend_url = "http://{:s}:{:d}".format(args.host, args.port)
    TelegramBot.main(args.token, backend_url)
