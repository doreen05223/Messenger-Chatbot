# TOC Project 2019
牙醫門診Chatbot

## How to Start the Chatbot
1. ./ngrok http 5000 (creat a https URL)
2. python3 app.py
3. setting webhook on the website *facebook for developer* (https URL created by ngrok, VERIFY_TOKEN=2325)
4. finish setting

## How to Interact with the Chatbot
> state1
* Input: 讚或貼圖
	* Reply: (๑´ڡ`๑)
* Input: image
	* Reply:  收到，晚點再回復您
> state2
* Input: 謝謝
	* Reply: 不客氣~有任何問題都可以在聯絡
> state3
* Input: 嗨
	* Reply: 哈囉你好
	* Reply: 請問您需要什麼服務呢?Tap a button to answer.[Two buttons:詢問醫生問題, 預約看診]
	* Click "詢問醫生問題" -> reply "請寫下您的問題或傳送圖片，稍後在為您答覆"
	* Click "預約看診"  -> reply "請寫下想要預約>看診的日期時間,如果預約已經額滿會再另外通知"
> state4
* Input: 服務項目
	* Reply: 想要詢問哪方面的服務呢?Tap a button to answer.[Two buttons:一般門診, 牙齒矯正]
	* Click "一般門診" -> reply "口腔整體性的評估及治療\n蛀牙填補\n洗牙\n牙痛緊急處理\n定期口腔檢查"
	* Click "牙齒矯正"  -> reply "藉由牙套及矯正>線以期治療暴牙、戽斗、齒列擁擠、牙齒異位及各種的不正咬合"

## FSM
![fsm](./fsm.png)

## How to Start the Chatbot after push to Heroku
1. open the domain
2. setting webhook on the website *facebook for developer* (https URL = https://chatbot-f74056190.herokuapp.com/, VERIFY_TOKEN=2325)
3. start chatbot
4. see the details when running in view log
