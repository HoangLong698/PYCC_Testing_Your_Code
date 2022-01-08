class AnonymouseSurvey:
    """Collect anonymouse answer to a survey question."""

    def __init__(self, question) -> None:
        """Store a question, and prepare to store response."""
        self.question = question
        self.responses = []

    def show_question(self):
        """Show the survey question."""
        print(self.question)

    def store_response(self, new_respone):
        """Store a single response to the suvery."""
        self.responses.append(new_respone)

    def show_result(self):
        """Show all the responses that have been given"""
        print("Survery results:")
        for response in self.responses:
            print(f"- {response}")