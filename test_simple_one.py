import pytest

def test_print_testOne(testOne, fixture_testTwo, global_data):
  print('----\nSIMPLE TEST ONE!\n----')
  print(testOne)
  print(testOne)
  print(fixture_testTwo)
  print('{} + {} = {}'.format(global_data.VarOne, global_data.VarTwo, global_data.Sum()))
  print('{} + {} = {}'.format(10, 5, global_data.Div(10, 5)))
  print('Global Variable: {}'.format(global_data.GlobalVal))
  assert global_data.GlobalVal == 10
  global_data.GlobalVal = 55
  assert global_data.GlobalVal == 55
  
  # Assert
  assert global_data.Div(10, 5) == 2.0