# Flashcard


class FlashCard:

    def __init__(self):
        self.flashcards = {
            "terms": ['purchase', "cos'(x)"],
            "definitions": ['buy', '-sin(x)']
        }
        self.user_definition = ''

    def main(self):
        term = input()
        definition = input()
        self.user_definition = input()
        if definition == self.user_definition:
            print("Your answer is right!")
        else:
            print("Your answer is wrong...")

    def show_term(self):
        pass

    def show_definition(self):
        pass


flashcards = FlashCard()
flashcards.main()
