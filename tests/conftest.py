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


@pytest.fixture
def menu_add():
    return ['add', 'term1', 'definition1', 'exit']


@pytest.fixture
def menu_remove():
    return ['remove', '1', 'exit']


@pytest.fixture
def menu_import():
    return ['import', 'cards.txt', 'exit']


@pytest.fixture
def menu_export():
    return ['export', 'cards.txt', 'exit']


@pytest.fixture
def menu_ask():
    return ['add', 'term2', 'definition2', 'ask', '1', 'term2', 'definition2', 'exit']


@pytest.fixture
def menu_exit():
    return ['exit']

@pytest.fixture
def test_2():
    add1 = ['add', 'cat', 'meow', 'add', 'cat', 'dog', 'meow', 'woof']
    ask1 = ['ask', '2', 'meow', 'meow']
    remove = ['remove', 'badger', 'remove', 'cat']
    add2 = ['add', 'horse', 'neigh']
    export = ['export', 'animal_sounds.txt']
    load = ['import', 'animal_sounds.txt']
    ask = ['ask', '4']
    entries = []
    for i in range(4):
        q = f"question{i}"
        a = "neigh"
        entries.append(q)
        entries.append(a)

    return add1 + ask1 + remove + add2 + export + load + entries + ["exit"]
