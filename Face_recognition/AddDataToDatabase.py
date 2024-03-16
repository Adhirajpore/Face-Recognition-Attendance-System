import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred,{
    'databaseURL':"https://faceattendancesystem-8c19d-default-rtdb.firebaseio.com/"
})

ref = db.reference('Students')

data = {
    "235768":
    {
        "name":"Vansh Parihar ",
        "Branch":"Computer",
        "starting_year":2022,
        "total_attendance":6,
        "standing":"Good",
        "year":2,
        "last_attendance_time":"2024-03-14 07:36:56"
    },
    "878324":
    {
        "name":"Lavya Goel ",
        "Branch":"Computer",
        "starting_year":2022,
        "total_attendance":6,
        "standing":"Good",
        "year":2,
        "last_attendance_time":"2024-03-14 07:36:56"
    },
    "896523":
    {
        "name":"Adhiraj Pore",
        "Branch":"Computer",
        "starting_year":2022,
        "total_attendance":5,
        "standing":"Good",
        "year":2,
        "last_attendance_time":"2024-03-14 07:36:56"

    },
    "897345":
    {
        "name":"Rohit Mudliyar",
        "Branch":"Computer",
        "starting_year":2022,
        "total_attendance":8,
        "standing":"Good",
        "year":2,
        "last_attendance_time":"2024-03-14 07:36:56"
    }

}

for key,value in data.items():
    ref.child(key).set(value)