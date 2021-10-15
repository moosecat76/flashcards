# Flashcard

class TermExistError(Exception):
    def __init__(self, term):
        self.term = term

    def __str__(self):
        return f'The term "{self.term}" already exists. Try again:'


class DefinitionExistError(Exception):
    def __init__(self, definition):
        self.definition = definition

    def __str__(self):
        return f'The term "{self.definition}" already exists. Try again:'


class FlashCard:

    def __init__(self):
        self.flashcards = {
            'terms': [],
            'definitions': []
        }
        self.user_definition = ''
        self.n = 0

    def main(self):
        self.create_cards()
        for n in range(self.n):
            self.users_knowledge_test(n)

    def create_cards(self):
        self.n = int(input("Input the number of cards:\n"))
        for n in range(self.n):
            self.create_card(n)

    def create_card(self, n):
        self.define_term(n)
        self.define_definition(n)

    def define_term(self, n):
        valid_term = False
        term = input(f"The term for card #{n + 1}:\n")
        while valid_term is False:
            if self.check_term(term):
                print(TermExistError(term))
                term = input()
            else:
                self.flashcards['terms'].append(term)
                valid_term = True

    def define_definition(self, n):
        valid_definition = False
        definition = input(f"The definition for card #{n + 1}:\n")
        while valid_definition is False:
            if self.check_definition(definition):
                print(DefinitionExistError(definition))
                definition = input()
            else:
                self.flashcards['definitions'].append(definition)
                valid_definition = True

    def users_knowledge_test(self, n):
        term = self.flashcards['terms'][n]
        definition = self.flashcards['definitions'][n]
        self.user_definition = input(f"Print the definition of \"{term}\":\n")
        if definition == self.user_definition:
            return print("Correct!")
        if self.check_definition(self.user_definition):
            term = self.flashcards['terms'][self.flashcards['definitions'].index(self.user_definition)]
            return print(f"Wrong. The right answer is \"{definition}\", but your definition is correct for \"{term}\".")
        return print(f"Wrong. The right answer is \"{definition}\"")

    def check_term(self, term):
        return term in self.flashcards['terms']

    def check_definition(self, definition):
        return definition in self.flashcards['definitions']


if __name__ == "__main__":
    flashcards = FlashCard()
    flashcards.main()
