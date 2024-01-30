#!/usr/bin/python3
import unittest
import sys
import os
import logging

# we really want to create .config and .todo files right here, but really want to use todo so this is a fix
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from todo.operation_API import Operation_API

#Operation_API.test()

class TestHappyPath(unittest.TestCase):
    """Test the happy path. Verify that the software doesn't raise errors 
    when used under typical conditions under knowledable user. """

    def test_general1(self):
        try:
            with self.assertNoLogs(level = logging.ERROR):
                args = Args("create")
                operator = Operation_API(args)
                operator.execute()

                args = Args("add")
                args.task = "some content"
                operator = Operation_API(args)
                operator.execute()

                args = Args("remove")
                args.taskID = 0
                operator = Operation_API(args)
                operator.execute()

                args = Args("add")
                args.task = "some content yep"
                operator = Operation_API(args)
                operator.execute()

                args = Args("add")
                args.task = "some content yep yep"
                operator = Operation_API(args)
                operator.execute()

                args = Args("reset_ids")
                operator = Operation_API(args)
                operator.execute()

                args = Args("read")
                operator = Operation_API(args)
                operator.execute()

                args = Args("remove")
                args.taskID = 1
                operator = Operation_API(args)
                operator.execute()
        
                args = Args("read")
                operator = Operation_API(args)
                operator.execute()
        except Exception as e:
            self.fail(f"Unexpected exception: {e}")

            
class Args:
    def __init__(self, operation):
        self.operation = operation
        self.prio = None        
if __name__ == "__main__":
    unittest.main()