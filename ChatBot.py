import random
import re

class SupportBot:
    negative_res = {"no", "nope", "not a chance", "sorry", "incorrect"}
    exit_commands = {"quit", "stop", "pause", "exit", "bye"}

    def __init__(self):
        self.support_responses = {
            'ask_about_product': r'.*\bproduct\b.*',
            'technical_support': r'.*\btechnical\b.*\bsupport\b.*',
            'about_returns': r'.*\breturn\s*policy\b.*',
            'general_query': r'.*\bhow\b.*\bhelp\b.*'
        }

    def greet(self):
        self.name = input("Hello! Welcome to customer support by CodSoft. What's your name?\n")
        will_help = input(f"Hi {self.name}, how can I help you today?\n").lower()
        if will_help in self.negative_res:
            print("Alright, have a great day!")
            return
        self.chat()

    def make_exit(self, reply):
        for command in self.exit_commands:
            if command in reply:
                print("Thanks for reaching out. Have a great day!")
                return True
        return False

    def chat(self):
        reply = input("Please tell me your query:\n").lower()
        while not self.make_exit(reply):
            reply = input(self.match_reply(reply))

    def match_reply(self, reply):
        for intent, regex_pattern in self.support_responses.items():
            if re.search(regex_pattern, reply):
                if intent == 'ask_about_product':
                    return self.ask_about_product()
                elif intent == 'technical_support':
                    return self.technical_support()
                elif intent == 'about_returns':
                    return self.about_returns()
                elif intent == 'general_query':
                    return self.general_query()
        return self.no_match_intent()

    def ask_about_product(self):
        responses = [
            "Our service is top notch!",
            "You can find all the product details on our website."
        ]
        return random.choice(responses)

    def technical_support(self):
        responses = [
            "Please visit our technical support page for assistance.",
            "Our technical support team is available 24/7."
        ]
        return random.choice(responses)

    def about_returns(self):
        responses = [
            "We have a 30-day assistance policy.",
            "You can return your product within 30 days of purchase."
        ]
        return random.choice(responses)

    def general_query(self):
        responses = [
            "I'm here to assist you! Ask me anything.",
            "How can I be of service today?"
        ]
        return random.choice(responses)

    def no_match_intent(self):
        responces =("Im sorry can you provide me more details?.\n") 
        return random.choice(responces)
    
bot = SupportBot()
bot.greet()
