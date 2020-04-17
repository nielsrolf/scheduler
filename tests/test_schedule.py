import unittest


class TestSchedule(unittest.TestCase):
    def test_basic(self):
        from . import triangle_and_box_example # noqa

    def test_example(self):
        from . import fake_train_loop # noqa
