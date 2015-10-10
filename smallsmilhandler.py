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
            my_dict = self.labels[name]
            for key in my_dict.keys():
                my_dict[key] = attrs.get(key, "")
            self.list_labels.append([name, my_dict])

    def get_tags(self):
        return self.list_labels
