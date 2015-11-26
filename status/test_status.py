# -*- coding: utf-8 -*-
import unittest
from client import testutils
from . import status


class TestStatusPlugin(unittest.TestCase):
    def setUp(self):
        self.plugin = testutils.get_plugin_instance(status.StatusPlugin)

    def test_is_valid_method(self):
        self.assertTrue(self.plugin.is_valid("status?"))
        self.assertTrue(self.plugin.is_valid("STATUS"))
        self.assertFalse(self.plugin.is_valid("Jasper, you're the best!"))

    def test_handle_method(self):
        mic = testutils.TestMic()
        self.plugin.handle("What's your status?", mic)
        self.assertEqual(len(mic.outputs), 1)
        self.assertIn("I am currently running", mic.outputs[0])
