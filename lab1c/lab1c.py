def read_file(filename):
    with open(filename, 'r') as file:
        content = file.read()
    return content

def parse_questions(questions_text):
    questions = questions_text.strip().split('\n\n')
    return questions

def parse_answers(answers_text):
    answers = {}
    lines = answers_text.strip().split('\n')
    for line in lines:
        q_num, answer = line.split('. ')
        answers[int(q_num)] = answer
    return answers

def display_quiz(questions, answers):
    for question in questions:
        print(question)
        q_num = int(question.split('.')[0])
        correct_answer = answers.get(q_num)
        print(f"Correct answer: {correct_answer}\n")

if __name__ == "__main__":
    questions_filename = 'Questions.txt'
    answers_filename = 'Answers.txt'
    
    # Read the content of the files
    questions_text = read_file(questions_filename)
    answers_text = read_file(answers_filename)
    
    # Parse questions and answers
    questions = parse_questions(questions_text)
    answers = parse_answers(answers_text)
    
    # Display the quiz with answers
    display_quiz(questions, answers)
