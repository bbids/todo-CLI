#!/usr/bin/python3
import unittest
import sys
import os

# we really want to create .config and .todo files right here, but really want to use todo so this is a fix
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from todo.config import Config
from todo.operation_API import Operation_API
from todo.operation import Operation


class TestHappyPath(unittest.TestCase):
    """Test the happy path. Verify that the software doesn't raise errors 
    when used under typical conditions under knowledable user. """

    def test_read(self):
        try:
            Operation.display_tasks()
        except Exception as e:
            self.fail(f"Exception: {e}")


    def test_add(self):
        try:
            content = "This is some content"
            priority = 5
            Operation.add_task(content, priority)
        except Exception as e:
            self.fail(f"Exception: {e}")

    def test_reset_ids(self):
        try:
            Operation.reset_ids()
        except Exception as e:
            self.fail(f"Exception: {e}")


def preliminary_setup():
    Config.create()

    operator = Operation_API()
    operator.create()

if __name__ == "__main__":
    preliminary_setup()
    unittest.main()