#!/usr/bin/env python
import requests
from subprocess import Popen
import json
import os
import inflect
p = inflect.engine()


c_dir = os.path.dirname(os.path.realpath(__file__))
config = json.load(open(c_dir + '/config.json'))

for team in config['teams']:
  x = json.loads(requests.get('https://ctftime.org/api/v1/teams/%d/' % team['id']).text)

  rating = x['rating'][0]
  rating = rating[rating.keys()[0]]
  message = '%s: %s (%f)' % (x['name'], p.ordinal(rating['rating_place']), rating['rating_points'])
  print message

