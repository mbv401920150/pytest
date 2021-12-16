import pytest

@pytest.mark.usefixtures("testOne")
def test_print_testOne(testOne, fixture_testTwo):
  print('----\nSIMPLE TEST TWO!\n----')
  print(testOne)
  print(testOne)
  print(fixture_testTwo)