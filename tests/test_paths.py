from cnsr.paths import *

import os
import pytest


def test_eda_init(eda):
    data = EDADataManager(root=eda, participant="12345")
    assert len(data.find_participants()) == 1
    assert data.root == eda
    assert data.participant == "12345"
    assert os.path.exists(data.filename)


def test_eda_property_setter(eda):
    data = EDADataManager()
    data.root = eda
    data.participant = "12345"
    assert len(data.find_participants()) == 1
    assert data.root == eda
    assert data.participant == "12345"
    assert os.path.exists(data.filename)


def test_eda_wrong_participant(eda):
    data = EDADataManager(root=eda)
    with pytest.raises(FileNotFoundError):
        data.participant = "non-existent"


def test_ern_init(ern):
    data = ERNDataManager(root=ern, participant="12345")
    assert len(data.find_participants()) == 1
    assert data.root == ern
    assert data.participant == "12345"
    assert os.path.exists(data.eegfile)
    assert os.path.exists(data.vhdrfile)
    assert os.path.exists(data.vmrkfile)


def test_ern_property_setter(ern):
    data = ERNDataManager()
    data.root = ern
    data.participant = "12345"
    assert len(data.find_participants()) == 1
    assert data.root == ern
    assert data.participant == "12345"
    assert os.path.exists(data.eegfile)
    assert os.path.exists(data.vhdrfile)
    assert os.path.exists(data.vmrkfile)


def test_ern_wrong_participant(ern):
    data = ERNDataManager(root=ern)
    with pytest.raises(FileNotFoundError):
        data.participant = "23456"


def test_faa_init(faa):
    data = FAADataManager(root=faa, participant="12345")
    assert len(data.find_participants()) == 1
    assert data.root == faa
    assert data.participant == "12345"
    assert os.path.exists(data.eegfile)
    assert os.path.exists(data.vhdrfile)
    assert os.path.exists(data.vmrkfile)


def test_faa_property_setter(faa):
    data = FAADataManager()
    data.root = faa
    data.participant = "12345"
    assert len(data.find_participants()) == 1
    assert data.root == faa
    assert data.participant == "12345"
    assert os.path.exists(data.eegfile)
    assert os.path.exists(data.vhdrfile)
    assert os.path.exists(data.vmrkfile)


def test_faa_wrong_participant(faa):
    data = FAADataManager(root=faa)
    with pytest.raises(FileNotFoundError):
        data.participant = "23456"


def test_hrv_init(hrv):
    data = HRVDataManager(root=hrv, participant="12345")
    assert len(data.find_participants()) == 1
    assert data.root == hrv
    assert data.participant == "12345"
    assert os.path.exists(data.eegfile)
    assert os.path.exists(data.vhdrfile)
    assert os.path.exists(data.vmrkfile)


def test_hrv_property_setter(hrv):
    data = HRVDataManager()
    data.root = hrv
    data.participant = "12345"
    assert len(data.find_participants()) == 1
    assert data.root == hrv
    assert data.participant == "12345"
    assert os.path.exists(data.eegfile)
    assert os.path.exists(data.vhdrfile)
    assert os.path.exists(data.vmrkfile)


def test_hrv_wrong_participant(hrv):
    data = HRVDataManager(root=hrv)
    with pytest.raises(FileNotFoundError):
        data.participant = "23456"


def test_faa_interactive(faa):
    # This only tests instantiation of the widgets. Better than nothing.
    data = FAADataManager(root=faa)
    data._repr_mimebundle_()
