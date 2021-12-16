import pytest

class globalData:
  def __init__(self):
    self.VarOne = 4
    self.VarTwo = 7
    self.GlobalVal = 10
    self.Sum = lambda : self.VarOne + self.VarTwo
    self.Div = lambda x, y : x / y

class GlobalOmbd:
  def __init__(self):
    self.url = "http://www.omdbapi.com/"
    self.apiKey = "787f6d45"
    self.generateQuery = lambda title: '{}?t={}&apiKey={}'.format(self.url, title, self.apiKey)

@pytest.fixture(scope='session')
def global_data():
  return globalData()

@pytest.fixture(scope='session')
def globalOmbd():
  return GlobalOmbd()
