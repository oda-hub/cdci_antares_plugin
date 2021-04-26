
from __future__ import absolute_import, division, print_function

from builtins import (bytes, str, open, super, range,
                      zip, round, input, int, pow, object, map, zip)

__author__ = 'andrea tramacere'




#!/usr/bin/env python

from setuptools import setup, find_packages
import  glob



f = open("./requirements.txt",'r')
install_req=f.readlines()
f.close()


packs=find_packages()

print ('packs',packs)




include_package_data=True

scripts_list=glob.glob('./bin/*')
setup(name='dispatcher_plugin_antares',
      version=1.0,
      description='ANTARES plugin  for CDCI online data analysis',
      author='Andrea Tramacere',
      author_email='andrea.tramacere@unige.ch',
      scripts=scripts_list,
      packages=packs,
      package_data={'dispatcher_plugin_antares':['config_dir/*']},
      include_package_data=True,
      install_requires=install_req,
)



