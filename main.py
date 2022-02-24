import gzip
from os import listdir
from os.path import isfile, join
from typing import List

exchange_name = ["cexio", "bithumb", "binance", "ftx", "gateio", "huobi", "kucoin", "okex"]
current_log_file_path = "./logs/current/connectors-log.log"


def gz_file_names() -> List[str]:
    return [f for f in listdir("./logs/zipped") if isfile(join("./logs/zipped", f)) and ".gz" in f]


def print_files():
    only_files = [f for f in listdir("./logs/zipped") if isfile(join("./logs/zipped", f))]
    print(only_files)


def cur_print_all_error():
    """
    Prints to the console found line with ERROR or 10 lines of Exception stack trace
    """
    with open(file=current_log_file_path, mode="r") as log_file:
        lines = iter([line.rstrip('\n') for line in log_file])
        for line in lines:
            # if "ERROR" in line:
            #     print(line)
            if "org.knowm.xchange.exceptions.ExchangeException" in line:
                print(line)
                for _ in range(10):
                    stack_trace = next(lines)
                    print('            ' + stack_trace)


def cur_find_by_key(key_word: str):
    """
    Prints to the console found line with provided key_word
    :param key_word:
        ERROR,
        ExchangeException,
        arbitrageId,
        etc
    """
    with open(file=current_log_file_path, mode="r") as log_file:
        lines = iter([line.rstrip('\n') for line in log_file])

        for line in lines:
            if key_word in line:
                print(line)


def cur_find_by_key_exchange(key_word: str):
    """
    Prints to the console found line with provided key_word
    :param key_word:
        ERROR,
        ExchangeException,
        arbitrageId,
        etc
    """
    for exchange in exchange_name:
        print(f"================={exchange}=================")
        exchange_key_word = key_word.replace("__exchange__", exchange)
        with open(file=current_log_file_path, mode="r") as log_file:
            lines = iter([line.rstrip('\n') for line in log_file])

            for line in lines:
                if exchange_key_word in line:
                    print(line)


def gz_find_by_key_exchange_all(key_word: str):
    """
    Prints to the console found line with provided key_word
    :param key_word:
        ERROR,
        ExchangeException,
        arbitrageId,
        etc
    """
    for file_name in gz_file_names():
        print(f"\n=================================={file_name}==================================")
        for exchange in exchange_name:
            print(f"-----------------------{exchange}-----------------------")
            exchange_key_word = key_word.replace("__exchange__", exchange)
            with gzip.open(filename=f"./logs/zipped/{file_name}", mode="rb") as gz_file:
                lines = [line.decode("utf-8").rstrip("\n") for line in gz_file.readlines()]

            for line in lines:
                if exchange_key_word in line:
                    print(line)


if __name__ == "__main__":
    # gz_find_by_key_exchange_all('{"exchange":"__exchange__","status":"DISCONNECTED"}')

    # cur_find_by_key('{"exchange":"cexio","status":"DISCONNECTED"}')
    # cur_find_by_key_exchange('{"exchange":"__exchange__","status":"DISCONNECTED"}')
    cur_print_all_error()
