from django.db import models
from users.models import User
from properties.models import Property

class Transaction(models.Model):
    property = models.ForeignKey(Property, on_delete=models.CASCADE)
    buyer = models.ForeignKey(User, on_delete=models.CASCADE, related_name='transactions')
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=20, choices=[('pending', 'Pending'), ('completed', 'Completed')])
    transaction_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Transaction for {self.property.title} by {self.buyer.username}"