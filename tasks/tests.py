from importlib import import_module
from django.test import SimpleTestCase


class TaskURLModuleTests(SimpleTestCase):
    def test_tasks_urls_module_can_be_imported(self):
        import_module("tasks.urls")
