from django.test import TestCase

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
