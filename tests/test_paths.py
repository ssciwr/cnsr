from cnsr.paths import *

import os
import pytest


def test_eda_init(eda):
    data = EDADataManager(root=eda, patient="12345")
    assert len(data.find_patients()) == 1
    assert data.root == eda
    assert data.patient == "12345"
    assert os.path.exists(data.filename)


def test_eda_property_setter(eda):
    data = EDADataManager()
    data.root = eda
    data.patient = "12345"
    assert len(data.find_patients()) == 1
    assert data.root == eda
    assert data.patient == "12345"
    assert os.path.exists(data.filename)


def test_eda_wrong_patient(eda):
    data = EDADataManager(root=eda)
    with pytest.raises(FileNotFoundError):
        data.patient = "non-existent"


def test_ern_init(ern):
    data = ERNDataManager(root=ern, patient="12345")
    assert len(data.find_patients()) == 1
    assert data.root == ern
    assert data.patient == "12345"
    assert os.path.exists(data.eegfile)
    assert os.path.exists(data.vhdrfile)
    assert os.path.exists(data.vmrkfile)


def test_ern_property_setter(ern):
    data = ERNDataManager()
    data.root = ern
    data.patient = "12345"
    assert len(data.find_patients()) == 1
    assert data.root == ern
    assert data.patient == "12345"
    assert os.path.exists(data.eegfile)
    assert os.path.exists(data.vhdrfile)
    assert os.path.exists(data.vmrkfile)


def test_ern_wrong_patient(ern):
    data = ERNDataManager(root=ern)
    with pytest.raises(FileNotFoundError):
        data.patient = "23456"


def test_faa_init(faa):
    data = FAADataManager(root=faa, patient="12345")
    assert len(data.find_patients()) == 1
    assert data.root == faa
    assert data.patient == "12345"
    assert os.path.exists(data.eegfile)
    assert os.path.exists(data.vhdrfile)
    assert os.path.exists(data.vmrkfile)


def test_faa_property_setter(faa):
    data = FAADataManager()
    data.root = faa
    data.patient = "12345"
    assert len(data.find_patients()) == 1
    assert data.root == faa
    assert data.patient == "12345"
    assert os.path.exists(data.eegfile)
    assert os.path.exists(data.vhdrfile)
    assert os.path.exists(data.vmrkfile)


def test_faa_wrong_patient(faa):
    data = FAADataManager(root=faa)
    with pytest.raises(FileNotFoundError):
        data.patient = "23456"


def test_hrv_init(hrv):
    data = HRVDataManager(root=hrv, patient="12345")
    assert len(data.find_patients()) == 1
    assert data.root == hrv
    assert data.patient == "12345"
    assert os.path.exists(data.eegfile)
    assert os.path.exists(data.vhdrfile)
    assert os.path.exists(data.vmrkfile)


def test_hrv_property_setter(hrv):
    data = HRVDataManager()
    data.root = hrv
    data.patient = "12345"
    assert len(data.find_patients()) == 1
    assert data.root == hrv
    assert data.patient == "12345"
    assert os.path.exists(data.eegfile)
    assert os.path.exists(data.vhdrfile)
    assert os.path.exists(data.vmrkfile)


def test_hrv_wrong_patient(hrv):
    data = HRVDataManager(root=hrv)
    with pytest.raises(FileNotFoundError):
        data.patient = "23456"


def test_faa_interactive(faa):
    # This only tests instantiation of the widgets. Better than nothing.
    data = FAADataManager(root=faa)
    data._repr_mimebundle_()
