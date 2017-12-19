import unittest
import bootstrapper.cli as cli

class CliTestClass(unittest.TestCase):

    def test_do_something(self):
        expected = 'hello world'
        actual = cli.get_the_value()
        assert actual == expected

if __name__ == '__main__':
    unittest.main()
