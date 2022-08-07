import pytest
import re

def test_something(host):
    file_exists = host.file('$HOME/.dotfiles/nvim/.config/nvim/init.lua')
    assert file_exists == True
