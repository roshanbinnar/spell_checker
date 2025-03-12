from spellchecker import Spellchecker
class SpellCheckerApp():
    def __int__(self):
        self.spell = Spellchecker()

    def corect_text(self,text):
        words = text.split()
        corrected_words = []

        for word in words:
            corrected_word = self.spell.correction(word)
            if corrected_word != word.lower():
                print(f"Correting {word} to {corrected_word}")
                corrected_words.append(corrected_word)
        return " ".join(corrected_words)

    def run(self):
        print("SPELL CHECKER")
        while True:
            text = input("Enter the text to check or type exit to quite")

            if text.lower() == "exit":
                print("CLOSING THE PROGRAMME")
                break
            corrected_text = self.corect_text(text)
            print(f"corrected_text : {corrected_text}")

if __name__ == "__main__":
    obj = SpellCheckerApp()
    obj.run()

