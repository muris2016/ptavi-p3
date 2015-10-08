#!/usr/bin/python3
# -*- coding: utf-8 -*-

from xml.sax import make_parser
from xml.sax.handler import ContentHandler

class SmallSMILHandler(ContentHandler):
    def __init__ (self):
        self.labels = []
        self.set_labels()
        self.attributes = {'root-layout': self.root_layout,
                           'region': self.region,
                           'img': self.img,
                           'audio': self.audio,
                           'textstream': self.textstream}

    def set_labels(self):
        self.root_layout = {'width': '', 'height': '', 'background-color': ''}
        self.region = {'id': '', 'top': '', 'bottom': '', 'left': '', 'right': ''}
        self.img = {'src': '', 'region': '', 'begin': '', 'dur': ''}
        self.audio = {'src': '', 'begin': '', 'dur': ''}
        self.textstream = {'src': '', 'region': ''}

    def startElement(self, name, attrs):
        if name in self.attributes:
            self.set_labels()
            self.labels.append(name)
            for key, value in self.attributes[name].items():
                self.attributes[name][key] = attrs.get(key,'')
            self.labels.append(self.attributes[name])

    def get_tags(self):
        for i in self.labels:
            try:
                for key, value in i.items():
                    print("   %s : %s" % (key, value))
                print('')
            except AttributeError:
                print(i)

    def endElement(self, name):
        pass
    def characters(self, char):
        pass

if __name__ == '__main__':
    parser = make_parser()
    cHandler = SmallSMILHandler()
    parser.setContentHandler(cHandler)
    parser.parse(open('karaoke.smil'))
    cHandler.get_tags()
