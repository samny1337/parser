import re
from collections import Counter
import csv


def reader(filename):
    # Считывает ip адреса из файла с логами.
    regexp = r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}'

    with open(filename) as f:
        log = f.read()
        ips_list = re.findall(regexp, log)
        return ips_list


def count(ips_list):
    # Считает колличество каждого повторения ip адресса.
    counter = Counter(ips_list)
    return counter


def write_csv(counter):
    # Записывает результат в csv файл и создает заголовок.
    with open('output.csv', 'w') as csvfile:
        writer = csv.writer(csvfile)
        header = ['IP', 'Frequency']
        writer.writerow(header)
        for item in counter:
            writer.writerow((item, counter[item]))



if __name__ == '__main__':
    write_csv(count(reader('logs2.log')))
