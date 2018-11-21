# -*- coding: utf-8 -*-
from AlfredItemsList import AlfredItemsList
from query import Query
import enigma
import sys
import os


def encrypt_method(*entities):
    record_src = enigma.generate_src(*entities)
    record = enigma.encrypt(record_src)
    return record

def decrypt_method(line):
    temp = enigma.decrypt(line.rstrip()).split(' ')
    return tuple(temp)


query = Query(sys.argv[1], encrypt_method, decrypt_method)
al = AlfredItemsList()


def password():
    for website, username in query.search_records():
        hearder = 'get'
        arg = hearder+' '+website+' '+username
        al.append(arg, website, username, uid=arg)

    if len(query.query_words) > 1 and not query.absolute_match():
        website = query.query_words[0]
        username = query.query_words[1]

        hearder = 'new'
        arg = hearder+' '+website+' '+username
        title = website+' - New password'
        subtitle = 'Create password for '+username+' in '+website
        al.append(arg, title, subtitle, uid=arg)

    if al.is_empty():
        title = 'No Result'
        al.append('', title, '')

    print(al)


def allpassword():
    for website, username in query.all_records():
        hearder = 'get'
        arg = hearder+' '+website+' '+username
        al.append(arg, website, username, uid=arg)

    print(al)


def verify(key):
    website = os.environ['website'].decode('utf-8')
    username = os.environ['username'].decode('utf-8')
    title = 'Verify the user'
    subtitle = website+' '+username

    al.append(key, title, subtitle, uid='password')
    print(al)


def process(key):
    header = os.environ['header'].decode('utf-8')
    website = os.environ['website'].decode('utf-8')
    username = os.environ['username'].decode('utf-8')

    if header == 'del':
        query.delete_record(website, username)
        sys.stdout.write('')
        return

    if header == 'new':
        query.append_record(website, username)

    src = enigma.generate_src(website, key, username)
    password = generate_password(src)
    sys.stdout.write(password)


def generate_password(src, length=12):
    import hashlib
    import re

    def missing(raw_code):
        char_set = {
            'upper':tuple('ABCDEFGHIJKLMNOPQRSTUVWXYZ'),
            'lower':tuple('abcdefghijklmnopqrstuvwxyz'),
            'digit':tuple('0123456789')
        }
        counter = {'upper':0,'lower':0,'digit':0}

        for c in raw_code:
            for i in counter:
                if c in char_set[i]:
                    counter[i] += 1
                    break
        missing_set = []
        for i in counter:
            if counter[i] <= 1:
                missing_set.append(char_set[i])
        return missing_set

    try:
        raw = hashlib.md5(src)
    except:
        raw = hashlib.md5(src.encode('utf-8'))
    raw = re.sub(r'[^\w]', '', enigma.encrypt(raw.hexdigest()))
    raw_code = raw[length::len(raw)//length//2-1][length:2*length]
    
    missing_set = missing(raw_code)
    if not missing_set:
        return raw_code[::-1]

    code = raw_code[:length-len(missing_set)]
    for s in missing_set:
        for c in raw[::-1]:
            if c in s:
                i = raw.index(c)%length
                code = code[:i]+c+code[i:]
                break

    return code[::-1]




