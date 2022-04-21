from application import db
from application.templates.models import Customer, Address, RegisteredUser

db.drop_all()
db.create_all()

testCustomer1 = Customer(first_name="Mya", last_name="Miah", email="mya.miah1980@gmail.com", phone="07932673910")
testCustomer2 = Customer(first_name="Tunji", last_name="Oladiran", email="tunji.oladiran@gmail.com", phone="07799585741")

db.session.add(testCustomer1)
db.session.add(testCustomer2)

db.session.commit()