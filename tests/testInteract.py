#!/usr/bin/python3
import unittest
import sys
import os
import logging

# we really want to create .config and .todo files right here, but really want to use todo so this is a fix
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from todo.operation_API import Operation_API

#Operation_API.test()
class TestInteract(unittest.TestCase):

    def test_general3(self):
        """Test interact"""
        try:
            with self.assertNoLogs(level = logging.ERROR):
                args = Args("config")
                operator = Operation_API(args)
                operator.execute()

                args = Args("create")
                operator = Operation_API(args)
                operator.execute()

                args = Args("add")
                args.task = "some content"
                operator = Operation_API(args)
                operator.execute()

                args = Args("interact")
                operator = Operation_API(args)
                operator.execute()             
        except Exception as e:
            self.fail(f"Unexpected exception: {e}")


    def test_general2(self):
        """Config test"""
        try:
            with self.assertNoLogs(level = logging.ERROR):
                args = Args("config")
                operator = Operation_API(args)
                operator.execute()

                args = Args("create")
                operator = Operation_API(args)
                operator.execute()

                args = Args("config")
                operator = Operation_API(args)
                operator.execute()             
        except Exception as e:
            self.fail(f"Unexpected exception: {e}")

            
class Args:
    def __init__(self, operation):
        self.operation = operation
        self.prio = None     

if __name__ == "__main__":
    loader = unittest.TestLoader()

    # we load interact first because it clears the terminal
    suite = unittest.TestSuite([
        loader.loadTestsFromTestCase(TestInteract),
    ])
    unittest.TextTestRunner().run(suite)