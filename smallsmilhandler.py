#!/usr/bin/python3
# -*- coding: utf-8 -*-

from xml.sax import make_parser
from xml.sax.handler import ContentHandler

class SmallSMILHandler(ContentHandler):
    def __init__ (self):
        self.list_labels = []
        root_layout = {'width': '', 'height': '', 'background-color': ''}
        region = {'id': '', 'top': '', 'bottom': '', 'left': '', 'right': ''}
        img = {'src': '', 'region': '', 'begin': '', 'dur': ''}
        audio = {'src': '', 'begin': '', 'dur': ''}
        textstream = {'src': '', 'region': ''}
        self.labels = {'root-layout': root_layout, 'region': region,'img': img,
                       'audio': audio, 'textstream': textstream}


    def startElement(self, name, attrs):
        if name in self.labels:
            # if name == 'region':
                my_dict = {}
                for key in self.labels[name].keys():
                    # if 'src'in self.labels[name]:
                        my_dict[key] = attrs.get(key, "")
                self.list_labels.append([name, my_dict])

    def get_tags(self):
        return self.list_labels

if __name__ == '__main__':
    filename = sys.argv[1]
    parser = make_parser()
    cHandler = SmallSMILHandler()
    parser.setContentHandler(cHandler)
    parser.parse(open(filename))
