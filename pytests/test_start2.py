class Testclass:
    """docstring for """
    def test_one(self):
        x = "this"
        assert 'h' in x, "if h is inside x"

    def test_two(self):
        y = "check"
        assert hasattr(y, 'hello')
