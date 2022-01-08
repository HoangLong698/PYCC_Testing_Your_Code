from survey import AnonymouseSurvey

# Define a question, and make a survey.
question = "What language did you first learn to speak?\n"
my_survery = AnonymouseSurvey(question)

# Show the question, and store response to the question.
my_survery.show_question()
print("Enter 'q' at any time to quit.\n")
while True:
    response = input("Language: ")
    if response == 'q':
        break
    my_survery.store_response(response)

# Show the survey results.
print("\nThank you to everyone who participated in the survery!")
my_survery.show_result()