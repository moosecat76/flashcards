# Flashcard
import random

class ExistError(Exception):
    def __init__(self, element, element_value):
        self.element = element
        self.element_value = element_value

    def __str__(self):
        if self.element == "terms":
            return f'The card "{self.element_value}" already exists. Try again:'
        else:
            return f'The definition "{self.element_value}" already exists. Try again:'

class FlashCard:

    def __init__(self):
        self.flashcards = {
            'terms': [],
            'definitions': []
        }
        self.user_definition = ''
        self.n = 0

    def main(self):
        self.menu()
        # for n in range(self.n):
        #       self.users_knowledge_test(n)

    def menu(self):
        flashcard_game = True
        while flashcard_game is True:
            choice = input("Input the action (add, remove, import, export, ask, exit):\n")
            if choice.lower() == "add":
                self.add_card()
            if choice.lower() == "remove":
                self.remove_card()
            if choice.lower() == "import":
                self.import_cards()
            if choice.lower() == "export":
                self.export_cards()
            if choice.lower() == "ask":
                self.ask()
            if choice.lower() == "exit":
                flashcard_game = self.exit_cards()
            # print("\n")

    def create_cards(self):
        self.n = int(input("Input the number of cards:\n"))
        for n in range(self.n):
            self.create_card(n)

    def create_card(self, n):
        return self.define_element(n, 'terms'), self.define_element(n, 'definitions')

    def define_element(self, n, element):
        valid_element = False
        if element == "terms":
            element_value = input(f"The card:\n")
        else:
            element_value = input(f"The definition of the card:\n")
        while valid_element is False:
            if self.check_element(element_value, element)[0] is True:
                print(ExistError(element, element_value))
                element_value = input("")
            else:
                self.flashcards[element].append(element_value)
                valid_element = True
                return element_value

    def users_knowledge_test(self, element_value):
        n = self.check_element(element_value, "terms")[1]
        term = self.flashcards['terms'][n]
        definition = self.flashcards['definitions'][n]
        self.user_definition = input(f"Print the definition of \"{term}\":\n")
        if definition == self.user_definition:
            return print("Correct!")
        if self.check_element(self.user_definition, 'definitions')[0] is True:
            term = self.flashcards['terms'][self.flashcards['definitions'].index(self.user_definition)]
            return print(f"Wrong. The right answer is \"{definition}\", but your definition is correct for \"{term}\"")
        return print(f"Wrong. The right answer is \"{definition}\"")

    def check_element(self, element_value, element):
        if element_value in self.flashcards[element]:
            return True, self.flashcards[element].index(element_value)
        else:
            return False, -1


    def add_card(self):
        term, definition = self.create_card(1)
        return print(f"The pair (\"{term}\":\"{definition}\") has been added.\n")

    def remove_card(self):
        card_to_remove = input("Which card?\n")
        result, card_id = self.check_element(card_to_remove, "terms")
        if result is True:
            self.flashcards['terms'].pop(card_id)
            self.flashcards['definitions'].pop(card_id)
            return print("The card has been removed.\n")
        else:
            return print(f"Can't remove \"{card_to_remove}\": there is no such card\n")

    def import_cards(self):
        file_name = input("File name:\n")
        try:
            import_file = open(file_name, "r", encoding="utf-8")
        except OSError as error:
            print("File not found.\n")
            return
        lines = import_file.readlines()
        n = 0
        for line in reversed(lines):
            term, definition = line.split(":")
            result, card_id = self.check_element(term, "terms")
            if result:
                self.flashcards['terms'][card_id] = term
                self.flashcards['definitions'][card_id] = definition.strip()
            else:
                self.flashcards['terms'].insert(0, term)
                self.flashcards['definitions'].insert(0, definition.strip())
            n += 1
        import_file.close()
        return print(f"{n} cards have been loaded.")

    def export_cards(self):
        file_name = input("File name:\n")
        export_file = open(file_name, "w", encoding="utf-8")
        n = 0
        for term, definition in zip(self.flashcards['terms'], self.flashcards['definitions']):
            line = f"{term}:{definition}\n"
            export_file.write(line)
            n += 1
        export_file.close()
        return print(f"{n} cards have been saved.")

    def ask(self):
        n = int(input("How many times to ask?\n"))
        total_cards = len(self.flashcards['terms'])
        if n > total_cards:
            try:
                m = n // total_cards
            except ZeroDivisionError as error:
                print("There a no cards loaded")
                return
        else:
            m = 0
        big_list = self.flashcards['terms'] * (m + 1)
        for i, term in enumerate(big_list[:n]):
            # self.users_knowledge_test(random.choice(range(total_cards)))
            self.users_knowledge_test(term)

    def exit_cards(self):
        print("Bye bye!")
        return False


if __name__ == "__main__":
    flashcards = FlashCard()
    flashcards.main()
