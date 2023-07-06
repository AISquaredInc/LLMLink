feedback = {
    'user_msg': None,
    'bot_msg': None,
    'binary_feedback': None,
    'correction': None
}


def binary_feedback_handler(choice):
    feedback['binary_feedback'] = 1 if choice == 'Good Response' else -1


def correction_feedback_handler(correction):
    feedback['correction'] = correction


def submit_feedback():
    """
    Default function to submit feedback - simply prints the feedback to the console
    """
    if feedback['user_msg'] is not None and feedback['bot_msg'] is not None:
        print(f'User Messsage: {feedback["user_msg"]}')
        print(f'Bot Message: {feedback["bot_msg"]}')
        print(f'Binary Feedback: {feedback["binary_feedback"]}')
        print(f'Correction: {feedback["correction"]}')

    feedback['user_msg'] = None
    feedback['bot_msg'] = None
    feedback['binary_feedback'] = None
    feedback['correction'] = None
