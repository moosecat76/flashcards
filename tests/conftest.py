from main import *
import pytest


@pytest.fixture
def card_valid():
    term = 'print()'
    definition = 'outputs text'
    return {'term': term, 'definition': definition}


@pytest.fixture
def card_valid1():
    term = '1'
    definition = 'one'
    return {'term': term, 'definition': definition}


@pytest.fixture
def card_valid2():
    term = '2'
    definition = 'two'
    return {'term': term, 'definition': definition}


@pytest.fixture
def card_valid3():
    term = '3'
    definition = 'three'
    return {'term': term, 'definition': definition}


@pytest.fixture
def three_cards(card_valid1, card_valid2, card_valid3):
    r = [3, card_valid1['term'], card_valid1['definition'], card_valid2['term'], card_valid2['definition'], card_valid3['term'], card_valid3['definition']]
    return r


