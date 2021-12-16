import pytest

@pytest.mark.usefixtures("testOne")
def test_print_testOne(testOne, fixture_testTwo, global_data):
  print('----\nSIMPLE TEST TWO!\n----')
  print(testOne)
  print(testOne)
  print(fixture_testTwo)
  
  # The global_data fixture is session's scoped 
  # Was changed in the simple_one.py file
  print('Global Variable: {}'.format(global_data.GlobalVal))
  assert global_data.GlobalVal == 55