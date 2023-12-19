import pytest
from project import get_rid_of_punctuation
from project import get_sentence


def test_get_rid_of_punctuation():
    assert get_rid_of_punctuation("Hey") == "Hey"
    assert get_rid_of_punctuation("Hey,") == "Hey"
    assert get_rid_of_punctuation("Hey!") == "Hey"
    assert get_rid_of_punctuation("Hey?") == "Hey"
    assert get_rid_of_punctuation("Hey.") == "Hey"


def test_get_sentence():
    assert get_sentence(0) == "Better luck next time!"
    assert get_sentence(1) == "Well done!"
    assert get_sentence(10) == "Well done!"
