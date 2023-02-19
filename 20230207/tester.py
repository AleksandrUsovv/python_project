# answer_question() - function to take one question as an argument
import json
def answer_question(question):
    while True:
        print(f'1.{question[0]} 2.{question[1]}\n'
              f'3.{question[2]} 4.{question[3]}')
        user_choice = input('What is your answer? -> ')
        if user_choice.lower() == 'exit':
            print('Ciao!')
            quit()
        if user_choice in '1234':
            return question[int(user_choice) - 1]
        else:
            print('Choice is out of range. Please try again or type "exit" to quit')

def check_answer(answer, user_answer):
    if user_answer == answer:
        return True
    return False

def start_quiz(topic, data):
    quiz = data[topic]
    score = 0
    print(quiz)
    for question in quiz.values():
        print(question.get('question'))
        user_answer = answer_question(question.get('options'))
        if check_answer(question.get('answer'), user_answer):
            score+=1
    print(f'You answered {score} questions right.')

def mail(data):
    print('Hello! Welcome to our quiz.')
    print(f'You can choose from {len(data.keys())} topics')

    for topic in data.keys():
        print('*', topic)
    while True:
        quiz_topic = input('Type topic name to continue or "exit" to quit. -> ')
        if quiz_topic.lower() == 'exit':
            print('Ciao!')
            quit()
        if quiz_topic.lower() in data.keys():
            start_quiz(quiz_topic.lower(), data)
            if input('Another quiz? y/n').lower() == 'y':
                mail(data)
        else:
            print(f'There is no {quiz_topic}')
            quit()


with open('quiz.json', 'r', encoding='utf8') as file:
    quiz_data = json.load(file).get('quiz')

mail(quiz_data)