class NegativeValueError(Exception):    pass


class DataClassifier:
    def classify(self, value):
        """
        Klasyfikuje wartość liczbową:
        - < 30  => "Niska wartość"
        - 30-70 => "Średnia wartość"
        - > 70  => "Wysoka wartość"

        Rzuca wyjątki:
        - TypeError, jeśli value nie jest liczbą (int lub float).
        - NegativeValueError, jeśli wartość jest ujemna.
        """
        if not isinstance(value, (int, float)):
            raise TypeError("Wartość musi być liczbą (int lub float).")

        if value < 0:
            raise NegativeValueError("Wartość nie może być ujemna.")

        if value < 30:
            return "Niska wartość"
        elif value <= 70:
            return "Średnia wartość"
        else:
            return "Wysoka wartość"


if __name__ == "__main__":
    classifier = DataClassifier()

    try:
        print(classifier.classify(50))
        print(classifier.classify(100))

        print(classifier.classify(-10))

    except NegativeValueError as e:
        print("Błąd (NegativeValueError):", e)

    except TypeError as e:
        print("Błąd (TypeError):", e)

    try:
        print(classifier.classify("abc"))
    except TypeError as e:
        print("Błąd (TypeError):", e)
