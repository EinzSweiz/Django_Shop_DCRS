from celery import Celery, shared_task
from django.core.mail import send_mail
from .models import Order



@shared_task
def order_created(order_id):
    order = Order.objects.get(id=order_id)
    subject = f'Order No. {order_id}'
    message = f'Dear {order.first_name}, \n\n'\
        f'You have successfully placed and order'\
        f'Your order ID is {order_id}'
    mail_send = send_mail(subject, 
                          message,
                          'riad.sultanov.1999@gmail.com',
                          [order.email])
    return mail_send