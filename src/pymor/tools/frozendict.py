# This file is part of the pyMor project (http://www.pymor.org).
# Copyright Holders: Felix Albrecht, Rene Milk, Stephan Rave
# License: BSD 2-Clause License (http://opensource.org/licenses/BSD-2-Clause)

from __future__ import absolute_import, division, print_function


# The following implementation is based on
# http://code.activestate.com/recipes/414283-frozen-dictionaries/


class FrozenDict(dict):

    @property
    def _blocked_attribute(obj):
        raise AttributeError, "A frozendict cannot be modified."

    __delitem__ = __setitem__ = clear = _blocked_attribute
    pop = popitem = setdefault = update = _blocked_attribute

    def __new__(cls, *args, **kwargs):
        new = dict.__new__(cls)
        dict.__init__(new, *args, **kwargs)
        return new

    def __init__(self, *args, **kwargs):
        pass

    def __repr__(self):
        return "FrozenDict({})".format(dict.__repr__(self))
