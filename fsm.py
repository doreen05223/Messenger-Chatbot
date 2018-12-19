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
            return text == '謝謝'
        return False

    def is_going_to_state3(self, event):
        if event.get("message"):
            text = event['message']['text']
            return text.lower() == '嗨'
        elif event.get("postback"):
            if event['postback']['title']=='詢問醫生問題':
                text = '詢問醫生問題'
                return text.lower() == '詢問醫生問題'
            elif event['postback']['title']=='預約看診':
                text = '預約看診'
                return text.lower() == '預約看診'
        return False

    def is_going_to_state4(self, event):
        if event.get("message"):
            text = event['message']['text']
            return text.lower() == '服務項目'
        elif event.get("postback"):
            if event['postback']['title']=='一般門診':
                text = '一般門診'
                return text.lower() == '一般門診'
            elif event['postback']['title']=='牙齒矯正':
                text = '牙齒矯正'
                return text.lower() == '牙齒矯正'
        return False

    def on_enter_state1(self, event):
        print("I'm entering state1")

        sender_id = event['sender']['id']
        if event['message'].get("text"):
            responese = send_text_message(sender_id, "I'm entering state1")
        elif event['message'].get("sticker_id"):
            responese = send_text_message(sender_id, "(๑´ڡ`๑)")
        elif event['message'].get("attachments"):
            responese = send_text_message(sender_id, "收到，晚點再回復您")
        self.go_back()

    def on_exit_state1(self):
        print('Leaving state1')

    def on_enter_state2(self, event):
        print("I'm entering state2")

        sender_id = event['sender']['id']
        send_text_message(sender_id, "不客氣~有任何問題都可以在聯絡")
        self.go_back()

    def on_exit_state2(self):
        print('Leaving state2')

    def on_enter_state3(self, event):
        print("I'm entering state3")

        sender_id = event['sender']['id']
        if event.get("message"):
            send_text_message(sender_id, "哈囉你好")
            send_button_message(sender_id, "請問您需要什麼服務呢?", "詢問醫生問題", "預約看診")
        elif event.get("postback"):
            text = event['postback']['payload']
            if text=="button1": send_text_message(sender_id, "請寫下您的問題或傳送圖片，稍後在為您答覆")
            elif text=="button2":  send_text_message(sender_id, "請寫下想要預約看診的日期時間,如果預約已經額滿會再另外通知")
        self.go_back()

    def on_exit_state3(self):
        print('Leaving state3')

    def on_enter_state4(self, event):
        print("I'm entering state4")

        sender_id = event['sender']['id']
        if event.get("message"):
            send_button_message(sender_id, "想要詢問哪方面的服務呢?", "一般門診", "牙齒矯正")
        elif event.get("postback"):
            text = event['postback']['payload']
            if text=="button1": send_text_message(sender_id, "口腔整體性的評估及治療\n蛀牙填補\n洗牙\n牙痛緊急處理\n定期口腔檢查")
            elif text=="button2":  send_text_message(sender_id, "藉由牙套及矯正線以期治療暴牙、戽斗、齒列擁擠、牙齒異位及各種的不正咬合")
        self.go_back()

    def on_exit_state4(self):
        print('Leaving state4')

        
