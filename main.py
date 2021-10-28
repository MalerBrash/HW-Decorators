import json
import hashlib
from path_settigs import file_path
from logger import logger
from path_settigs import path_logfile


class IterCounter:
    def __init__(self, file):
        self.file = open(file, 'r', encoding='utf-8')

    @logger(path_logfile)
    def __iter__(self):
        link_list = []
        for i in iter(json.load(self.file)):
            for k, v in i.items():
                if k == 'name':
                    for k, v in v.items():
                        if k == 'common':
                            link = 'https://en.wikipedia.org/wiki/' + v.replace(' ', '_') + '\n'
                            link_list.append(link)
                            self.counter_writer(v + ', ' + link)  # вызывает запись страны и ссылки в файл

        return iter(link_list)

    @logger(path_logfile)
    def __next__(self):
        link = next(self)
        return link

    def counter_writer(self, link):
        with open('json_file.txt', 'a', encoding='utf-8') as f:
            f.write(link)


@logger(path_logfile)
def MyHashGen(file_path):  # хэш генератор
    with open(file_path, 'r', encoding='utf-8') as f:
        for i, v in enumerate(f):
            yield hashlib.md5(v.encode()).hexdigest()


if __name__ == '__main__':
    for item in IterCounter('countries.json'):
        print(item)

    for hash in MyHashGen(file_path):
        print(hash)
