from datetime import time
from django.test import TestCase
from .models import Task


class TaskModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        Task.objects.create(title='First task', body='First task body', done=False)
    
    def test_title(self):
        task = Task.objects.get(id=1)
        expected = f'{task.title}'
        self.assertEqual(expected, 'First task')
    
    