from django.test import TestCase
from django.urls import reverse
from rest_framework import status

from todos.models import Todo


class TodoTest(TestCase):
    def setUp(self) -> None:
        self.todo_test = Todo.objects.create(
            title='Test title',
            body='Test body'
        )

    def test_todo_content(self):
        self.assertEqual(self.todo_test.title, 'Test title')
        self.assertEqual(self.todo_test.body, 'Test body')
        self.assertEqual(str(self.todo_test), 'Test title')

    def test_todo_list(self):
        response = self.client.get(reverse('todo_list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertContains(response, 'Test title')
        self.assertEqual(Todo.objects.count(), 1)

    def test_todo_detail(self):
        response = self.client.get(reverse('todo_detail', kwargs={'pk': self.todo_test.id}), format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Todo.objects.count(), 1)
        self.assertContains(response, 'Test title')
