# transactions/models.py
from django.db import models
from users.models import User

class Transaction(models.Model):
    property_name = models.CharField(max_length=255)
    owner = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='properties_owned')
    buyer = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='properties_bought')
    broker = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='brokered_deals')
    agreement_cost = models.DecimalField(max_digits=10, decimal_places=2)
    selling_price = models.DecimalField(max_digits=10, decimal_places=2)
    broker_cost = models.DecimalField(max_digits=10, decimal_places=2)
    total_cost = models.DecimalField(max_digits=10, decimal_places=2)
    transaction_date = models.DateTimeField(auto_now_add=True)
    description = models.TextField()
    amount = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Transaction {self.id} for {self.property_name}"