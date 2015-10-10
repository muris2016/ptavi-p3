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
def show_smil(list_labels):
    for label in list_labels:
        label_name = label[0]
        attributes = label[1]
        sys.stdout.write(label_name + '\\')
        for key, value in attributes.items():
            if value != '':
                # sys.stdout.write('%s="%s"\\' % (key, value))
                sys.stdout.write(key + '=' + '"'+ value + '"' + '\\')
        print('n')

def do_json_file(list_labels):

    data = json.dumps(list_labels)
    with open('labels.json', 'w') as outfile:
        json.dump(data, outfile)

def get_url(list_labels):
    for label in list_labels:
        attributes = label[1]
        for key in attributes:
            if 'http://' in attributes[key]:
                filename = attributes[key].split('/')[-1]
                urllib.request.urlretrieve(attributes[key], filename)
                attributes[key] = filename

if __name__ == "__main__":
    filename = take_filename()
    parser = make_parser()
    cHandler = SmallSMILHandler()
    parser.setContentHandler(cHandler)
    parser.parse(open(filename))
    list_labels = cHandler.get_tags()
    do_json_file(list_labels)
    get_url(list_labels)
    show_smil(list_labels)
