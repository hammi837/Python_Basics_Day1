import pytest


def test_open_website(crossbrowser):
    print(f"Running test on: {crossbrowser}")
    assert crossbrowser in ["chrome", "firefox", "safari"] , "Unsupported browser!"