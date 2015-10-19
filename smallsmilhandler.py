#!/usr/bin/python3
# -*- coding: utf-8 -*-

from xml.sax.handler import ContentHandler


class SmallSMILHandler(ContentHandler):
    def __init__(self):
        root_layout = {'width': '', 'height': '', 'background-color': ''}
        region = {'id': '', 'top': '', 'bottom': '', 'left': '', 'right': ''}
        img = {'src': '', 'region': '', 'begin': '', 'dur': ''}
        audio = {'src': '', 'begin': '', 'dur': ''}
        textstream = {'src': '', 'region': ''}
        self.labels = {'root-layout': root_layout, 'region': region,
                       'img': img, 'audio': audio, 'textstream': textstream}
        self.list_labels = []

    def startElement(self, name, attrs):
        if name in self.labels:
            my_dict = {key: attrs.get(key, '') for key in self.labels[name]}
            self.list_labels.append([name, my_dict])

    def get_tags(self):
        return self.list_labels
