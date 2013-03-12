import setuptools
from setuptools import find_packages


class SetupTrapper(object):
    def __init__(self):
        self.kwargs = {}
        self.args = ()

    def get_data(self):
        return (self.args, self.kwargs)

    def __call__(self, *args, **kwargs):
        self.kwargs = kwargs
        self.args = args

def trap_setup():
    """
    Monkey Patch setuptools to use the SetupTrapper class which lets us
    capture all the arguments given to it. This function returns a tuple
    of the args, and keyword args given to the setup function in a setup.py
    file.
    """
    trapper = SetupTrapper()
    setuptools.setup = trapper
    __import__("setup",globals(),locals(),[],-1)
    return trapper.get_data()

