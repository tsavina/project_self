from random import randint

class Human:
    def __init__(self, name):
        self.name = name
    # ответ по умолчанию для всех одинаковый, можно
    # доверить его родительскому классу
    def answer_question(self, question):
        if question.lower() in  ["как твое имя"]:
            return f"{self}> " + self.get_name()
        elif "погод" in question.lower():
            return self.get_weather()
        return f"{self}> Очень интересный вопрос! Не знаю."

    def get_name(self):
        return self.name

    def __str__(self):
        return "Человек"

    def get_weather(self):
        return f"{self}>  Не знаю."

class Student(Human):
    #  метод ask_question() принимает параметр someone:
    #  это объект, экземпляр класса Curator, Mentor или CodeReviewer,
    #  которому Student задаёт вопрос;
    #  параметр question — это просто строка
    #  имя объекта и текст вопроса задаются при вызове метода ask_question
    def ask_question(self, someone, question):
        # напечатайте на экран вопрос в нужном формате
        return f"{self}> {someone.name}, {question}\n" + someone.answer_question(question) + "\n"
        # запросите ответ на вопрос у someone
    def __str__(self):
        return "Студент"

class Curator(Human):

    def answer_question(self, question):
        if question=="мне грустненько, что делать?":
            return f"{self}> Держись все получится."
        else:
            return super().answer_question(question)
        # здесь нужно проверить, пришёл куратору знакомый вопрос или нет
        # если да - ответить на него
        # если нет - вызвать метод answer_question() у родительского класса
    def __str__(self):
        return "Куратор"

class CodeReviewer(Human):

    def answer_question(self, question):
        if question=="что не так с моим проектом?":
            return f"{self}> о вопрос про проект, я это люблю."
        else:
            return super().answer_question(question)
    def __str__(self):
        return "Ревьюер"

class Mentor(Human):

    def answer_question(self, question):
        if question=="мне грустненько, что делать?":
            return f"{self}>Отдохни и возвращайся с вопросом по теории."
        else:
            return super().answer_question(question)

    def __str__(self):
        return "Ментор"

# объявите и реализуйте классы CodeReviewer и Mentor
# следующий код менять не нужно, он работает, мы проверяли

class WeatherMan(Human):
    def get_weather(self):
        return "Погода" + str(randint(-10,10))

student = Student('Тимофей')
curator = Curator('Марина')
mentor = Mentor('Ира')
reviewer = CodeReviewer('Евгений')
friend = Human('Виталя')
weatherman= WeatherMan('Игорь')

print(student.ask_question(curator, 'мне грустненько, что делать?'))
print(student.ask_question(mentor, 'мне грустненько, что делать?'))
print(student.ask_question(reviewer, 'когда каникулы?'))
print(student.ask_question(reviewer, 'что не так с моим проектом?'))
print(student.ask_question(friend, 'как устроиться на работу питонистом?'))
print(student.ask_question(mentor, 'как устроиться работать питонистом?'))
print(student.ask_question(mentor, 'как твое имя'))
print(student.ask_question(weatherman, 'как погода'))