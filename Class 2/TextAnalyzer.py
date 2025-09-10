from transformers import pipeline


class TextAnalyzer:
    def word_count(self, text):
        words = text.split()
        return len(words)

    def char_count(self, text):
        return len(text)

    def unique_words(self, text):
        words = text.lower().split()
        unique_words_set = set(words)
        return len(unique_words_set)


class AdvancedTextAnalyzer(TextAnalyzer):
    def sentiment_analysis(self, text):
        pozytywne = ["wspaniały", "świetny", "dobry", "szczęśliwy", "fantastyczny"]
        negatywne = ["okropny", "zły", "smutny", "straszny", "fatalny"]

        words = text.lower().split()

        pozytywne_count = sum(word in pozytywne for word in words)
        negatywne_count = sum(word in negatywne for word in words)

        if pozytywne_count > negatywne_count:
            return "Pozytywny"
        elif negatywne_count > pozytywne_count:
            return "Negatywny"
        else:
            return "Neutralny"


if __name__ == "__main__":
    # Przykładowy tekst do analizy
    test_text = ("To był naprawdę wspaniały dzień!")

    analyzer = AdvancedTextAnalyzer()

    sentiment_pipeline = pipeline("sentiment-analysis")
    data = ["I love you", "I hate you"]
    print(sentiment_pipeline(data))

    # print("Tekst:", test_text)
    # print("Liczba słów:", analyzer.word_count(test_text))
    # print("Liczba znaków:", analyzer.char_count(test_text))
    # print("Liczba unikalnych słów:", analyzer.unique_words(test_text))
    # print("Sentyment:", analyzer.sentiment_analysis(test_text))
