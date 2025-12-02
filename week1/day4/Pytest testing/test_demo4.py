import pytest

@pytest.mark.usefixtures("setup")
class TestDemo4:
    def test_methodA(self):
        print("Executing Test Method A")

    def test_methodB(self):
        print("Executing Test Method B")

    def test_methodC(self):
        print("Executing Test Method C")

    def test_methodD(self):
        print("Executing Test Method D")

