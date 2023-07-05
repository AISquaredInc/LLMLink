chat = {
    'user_msg' : None,
    'bot_msg' : None,
    'binary_feedback' : None,
    'correction' : None
}

def binary_feedback_handler(choice):
    chat['binary_feedback'] = 1 if choice == 'Good Response' else -1

def correction_feedback_handler(correction):
    chat['correction'] = correction

def submit_feedback():
    if chat['user_msg'] is not None and chat['bot_msg'] is not None:
        print(f'User Messsage: {chat["user_msg"]}')
        print(f'Bot Message: {chat["bot_msg"]}')
        print(f'Binary Feedback: {chat["binary_feedback"]}')
        print(f'Correction: {chat["correction"]}')
    
    chat['user_msg'] = None
    chat['bot_msg'] = None
    chat['binary_feedback'] = None
    chat['correction'] = None
