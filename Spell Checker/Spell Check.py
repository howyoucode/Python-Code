from spellchecker import SpellChecker

class SpellCheckerApp:
    def __init__(self):
        self.spell = SpellChecker()

    def correct_text(self, text):
        words = text.split()
        corrected_words = []

        for word in words:
            corrected_word = self.spell.correction(word)
            # Ensure corrected_word is not None before adding it to the list
            if corrected_word and corrected_word != word.lower():
                corrected_words.append(corrected_word)
            elif corrected_word == word.lower():
                corrected_words.append("Already a corrected word!")
            else:
                corrected_words.append("Not a word!")
                
        return " ".join(corrected_words)
    
    def run(self):
        while True:
            word = input("Enter word to check or (x) to exit: ").lower()
            if word == "x":
                print("Exit!")
                break
            else:
                corrected_word = self.correct_text(word)
                print(f"Corrected text is: {corrected_word}")

if __name__ == "__main__":
    SpellCheckerApp().run()
