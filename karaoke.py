#!/usr/bin/python3
# -*- coding: utf-8 -*-
import sys
from xml.sax import make_parser
from smallsmilhandler import SmallSMILHandler
from urllib.request import urlretrieve
import json


class KaraokeLocal():
    def __init__(self, filename):
        parser = make_parser()
        cHandler = SmallSMILHandler()
        parser.setContentHandler(cHandler)
        parser.parse(open(filename))
        self.list_tags = cHandler.get_tags()

    def __str__(self):
        string = ''
        for tag in self.list_tags:
            string += tag[0]  # tag[0], tag[1] are the tag name & attrs ditc
            string += ''.join('\t%s="%s"' % (key, value)
                              for key, value in tag[1].items() if value != '')
            string += '\n'
        return string.strip('\n')  # removes last \n

    def to_json(self, smile_file, json_file=''):
        if not json_file:
            json_file = smile_file.replace('.smil', '.json')
        with open(json_file, 'w') as outfile:
            json.dump(self.list_tags, outfile, sort_keys=True, indent=4)

    def do_local(self):
        attrs_dict = [tag[1] for tag in self.list_tags]
        for attrs in attrs_dict:
            if 'src' in attrs and 'http://' in attrs['src']:
                filename = attrs['src'].split('/')[-1]
                urlretrieve(attrs['src'], filename)
                attrs['src'] = filename


if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit("Usage:  python3 karaoke.py file.smil")
    filename = sys.argv[1]
    cHandler = KaraokeLocal(filename)
    print(cHandler)
    cHandler.to_json(filename)
    cHandler.do_local()
    cHandler.to_json(filename, 'local.json')
    print(cHandler)
