# Ques 1
# By default are django signals executed synchronously or asynchronously? Please support your answer with a code snippet that conclusively proves your stance. The code does not need to be elegant and production ready, we just need to understand your logic.

# Ans:
# Django signals are executed synchronously by default.

# code

import time
from django.db.models.signals import post_save
from django.dispatch import receiver
from myapp.models import MyModel

@receiver(post_save, sender=MyModel)
def my_handler(sender, instance, **kwargs):
    print("Signal handler started")
    time.sleep(10)
    print("Signal handler finished")

print("Saving instance")
MyModel.objects.create(name="Test Instance")
print("Instance saved")