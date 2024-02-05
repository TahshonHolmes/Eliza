# Tahshon Holmes - 02/05/2024 
# Tasked with writing a program to engage in dialogue with the user and the program should 
#     take the role of a psychotherapist named eliza. The program should recognize some key 
#     words and respond simply based on those words being in the user input. Also it should translate
#     some sentence forms into questions that eliza will them ask. 
# Examples:
#           [eliza] Hi, I'm a psychotherapist. What is your name?
#           [user] My name is Aang.
#           [eliza] Hi Aang. How can I help you today?
#           [Aang] I feel sad and I don't know why.
#           [eliza] Well Aang, why do you feel sad?
# How to use: in the terminal just run [python eliza.py] and it will start the program and eliza will begin the chat.
# The program uses a simple rule based approach where regular expressions and predefined responses are used to simulate speech.
#     Initially the program gets the users name, sets the cycle responses, and tracks whether or not the session has ended.
#     Then it greets the user and asks for their name, checks for an I feel statement. Then checks for a because statement. 
#     Then it checks for an i want statement with a followup as to why. Then it goes into generic questions and cycles with predefined responses. 
#     After 1 cycle, it ends the session and the user says an exit command. 

import re

class Eliza:
    # Starts the whole schbang and has the group of generic responses Eliza will cycle through. 
    def __init__(self):
        self.user_name = None
        self.prompt = "[user]"
        self.cycle_responses = [
            "I'm here to listen. Can you share more about your thoughts?",
            "Hmm... Interesting... I see I see, tell me more.",
            "Help me understand what that experience was like for you.",
            "What exactly do you think might be underlying these feelings?"
        ]
        self.cycle_index = 0
        self.session_ended = False
    # Eliza greets the user. 
    def greet_user(self):
        print("[eliza] Hi, I'm a psychotherapist. What is your name?")
    # This happens way later, where after it cycles the phrases above, Eliza says goodbye. 
    def process_input(self, user_input):
        if self.session_ended:
            print("[eliza] Well, I think that's enough for this session. See you next time, bye!")
            return

        # Checks if the user provides a name and then updates the little box at the beginning accordingly, also if they
        # don't start with one of the three words/phrases it will tell them to repeat their name. 
        if not self.user_name:
            match = re.search(r'\b(?:My name is|I am|I\'m)\s+(\w+)\b', user_input, re.IGNORECASE)
            if match:
                self.user_name = match.group(1)
                self.prompt = f"[{self.user_name}]"
                print(f"[eliza] Hi {self.user_name}. How can I help you today?")
            else:
                print("[eliza] I didn't quite catch your name. Can you tell me again?")
        else:
            # Checks if the user expresses emotions via the word "feel" which is the word being spotted in this case. 
            emotion_match = re.search(r'\bI feel\s+(\w+)\b', user_input, re.IGNORECASE)
            if emotion_match:
                emotion = emotion_match.group(1)
                print(f"[eliza] {self.prompt[1:-1]}, how long have you been feeling {emotion}?")
            else:
                # After the I feel statement, eliza asks why and if you have Because in your answer, it sees that and responds accordingly.
                because_match = re.search(r'\bbecause\s+(.+)\b', user_input, re.IGNORECASE)
                if because_match:
                    reason = because_match.group(1)
                    print(f"[eliza] Well, I'm sorry that you feel {reason} but why do you think you feel this way?")
                else:
                    # Word spotting for the word want because I feel like its a common word and one thats easy to interpret. 
                    want_to_match = re.search(r'\bI want to\s+(.+)\b', user_input, re.IGNORECASE)
                    if want_to_match:
                        action = want_to_match.group(1)
                        print(f"[eliza] Well, {self.prompt[1:-1]}, why do you want to {action}?")
                    else:
                        # Transforms the statement into a question.
                        transformed_input = re.sub(r'\b(?:I|I\'m)\s+(\w+)', r'Why do you think \1?', user_input, re.IGNORECASE)
                        
                        # Cycles through the responses and if it reaches all 4, then you leave. 
                        print(f"[eliza] {self.cycle_responses[self.cycle_index]}")
                        self.cycle_index = (self.cycle_index + 1) % len(self.cycle_responses)

                        if self.cycle_index == 0:
                            self.session_ended = True

    def start_dialogue(self):
        self.greet_user()

        # This starts the dialogue cycle and if the user enters one of the 7 words, the program ends and eliza says "Goodbye! Take care."
        while True:
            user_input = input(f"=> {self.prompt} ")
            if user_input.lower() in ['exit', 'quit', 'bye', 'goodbye', 'cya', 'later', 'deuces']:
                if self.session_ended:
                    print("[eliza] Goodbye! Take care.")
                break
            self.process_input(user_input)

if __name__ == "__main__":
    # Create an instance of Eliza and start the dialogue.
    eliza = Eliza()
    eliza.start_dialogue()
