import cv2
import mediapipe as mp
import paho.mqtt.client as mqtt

mqttbroker = "broker.hivemq.com"
client = mqtt.Client()
client.connect("broker.hivemq.com")
topic = "fery/tangan"

cap = cv2.VideoCapture(0)
mphand = mp.solutions.hands
hands = mphand.Hands()
while True:
    success, img = cap.read()
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = hands.process(imgRGB)
    if results.multi_hand_landmarks:
        client.publish(topic, "ada tangan")
        print("ada tangan")
    else:
        client.publish(topic, "tidak ada tangan")
        print("tidak ada tangan")
    cv2.imshow("kamera", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
