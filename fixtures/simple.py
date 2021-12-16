import pytest

# You must include the decoration to Pytest know a method is a fixture.
# We can define a fixture with scope = session (So only will runs once in all tests)

# Check this section to know more about the Scope:
# https://docs.pytest.org/en/latest/how-to/fixtures.html#scope-sharing-fixtures-across-classes-modules-packages-or-session
# https://docs.pytest.org/en/latest/how-to/fixtures.html#fixture-scopes

@pytest.fixture
def testOne():
  print('\n** TEST ONE FIXTURE IS RUNNING **')
  return 'TEST #1'

@pytest.fixture(scope="session")
def fixture_testTwo():
  print('** TEST TWO FIXTURE IS RUNNING **')
  return 'Test #2'