import pytest

# Read all fixtures from the following files
# We change the / for . to define folders and subfolders
# It's not required specify manually all fixtures 
pytest_plugins = [
    "fixtures.global",
    "fixtures.simple",
    "fixtures.base"
]