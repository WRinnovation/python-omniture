# encoding: utf-8
from __future__ import absolute_import
from __future__ import print_function

import copy
import logging

from .import utils


class Value(object):
    """ Searchable Dict. Can search on both the key and the value """
    def __init__(self, title, id, parent, extra={}):
        self.log = logging.getLogger(__name__)
        self.title = unicode(title)
        self.id = id
        self.parent = parent
        self.properties = {'id': id}

        for k, v in extra.items():
            setattr(self, k, v)

    @classmethod
    def list(cls, name, items, parent, title='title', id='id'):
        values = [cls(item[title], unicode(item[id]), parent, item) for item in items]
        return utils.AddressableList(values, name)

    def __repr__(self):
        print(self)
        return "<{title}: {id} in {parent}>".format(**self.__dict__)

    def copy(self):
        value = self.__class__(self.title, self.id, self.parent)
        value.properties = copy.copy(self.properties)
        return value

    def serialize(self):
        return self.properties

    def _repr_html_(self):
        """ Format in HTML for iPython Users """
        return "<td><b>{0}</b></td><td>{1}</td>".format(self.id, self.title)


    def __str__(self):
        """ allows users to print this out in a user friendly using print
        """
        return "ID {0:25} | Name: {1} \n".format(self.id, self.title)
