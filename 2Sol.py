# Ques 2
# Do django signals run in the same thread as the caller? Please support your answer with a code snippet that conclusively proves your stance. The code does not need to be elegant and production ready, we just need to understand your logic.

# Ans: Yes, Django signals run in the same thread as the caller by default.

# code
import threading
from django.db.models.signals import post_save
from django.dispatch import receiver
from myapp.models import MyModel

@receiver(post_save, sender=MyModel)
def my_handler(sender, instance, **kwargs):
    print("Signal received in thread:", threading.current_thread())
instance = MyModel.objects.create(name="Test")
print("Operation in thread:", threading.current_thread())
