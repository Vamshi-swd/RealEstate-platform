# transactions/models.py
from django.db import models
from users.models import User

class Transaction(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    transaction_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Transaction by {self.user.username} for ${self.amount} on {self.transaction_date}"