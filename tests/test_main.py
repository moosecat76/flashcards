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
    assert len(fc.flashcards['terms']) == 3
    assert fc.flashcards['terms'][0] == '1'
    assert fc.flashcards['definitions'][0] == 'one'
    assert fc.flashcards['terms'][1] == '2'
    assert fc.flashcards['definitions'][1] == 'two'
    assert fc.flashcards['terms'][2] == '3'
    assert fc.flashcards['definitions'][2] == 'three'
    del(fc)



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
    assert len(fc.flashcards['terms']) == 1
    assert fc.flashcards['terms'][0] == 'print()'
    assert fc.flashcards['definitions'][0] == 'outputs text'
    del(fc)

def test_user_inputs_kt(monkeypatch, card_valid):
    fc = FlashCard()
    term = card_valid['term']
    definition = card_valid['definition']
    monkeypatch.setattr('builtins.input', lambda _: definition)
    fc.flashcards['terms'].append(term)
    fc.flashcards['definitions'].append(definition)
    fc.users_knowledge_test(0)
    assert fc.flashcards['definitions'][0] == fc.user_definition
    del(fc)

def test_check_term(monkeypatch, three_cards):
    fc = FlashCard()
    card_to_create = gen_inputs_cc(three_cards)
    monkeypatch.setattr('builtins.input', lambda _: next(card_to_create))
    fc.create_cards()
    result = fc.check_term(fc.flashcards['terms'][2])
    assert result is True
    del(fc)

def test_check_definition(monkeypatch, three_cards):
    fc = FlashCard()
    card_to_create = gen_inputs_cc(three_cards)
    monkeypatch.setattr('builtins.input', lambda _: next(card_to_create))
    fc.create_cards()
    result = fc.check_definition(fc.flashcards['definitions'][2])
    assert result is True
    del(fc)

def test_check_term_false(monkeypatch, three_cards):
    fc = FlashCard()
    card_to_create = gen_inputs_cc(three_cards)
    monkeypatch.setattr('builtins.input', lambda _: next(card_to_create))
    fc.create_cards()
    result = fc.check_term('Really should not match')
    assert result is False
    del(fc)

def test_check_definition_false(monkeypatch, three_cards):
    fc = FlashCard()
    card_to_create = gen_inputs_cc(three_cards)
    monkeypatch.setattr('builtins.input', lambda _: next(card_to_create))
    fc.create_cards()
    result = fc.check_definition('Really should not match')
    assert result is False
    del(fc)