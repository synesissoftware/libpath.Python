import unittest

import libpath


class Test_libpath(unittest.TestCase):

    def test_version(self):

        self.assertEqual('0.0.0.1', libpath.__version__)
