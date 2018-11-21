# -*- coding: utf-8 -*-

class Query(object):

    def __init__(self, query_text, encrypt, decrypt):
        self.query_words = filter(None, query_text.decode('utf-8').split(' '))
        self.path = 'records.txt'
        self.records = []
        self.encrypt = encrypt
        self.decrypt = decrypt

        with open(self.path, 'r') as file:
            lines = file.readlines()
            for line in lines:
                if not line.strip():
                    continue
                record = self.decrypt(line)
                self.records.append(record)

    def absolute_match(self):
        def same(words, entity):
            return words[0] == entity[0] and words[1] == entity[1]
        if (len(self.query_words) == 2):
            return any([same(self.query_words, entity) for entity in self.records])
        return False

    def create_query(self, query_words):
        def is_matching(query_word, entity):
            return query_word.lower() in entity.lower()
        def is_record_matching(record):
            if len(query_words) == 1:
                return any([is_matching(query_words[0], entity) for entity in record])
            return all([is_matching(query_words[i], record[i]) for i in xrange(min(len(query_words),len(record)))])
        return is_record_matching


    def all_records(self):
        for record in self.records:
            yield record


    def search_records(self, query_words=None):
        if not query_words:
            query_words = self.query_words
        query = self.create_query(query_words)
        for record in self.records:
            if query(record):
                yield record

   
    def append_record(self, *entities):
        record = self.encrypt(*entities)
        with open(self.path, 'a') as file:
            file.write(record+'\n')

   
    def delete_record(self, *entities):
        record = self.encrypt(*entities)
        with open(self.path, 'r+') as file:
            lines = file.readlines()
            file.seek(0)
            for line in lines:
                if line.strip() != record:
                    file.write(line)
            file.truncate()

