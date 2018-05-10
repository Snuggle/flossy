from django.test import TestCase
from django.test import Client

testPaths = ['/', '/messages/', '/admin', '/settings', '/register']

client = Client()
for path in testPaths:
    response = client.get(path)
    print(f"Path \"{path}\" exited with code: {response.status_code}")

# Simple test to check that the paths above are functional without errors.
