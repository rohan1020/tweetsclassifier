import pytest
from featureMappers import *

tweet_str = "may god help the families of the victims of the #gurdaspurattack ."

def test_featureMap():

    t = TagSequence()

    print t.getFeatureVector(tweet_str)

    assert 1==1

@pytest.mark.skipif("True")
def test_featureVector_length_of_two_strings_be_same():

    t = TagSequence()

    str1 = "my name is xxx"
    str2 = "my name is xxx and yyy"

    v1 = t.getFeatureVector(str1)
    v2 = t.getFeatureVector(str2)

    assert len(v1) == len(v2)

