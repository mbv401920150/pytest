import pytest
import requests
import json

def test_getOneItem(globalOmbd):
  x = globalOmbd.generateQuery('Schindler\'s+List')
  print(x)
  result = requests.get(x)
  jsonRes = result.json()
  print('Result: {}'.format(jsonRes))
  print(jsonRes['Title'])