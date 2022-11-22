import pytest
from func_copy_and_filter.main import *


def test_copy_log():
    assert copy_passwd() == "Data passwd copied"
    assert copy_group() == "Data group copied"


def test_filter_users():
    assert filter_users() == 'true'


def test_filter_group():
    assert filter_group() == 'true-g'


