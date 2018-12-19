from transitions.extensions import GraphMachine

from utils import send_text_message,send_button_message

class TocMachine(GraphMachine):
    def __init__(self, **machine_configs):
        self.machine = GraphMachine(
            model=self,
            **machine_configs
        )

    def is_going_to_state1(self, event):
       if event.get("message"):
            if event['message'].get("text"):
               text = event['message']['text']
            elif event['message'].get("attachments"):
               text = 'go to state1'
            return text.lower() == 'go to state1'
       return False

    def is_going_to_state2(self, event):
        if event.get("message"):
            text = event['message']['text']
            return text.lower() == 'go to state2'
        return False

    def is_going_to_state3(self, event):
        if event.get("message"):
            text = event['message']['text']
            return text.lower() == 'go to state3'
        return False

    def is_going_to_state4(self, event):
        print("in state4\n")
        if event.get("message"):
            text = event['message']['text']
            return text.lower() == 'go to state4'
        elif event.get("postback"):
            text = 'go to state4'
            return text.lower() == 'go to state4'
        return False

    def on_enter_state1(self, event):
        print("I'm entering state1")

        sender_id = event['sender']['id']
        if event['message'].get("text"):
            responese = send_text_message(sender_id, "I'm entering state1")
        elif event['message'].get("attachments"):
            responese = send_text_message(sender_id, "Great Photo><")
        self.go_back()

    def on_exit_state1(self):
        print('Leaving state1')

    def on_enter_state2(self, event):
        print("I'm entering state2")

        sender_id = event['sender']['id']
        send_text_message(sender_id, "I'm entering state2")
        self.go_back()

    def on_exit_state2(self):
        print('Leaving state2')

    def on_enter_state3(self, event):
        print("I'm entering state3")

        sender_id = event['sender']['id']
        send_text_message(sender_id, "I'm entering state3")
        self.go_back()

    def on_exit_state3(self):
        print('Leaving state3')

    def on_enter_state4(self, event):
        print("I'm entering button")

        sender_id = event['sender']['id']
        if event.get("message"):
            send_button_message(sender_id)
        elif event.get("postback"):
            text = event['postback']['payload']
            if text=="yes": send_text_message(sender_id, "Welcome!!")
            elif text=="no":  send_text_message(sender_id, "Why???")
        self.go_back()

    def on_exit_state4(self):
        print('Leaving state4')

