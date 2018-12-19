import requests


GRAPH_URL = "https://graph.facebook.com/v2.6"
ACCESS_TOKEN = "EAAD796mGzdEBAL9W9bYpXc3WHwTQDUoF7WXzMtox7X6iPkZCY8vKGuFMjtuiHymMIHYr0R8bijfpJMBgqNIZAulMBpVohZCbdH8nJEYTki28nuVexOysMpxKs5H3eZAimRgxWu9quu38ZADkJW0mdDB8KAliLnsS43ZAZBXZBDv4LUMYQwD2o0NK"


def send_text_message(id, text):
    url = "{0}/me/messages?access_token={1}".format(GRAPH_URL, ACCESS_TOKEN)
    payload = {
        "recipient": {"id": id},
        "message": {"text": text}
    }
    response = requests.post(url, json=payload)

    if response.status_code != 200:
        print("Unable to send message: " + response.text)
    return response


"""
def send_image_url(id, img_url):
    pass
"""
def send_button_message(id):#, text, buttons):
    url = "{0}/me/messages?access_token={1}".format(GRAPH_URL, ACCESS_TOKEN)
    text = {
      "attachment": {
        "type": "template",
        "payload": {
          "template_type": "generic",
          "elements": [{
            "title": "Will you join the club?",
            "subtitle": "Tap a button to answer.",
            "buttons": [
              {
                "type": "postback",
                "title": "Yes!",
                "payload": "yes",
              },
              {
                "type": "postback",
                "title": "No!",
                "payload": "no",
              }
            ],
          }]
        }
      }
    }
    payload = {
        "recipient": {"id": id},
        "message": text
    }
    response = requests.post(url, json=payload)
    if response.status_code != 200:
        print("Unable to send message: ")
    return response
