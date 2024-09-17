# Ques 3
# By default do django signals run in the same database transaction as the caller? Please support your answer with a code snippet that conclusively proves your stance. The code does not need to be elegant and production ready, we just need to understand your logic.

# Ans: Yes, Django signals run in the same database transaction as the caller by default.

# code
from django.db import transaction
from django.db.models.signals import post_save
from django.dispatch import receiver
from myapp.models import MyModel

@receiver(post_save, sender=MyModel)
def my_handler(sender, instance, **kwargs):
    print("Signal received after save")

with transaction.atomic():
    instance = MyModel.objects.create(name="Test")
    print("Database transaction successful.")
