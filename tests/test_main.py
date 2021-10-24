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
    del (fc)


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
    del (fc)


def test_user_inputs_kt(monkeypatch, card_valid):
    fc = FlashCard()
    term = card_valid['term']
    definition = card_valid['definition']
    monkeypatch.setattr('builtins.input', lambda _: definition)
    fc.flashcards['terms'].append(term)
    fc.flashcards['definitions'].append(definition)
    fc.users_knowledge_test(0)
    assert fc.flashcards['definitions'][0] == fc.user_definition
    del (fc)


def test_check_term(monkeypatch, three_cards):
    fc = FlashCard()
    card_to_create = gen_inputs_cc(three_cards)
    monkeypatch.setattr('builtins.input', lambda _: next(card_to_create))
    fc.create_cards()
    result = fc.check_element(fc.flashcards['terms'][2], 'terms')[0]
    assert result is True
    del (fc)


def test_check_definition(monkeypatch, three_cards):
    fc = FlashCard()
    card_to_create = gen_inputs_cc(three_cards)
    monkeypatch.setattr('builtins.input', lambda _: next(card_to_create))
    fc.create_cards()
    result = fc.check_element(fc.flashcards['definitions'][2], 'definitions')[0]
    assert result is True
    del (fc)


def test_check_term_false(monkeypatch, three_cards):
    fc = FlashCard()
    card_to_create = gen_inputs_cc(three_cards)
    monkeypatch.setattr('builtins.input', lambda _: next(card_to_create))
    fc.create_cards()
    result = fc.check_element('Really should not match', 'terms')[0]
    assert result is False
    del (fc)


def test_check_definition_false(monkeypatch, three_cards):
    fc = FlashCard()
    card_to_create = gen_inputs_cc(three_cards)
    monkeypatch.setattr('builtins.input', lambda _: next(card_to_create))
    fc.create_cards()
    result = fc.check_element('Really should not match', 'definitions')[0]
    assert result is False
    del (fc)


def test_menu_add(monkeypatch, menu_add):
    fc = FlashCard()
    gen = gen_inputs(menu_add)
    monkeypatch.setattr('builtins.input', lambda _: next(gen))
    fc.menu()
    assert len(fc.flashcards['terms']) == 1
    assert fc.flashcards['terms'][0] == 'term1'
    assert fc.flashcards['definitions'][0] == 'definition1'
    del (fc)


def test_menu_remove(monkeypatch, three_cards, menu_remove):
    fc = FlashCard()
    card_to_create = gen_inputs_cc(three_cards)
    monkeypatch.setattr('builtins.input', lambda _: next(card_to_create))
    fc.create_cards()
    gen = gen_inputs(menu_remove)
    monkeypatch.setattr('builtins.input', lambda _: next(gen))
    fc.menu()
    assert len(fc.flashcards['terms']) == 2
    assert fc.flashcards['terms'][0] == '2'
    assert fc.flashcards['definitions'][0] == 'two'
    assert fc.flashcards['terms'][1] == '3'
    assert fc.flashcards['definitions'][1] == 'three'
    del (fc)


def test_menu_export(monkeypatch, capsys, three_cards, menu_export):
    fc = FlashCard()
    assert len(fc.flashcards['terms']) == 0
    card_to_create = gen_inputs_cc(three_cards)
    monkeypatch.setattr('builtins.input', lambda _: next(card_to_create))
    fc.create_cards()
    assert len(fc.flashcards['terms']) == 3
    assert fc.flashcards['terms'][0] == '1'
    assert fc.flashcards['definitions'][0] == 'one'
    gen = gen_inputs(menu_export)
    monkeypatch.setattr('builtins.input', lambda _: next(gen))
    fc.menu()
    captured = capsys.readouterr()
    assert captured.out == "3 cards have been saved.\nBye bye!\n"
    del (fc)


def test_menu_import(monkeypatch, capsys, menu_import):
    fc = FlashCard()
    gen = gen_inputs(menu_import)
    monkeypatch.setattr('builtins.input', lambda _: next(gen))
    fc.menu()
    captured = capsys.readouterr()
    assert captured.out == "3 cards have been loaded.\nBye bye!\n"
    assert len(fc.flashcards['terms']) == 3
    assert fc.flashcards['terms'][0] == '1'
    assert fc.flashcards['definitions'][0] == 'one'
    del (fc)

def test_menu_ask(monkeypatch, menu_ask):
    fc = FlashCard()
    gen = gen_inputs(menu_ask)
    monkeypatch.setattr('builtins.input', lambda _: next(gen))
    fc.menu()
    assert len(fc.flashcards['terms']) == 1
    assert fc.flashcards['terms'][0] == 'term2'
    assert fc.flashcards['definitions'][0] == 'definition2'
    del (fc)

def test_menu_exit(monkeypatch, capsys, menu_exit):
    fc = FlashCard()
    gen = gen_inputs(menu_exit)
    monkeypatch.setattr('builtins.input', lambda _: next(gen))
    fc.menu()
    captured = capsys.readouterr()
    assert captured.out == "Bye bye!\n"
    del (fc)

def test_case_2(monkeypatch, capsys, test_2):
    fc = FlashCard()
    gen = gen_inputs(test_2)
    monkeypatch.setattr('builtins.input', lambda _: next(gen))
    fc.menu()
    captured = capsys.readouterr()
    assert captured.out == "Bye bye!\n"
    del (fc)

