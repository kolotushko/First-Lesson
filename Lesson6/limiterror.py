class LimitError(Exception):
    def __init(self, amount=0, limit=0):
        self.Amount = amount
        self.Limit = limit
    def __str__(self):
        return f"Dear Customer unfortunetly you want {self.Amount} goods\n"  \
               f"but we have only {self.Limit} goods\n"  \
               f"If you wantmore than we have you have to wait 2 days\n" \
               f"Thank you."

