# -*- coding: utf-8 -*-
import getpass
import base64


FORWARD	 = tuple('ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/=')
BACKWARD = tuple('oglzmqLIOjcM+b24a=VwpU591SWArNZTtv37h0H6kYQxusByK/ePnGFd8XDEiCRfJ')
KEY = int(getpass.getuser().encode('hex'),16)%0xffff


def shift(character, number=0):
	index = FORWARD.index(character)
	return BACKWARD[(index+number)%65]


def shift_back(character, number=0):
	index = BACKWARD.index(character)
	return FORWARD[(index+number)%65]


def encrypt(src):
	temp = ''.join([unichr(ord(x)^KEY) for x in unicode(src,'utf-8)')]).encode('utf-8').encode('hex')
	temp = base64.standard_b64encode(temp)
	temp = temp[::-1]

	length = len(temp)
	code = ''
	for c in temp:
		code += shift(c, length)
		length -= 1
	return code


def decrypt(src):
	length = len(src)
	temp = ''
	for c in src:
		temp += shift_back(c,-length)
		length -= 1

	temp = temp[::-1]
	temp = base64.standard_b64decode(temp)
	return ''.join([unichr(ord(x)^KEY) for x in temp.decode('hex').decode('utf-8')])


def generate_src(*inputs):
    string = ' '.join(inputs)
    return str(string.encode('utf-8'))





