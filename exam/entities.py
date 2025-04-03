class Order:
    def __init__(self, id: int, user_id: int, type: str, amount: float, flag: bool, status: str = "new", priority: str = "low"):
        self.id = id
        self.user_id = user_id
        self.type = type
        self.amount = amount
        self.flag = flag
        self.status = status
        self.priority = priority
