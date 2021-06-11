from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []
for q_text_ans in question_data:
    question_text = q_text_ans["question"]
    question_answer = q_text_ans["correct_answer"]
    new_question = Question(q_text=question_text, q_answer=question_answer)
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)
while quiz.still_has_question():
    quiz.next_question()

print("Game Over ")
print(f" Your Final score is  {quiz.user_score}/{quiz.question_number}")


