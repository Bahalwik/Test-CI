import pytest
import random


@pytest.mark.flaky(reruns=3, reruns_delay=2)
def test_rerun():
    assert random.choice([True, False])


@pytest.mark.flaky(reruns=3, reruns_delay=1)
class TestReruns:
    def test_rerun_1(self):
        assert random.choice([True, False])

    def test_rerun_2(self):
        assert random.choice([True, False])



PLATFORM = 'Windows'


@pytest.mark.flaky(reruns=3, reruns_delay=1, condition=PLATFORM == "Windows")
def test_rerun_with_condition():
    assert random.choice([True, False])