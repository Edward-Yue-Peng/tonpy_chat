from chat_program.chat_client_class import *


def main():
    import argparse

    parser = argparse.ArgumentParser(description="chat client argument")
    parser.add_argument("-d", type=str, default=None, help="server IP addr")
    args = parser.parse_args()

    client = Client(args)
    client.run_chat()


if __name__ == "__main__":
    main()
