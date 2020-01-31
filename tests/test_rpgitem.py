import pytest
from rpg_namer import RPGItems


def test_random():
    item = RPGItems().random_item()
    assert item != ''


def test_random_helm():
    item = RPGItems('helmet').random_item()
    assert item != ''


def test_random_body():
    item = RPGItems('body').random_item()
    assert item != ''


def test_random_legs():
    item = RPGItems('legs').random_item()
    assert item != ''


def test_random_boots():
    item = RPGItems('boots').random_item()
    assert item != ''


def test_random_shield():
    item = RPGItems('shield').random_item()
    assert item != ''


def test_random_gauntlets():
    item = RPGItems('gauntlets').random_item()
    assert item != ''


def test_custom_items():
    item = RPGItems(items=['A1B2C3D4']).random_item()
    assert 'A1B2C3D4' in item

