from exam.entities import Order


data_orders = [
    Order(id=1, user_id=1, type='A', amount=150, flag=True),
    Order(id=2, user_id=1, type='A', amount=151, flag=True),
    Order(id=3, user_id=2, type='B', amount=99, flag=False),
    Order(id=4, user_id=2, type='B', amount=100, flag=False),
    Order(id=5, user_id=2, type='B', amount=99, flag=True),
    Order(id=6, user_id=2, type='B', amount=100, flag=True),
    Order(id=7, user_id=3, type='C', amount=100, flag=True),
    Order(id=8, user_id=3, type='C', amount=100, flag=False),
    Order(id=10, user_id=5, type='C', amount=300, flag=True),
    Order(id=9, user_id=4, type='Z', amount=100, flag=True),
]
