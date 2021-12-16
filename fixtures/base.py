import pytest

class ClientCredentials:
    def __init__(self, id, secret):
        self.id = id
        self.secret = secret

@pytest.fixture
def fixture_client():
    client_id = 'egBDAFEAMABSAEQAWwA9AFkAbQAhAFgAcwBjAGUAUgBrAEkAKwBQAHYAVQA3AC0AbQB9ACEATgBdAFQAVQBuAA'
    client_secret = ':y!u!/IHpKr@_~zkJP6vq.opp08Ps9fB'
    return ClientCredentials(client_id, client_secret)