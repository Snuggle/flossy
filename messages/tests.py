from django.test import TestCase
from django.test import Client

testPaths = ['/', '/messages/', '/messages/1', '/messages/admin']

client = Client()
for path in testPaths:
    response = client.get(path)
    print(f"Path {path} exited with code {response.status_code}")
