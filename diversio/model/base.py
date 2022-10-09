import os
import importlib
import inspect
import diversio.model
from diversio.utils import _dict


class Base(object):
    def __init__(self, d):
        self.update(d)

    def update(self, d):
        for key, value in d.items():
            self.set(key, value)

        return self

    def set(self, key, value, as_value=False):
        loader = importlib.util.find_spec(
            "diversio.model.{0}".format(key))
        if loader:
            mod = importlib.import_module(loader.name)
            c = getattr(mod, key.capitalize())
            value = c(value)
            self.__dict__[key] = value
        else:
            if isinstance(value, dict):
                self.__dict__[key] = _dict(value)
            else:
                self.__dict__[key] = value

    def append(self, key, value=None):
        if value is None:
            value = {}
        if isinstance(value, (dict, Base)):
            if not self.__dict__.get(key):
                self.__dict__[key] = []

            self.__dict__[key].append(value)
        else:
            raise ValueError(
                "Base "
            )

    def extend(self, key, value):
        if isinstance(value, list):
            for v in value:
                self.append(key, v)
        else:
            raise ValueError
