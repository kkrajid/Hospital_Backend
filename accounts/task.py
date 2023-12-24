from celery import shared_task
import pyrebase
import time
import requests

firebase_config = {
    "apiKey": "YourFirebaseApiKey",
    "authDomain": "YourFirebaseAuthDomain",
    "databaseURL": "https://hospitalmgnt-default-rtdb.asia-southeast1.firebasedatabase.app/",
    "storageBucket": None,
}

firebase = pyrebase.initialize_app(firebase_config)
db = firebase.database()

@shared_task(bind=True)
def read_and_notify_task(self):
    try:
        previous_notifications = set()

        while True:
            nodes = db.child("/").get().val()
            for node, data in nodes.items():
                heart_rate = data.get("HeartRate", None)
                user_id = data.get("user_id", None)
                doctor_id=data.get("doctor_id",None)
                print(f"Node {node} - Heart Rate: {heart_rate} - UserID: {user_id}")

                if heart_rate is not None:
                    heart_rate = int(heart_rate)

                    if heart_rate > 80 and node not in previous_notifications:
                        print(f"Sending frontend notification for Node {node}!")
                        notification_data = {
                            "node": node,
                            "heart_rate": heart_rate,
                            "user_id": user_id,
                            "doctor_id":doctor_id
                        }
                        previous_notifications.add(node)
                        requests.post('http://127.0.0.1:8000/api/notifications/', data=notification_data)

                    elif heart_rate <= 80 and node in previous_notifications:
                        print(f"Heart rate for Node {node} is below 100. Removing from notifications.")
                        previous_notifications.remove(node)

            time.sleep(10)
    except Exception as e:
        print("An error occurred:", str(e))

