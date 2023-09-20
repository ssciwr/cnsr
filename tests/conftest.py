import os
import pytest


data_dir = os.path.join(os.path.dirname(__file__), "testdata")


def subdirectory_fixture(sub):
    @pytest.fixture
    def _fixture():
        return os.path.join(data_dir, sub)

    return _fixture


# One fixture per dataset type. These will always point to our respecive testdata
eda = subdirectory_fixture("EDA")
ern = subdirectory_fixture("ERN")
faa = subdirectory_fixture("FAA")
hrv = subdirectory_fixture("HRV")
