import firebase_admin
from firebase_admin import credentials, db

# Initialize Firebase
cred = credentials.Certificate(""C:\Users\jayson\Downloads\bored-168f2-firebase-adminsdk-hbtoz-8b5a72160d.json"")
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://bored-168f2-default-rtdb.firebaseio.com'
})

# Reference the "visitors" node in the database
ref = db.reference('visitors')

# Increment visitor count
def increment_visitors():
    visitors = ref.get() or 0
    visitors += 1
    ref.set(visitors)
    print(f"Visitors: {visitors}")

if __name__ == "__main__":
    increment_visitors()
