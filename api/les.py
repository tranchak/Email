from datetime import datetime
from django.conf import settings
from rest_framework import serializers
settings.configure()
from rest_framework.renderers import JSONRenderer
import io
from rest_framework.parsers import JSONParser

class Comment:
    def __init__(self, email, content, created=None):
        self.email = email
        self.content = content
        self.created = created or datetime.now()


comment = Comment(email='leila@example.com', content='foo bar')

print('1--',comment.email, comment.content, comment.created)


class CommentSerializer(serializers.Serializer):
    email = serializers.EmailField()
    content = serializers.CharField(max_length=200)
    created = serializers.DateTimeField()


serial = CommentSerializer(comment)
print('2--',serial.data)

json = JSONRenderer().render(serial.data)
print('3--',json)

stream = io.BytesIO(json)
data = JSONParser().parse(stream)
print('4--', data)

serializer = CommentSerializer(data=data)
serializer.is_valid()
print('5--', serializer.is_valid())
# True
serializer.validated_data
print('6--', serializer.validated_data)


akz = Comment(**serializer.validated_data)
print('7--', akz)
print('8--', akz.email, akz.content,akz.created)