"""Unit tests for KeyTrace.py. Run with: python3 -m unittest discover -s tests

pynput is stubbed out because it needs a live keyboard/display; the tests
only exercise the pure key-formatting logic.
"""
import os
import sys
import types
import unittest

# ---- Stub pynput before KeyTrace imports it ----
pynput = types.ModuleType("pynput")
keyboard = types.ModuleType("pynput.keyboard")


class Listener:  # minimal stand-in, never actually started in tests
    def __init__(self, on_press=None):
        self.on_press = on_press

    def __enter__(self):
        return self

    def __exit__(self, *args):
        return False

    def join(self):
        pass


keyboard.Listener = Listener
pynput.keyboard = keyboard
sys.modules["pynput"] = pynput
sys.modules["pynput.keyboard"] = keyboard

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from KeyTrace import format_key, IGNORED_KEYS


class FakeKey:
    def __init__(self, name):
        self._name = name

    def __str__(self):
        return self._name


class TestFormatKey(unittest.TestCase):
    def test_regular_character(self):
        self.assertEqual(format_key(FakeKey("'a'")), "a")

    def test_space(self):
        self.assertEqual(format_key(FakeKey("Key.space")), " ")

    def test_enter(self):
        self.assertEqual(format_key(FakeKey("Key.enter")), "\n")

    def test_backspace(self):
        self.assertEqual(format_key(FakeKey("Key.backspace")), "[BACKSPACE]")

    def test_tab(self):
        self.assertEqual(format_key(FakeKey("Key.tab")), "[TAB]")

    def test_modifiers_ignored(self):
        for name in ("Key.shift", "Key.shift_l", "Key.ctrl_r", "Key.alt"):
            self.assertIn(name, IGNORED_KEYS)
            self.assertIsNone(format_key(FakeKey(name)))

    def test_unknown_key_passes_through(self):
        self.assertEqual(format_key(FakeKey("Key.f5")), "Key.f5")


if __name__ == "__main__":
    unittest.main()
