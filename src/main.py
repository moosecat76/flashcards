# Flashcard


class FlashCard:

    def __init__(self):
        self.flashcards = {
            'cards': []  # {'term':t, 'definition': d}
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
        term = input(f"The term for card #{n+1}:\n")
        definition = input(f"The definition for card #{n+1}:\n")
        card = {'term': term, 'definition': definition}
        self.flashcards['cards'].append(card)
        return

    def users_knowledge_test(self, n):
        term = self.flashcards['cards'][n]['term']
        definition = self.flashcards['cards'][n]['definition']
        self.user_definition = input(f"Print the definition of \"{term}\":\n")
        if definition == self.user_definition:
            print("Correct!")
        else:
            print(f"Wrong. The right answer is \"{definition}\"")
        return


if __name__ == "__main__":
    flashcards = FlashCard()
    flashcards.main()
