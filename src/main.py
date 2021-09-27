# Flashcard
from random import random


class FlashCard:


    def __init__(self):
        self.flashcards = {
            "terms": ['purchase', "cos'(x)"],
            "definitions": ['buy', '-sin(x)']
        }
        self.main()

    def main(self):
        # Main
        card = int(random() * len(self.flashcards['terms']))
        print(f"Card:\n{self.flashcards['terms'][card]}\nDefinition:\n{self.flashcards['definitions'][card]}")


flashcards = FlashCard()
