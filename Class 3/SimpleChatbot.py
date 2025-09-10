from typing import List, Iterator


class SimpleChatbot:
    def __init__(self, questions: List[str]) -> None:
        self.questions = questions
        self.index = 0

    def __iter__(self) -> Iterator[str]:
        return self

    def __next__(self) -> str:
        if self.index < len(self.questions):
            question = self.questions[self.index]
            self.index += 1
            return question
        else:
            raise StopIteration


if __name__ == "__main__":
    bot = SimpleChatbot(["Jak się nazywasz?", "Jaki jest Twój ulubiony kolor?"])
    for question in bot:
        print(question)
        input("Twoja odpowiedź: ")
