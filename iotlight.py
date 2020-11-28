from firebase import firebase
from boltiot import Bolt
api_key ="2618ae2f-37a9-4eb7-9da1-29b1708258f2"
device_id ="BOLT14856162"
mybolt = Bolt(api_key,device_id)
connect=firebase.FirebaseApplication("https://siva-iot-light.firebaseio.com/", None)
while True:
    a = connect.get("/sivaiotlight/",None)
    b=a.get("off")
    if b == "1":
        mybolt.digitalWrite('0','HIGH')
    else:
        mybolt.digitalWrite('0','LOW')
    print(b)
