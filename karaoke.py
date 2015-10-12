#!/usr/bin/python3
# -*- coding: utf-8 -*-
import sys
from xml.sax import make_parser
from xml.sax.handler import ContentHandler
from smallsmilhandler import SmallSMILHandler
import json
import urllib.request


def take_filename():
    if len(sys.argv) != 2:
        sys.exit("Usage:  python3 karaoke.py file.smil")
    else:
        return sys.argv[1]


class KaraokeLocal():
    def __init__(self, filename):
        parser = make_parser()
        cHandler = SmallSMILHandler()
        parser.setContentHandler(cHandler)
        parser.parse(open(filename))
        self.list_tags = cHandler.get_tags()

    def __str__(self):
        str_tags = ''
        for tag in self.list_tags:
            str_tags += tag[0] # tag[0] is the tag name
            for key, value in tag[1].items(): # tag[1] is the attributes dict
                if value != '':
                    str_tags += '\t%s="%s"' % (key, value)
            if tag != self.list_tags[-1]:
                str_tags += '\n'
        return str_tags

    def to_json(self, smile_file, json_file=''):
        if json_file == '':
            json_file = smile_file.split('.')[0] + '.json'
        data = json.dumps(self.list_tags)
        with open(json_file, 'w') as outfile:
            json.dump(data, outfile)

    def do_local(self):
        for tag in self.list_tags:
            attributes = tag[1]
            for key in attributes:
                if 'src' in attributes and 'http://' in attributes[key]:
                    filename = attributes[key].split('/')[-1]
                    urllib.request.urlretrieve(attributes[key], filename)
                    attributes[key] = filename

if __name__ == "__main__":
    filename = take_filename()
    cHandler = KaraokeLocal(filename)
    print('\n' + cHandler.__str__() + '\n')
    cHandler.to_json(filename)
    cHandler.do_local()
    print('\n' + cHandler.__str__() + '\n')
