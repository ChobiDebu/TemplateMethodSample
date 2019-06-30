# -*- coding: utf-8 -*-

from abc import ABCMeta, abstractmethod


class AbstractTask(metaclass=ABCMeta):

    def __init__(self, title, text_list):
        self.title = title
        self.text_list = text_list

    @abstractmethod
    def pprint(self):
        pass

    @abstractmethod
    def start(self):
        pass

    @abstractmethod
    def end(self):
        pass

    def display(self):
        self.start()
        self.pprint()
        self.end()
