#!/usr/bin/python
# coding: utf-8

"""
Code for getting data from different sources using SunPy's VSO client and saving them into the specified directory.
"""

from sunpy.net import vso

data_client = vso.VSOClient()

data_query = data_client.query(vso.attrs.Time('2012/1/1', '2012/1/2'), vso.attrs.Instrument('eit'))

print(len(data_query))

data = data_client.get(data_query, path='/home/ivan/projects/Physics/solar/solar-physics-ex/data/{file}.fits').wait()