import pytest

class globalData:
  def __init__(self):
    self.VarOne = 4
    self.VarTwo = 7
    self.Sum = lambda : self.VarOne + self.VarTwo
    self.Div = lambda x, y : x / y

@pytest.fixture(scope='session')
def global_data():
  return globalData()