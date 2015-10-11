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

class KaraokeLocal(SmallSMILHandler):
    def __init__ (self, filename):
        parser = make_parser()
        cHandler = SmallSMILHandler()
        parser.setContentHandler(cHandler)
        parser.parse(open(filename))
        self.list_labels = cHandler.get_tags()


    def __str__ (self):
        str_label = ''
        for label in self.list_labels:
            str_label += label[0]
            for key, value in label[1].items():
                if value != '':
                    str_label += '\\%s="%s"\\n' % (key, value)
                    # str_label += '\\' + key + '=' + '"'+ value + '"' + '\\n'
            if label != self.list_labels[-1]:
                str_label += '\n'
        return str_label

    def to_json (self, smile_file, json_file = ''):
        if json_file == '':
            json_file = smile_file.split('.')[0] + '.json'
        data = json.dumps(self.list_labels)
        with open(json_file, 'w') as outfile:
            json.dump(data, outfile)

    def do_local (self):
        for label in self.list_labels:
            attributes = label[1]
            for key in attributes:
                if 'http://' in attributes[key]:
                    filename = attributes[key].split('/')[-1]
                    urllib.request.urlretrieve(attributes[key], filename)
                    attributes[key] = filename

if __name__ == "__main__":
    filename = take_filename()
    cHandler = KaraokeLocal(filename)
    print(cHandler.__str__())
    cHandler.to_json(filename)
    cHandler.do_local()
    print(cHandler.__str__())
