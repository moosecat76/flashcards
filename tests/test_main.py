from main import FlashCard


def gen_inputs_cc(three_cards):
    inputs = three_cards
    for in_ in inputs:
        yield in_


def test_create_cards(monkeypatch, three_cards):
    fc = FlashCard()
    card_to_create = gen_inputs_cc(three_cards)
    monkeypatch.setattr('builtins.input', lambda _: next(card_to_create))
    fc.create_cards()
    assert len(fc.flashcards['cards']) == 3
    assert fc.flashcards['cards'][0]['term'] == '1'
    assert fc.flashcards['cards'][0]['definition'] == 'one'
    assert fc.flashcards['cards'][1]['term'] == '2'
    assert fc.flashcards['cards'][1]['definition'] == 'two'
    assert fc.flashcards['cards'][2]['term'] == '3'
    assert fc.flashcards['cards'][2]['definition'] == 'three'


def gen_inputs(inputs):
    for in_ in inputs:
        yield in_


def test_create_card(monkeypatch, card_valid):
    fc = FlashCard()
    term = card_valid['term']
    definition = card_valid['definition']
    gen = gen_inputs([term, definition])
    monkeypatch.setattr('builtins.input', lambda _: next(gen))
    fc.create_card(1)
    assert len(fc.flashcards['cards']) == 1
    assert fc.flashcards['cards'][0]['term'] == 'print()'
    assert fc.flashcards['cards'][0]['definition'] == 'outputs text'


def test_user_inputs_kt(monkeypatch, card_valid):
    fc = FlashCard()
    term = card_valid['term']
    definition = card_valid['definition']
    monkeypatch.setattr('builtins.input', lambda _: definition)
    card = {'term': term, 'definition': definition}
    fc.flashcards['cards'].append(card)
    fc.users_knowledge_test(0)
    assert fc.flashcards['cards'][0]['definition'] == fc.user_definition


