# from likes.models import Quote
import json
import pika
# import django
# from django.conf import settings
from sys import path
from os import environ
# from likes import defaults
# from likes import Settings


# Your path to settings.py file
# path.append(
#     '/Users/rojsiroj/Projects/sandboxes/python/rabbitmq/Likes/likes/settings.py')
# environ.setdefault('DJANGO_SETTINGS_MODULE', 'likes.settings')
# settings = Settings(apps=["my_app"])
# settings = Settings(modules=[defaults])
# settings.configure(default_settings=settings, DEBUG=True)
# django.setup()

connection = pika.BlockingConnection(pika.ConnectionParameters(
    'localhost', heartbeat=600, blocked_connection_timeout=300))
channel = connection.channel()
channel.queue_declare(queue='likes')


def callback(ch, method, properties, body):
    print("Received in likes...")
    print(body)
    data = json.loads(body)
    print(data)

    if properties.content_type == 'quote_created':
        # quote = Quote.objects.create(id=data['id'], title=data['title'])
        # quote.save()
        print("quote created")
    elif properties.content_type == 'quote_updated':
        # quote = Quote.objects.get(id=data['id'])
        # quote.title = data['title']
        # quote.save()
        print("quote updated")
    elif properties.content_type == 'quote_deleted':
        # quote = Quote.objects.get(id=data)
        # quote.delete()
        print("quote deleted")


channel.basic_consume(
    queue='likes', on_message_callback=callback, auto_ack=True)
print("Started Consuming...")
channel.start_consuming()
