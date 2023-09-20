import glob
import ipywidgets
import ipyfilechooser
import os
import re


class DataManagerBase:
    def __init__(self, root=None, patient=None):
        self.root = root
        self.patient = patient

    @property
    def root(self):
        # If it was not specified, use a sensible default
        if self._root is None:
            self.root = os.path.join(os.getcwd(), "data")

        return self._root

    @root.setter
    def root(self, root):
        # If _root is None, we delete any previous choice and exit
        if root is None:
            self._root = None
            return self._root

        # Normalize and validate the given path
        root = os.path.abspath(root)
        if not os.path.exists(root):
            raise FileNotFoundError(f"The data directory '{root}' does not exist.'")

        # Store it
        self._root = root

    @property
    def patient(self):
        if self._patient is None:
            raise ValueError("No patient was selected.")

        return self._patient

    @patient.setter
    def patient(self, patient):
        if patient is None:
            self._patient = None
            return

        if patient not in self.find_patients():
            raise FileNotFoundError(
                f"Data for patient '{patient}' missing or incomplete"
            )

        self._patient = patient

    def find_patients(self):
        return []

    def _repr_mimebundle_(self, **kwargs):
        # Create interactive UI elements
        root = ipyfilechooser.FileChooser()
        root.show_only_dirs = True
        root.title = "Data Root Directory"
        patient = ipywidgets.Dropdown(
            options=self.find_patients(), description="Patient:"
        )

        def _root_callback(c):
            self.root = c.value
            patient.options = self.find_patients()

        root.register_callback(_root_callback)

        def _patient_callback(p):
            if p["type"] == "change":
                self.patient = p["new"]

        patient.observe(_patient_callback, names="value")
        return ipywidgets.VBox(children=[root, patient])._repr_mimebundle_(**kwargs)


class EDADataManager(DataManagerBase):
    def find_patients(self):
        patients = []
        for f in glob.glob(f"{self._root}{os.sep}*.txt"):
            patient = re.match("([0-9]*).txt", os.path.relpath(f, self._root)).groups()[
                0
            ]
            patients.append(patient)

        return patients

    @property
    def filename(self):
        return os.path.join(self.root, f"{self.patient}.txt")


class ERNDataManager(DataManagerBase):
    def find_patients(self):
        patients = []
        for f in glob.glob(f"{self._root}{os.sep}sart_*.eeg"):
            patient = re.match(
                "sart_([0-9]*).eeg", os.path.relpath(f, self._root)
            ).groups()[0]
            if all(
                os.path.exists(os.path.join(self._root, f"sart_{patient}.{ext}"))
                for ext in ["eeg", "vhdr", "vmrk"]
            ):
                patients.append(patient)

        return patients

    @property
    def eegfile(self):
        return os.path.join(self._root, f"sart_{self.patient}.eeg")

    @property
    def vhdrfile(self):
        return os.path.join(self._root, f"sart_{self.patient}.vhdr")

    @property
    def vmrkfile(self):
        return os.path.join(self._root, f"sart_{self.patient}.vmrk")


class FAADataManager(DataManagerBase):
    def find_patients(self):
        patients = []
        for f in glob.glob(f"{self._root}{os.sep}*.eeg"):
            patient = re.match("([0-9]*).eeg", os.path.relpath(f, self._root)).groups()[
                0
            ]
            if all(
                os.path.exists(os.path.join(self._root, f"{patient}.{ext}"))
                for ext in ["eeg", "vhdr", "vmrk"]
            ):
                patients.append(patient)

        return patients

    @property
    def eegfile(self):
        return os.path.join(self._root, f"{self.patient}.eeg")

    @property
    def vhdrfile(self):
        return os.path.join(self._root, f"{self.patient}.vhdr")

    @property
    def vmrkfile(self):
        return os.path.join(self._root, f"{self.patient}.vmrk")


class HRVDataManager(DataManagerBase):
    def find_patients(self):
        patients = []
        for f in glob.glob(f"{self._root}{os.sep}rest_*.eeg"):
            patient = re.match(
                "rest_([0-9]*).eeg", os.path.relpath(f, self._root)
            ).groups()[0]
            if all(
                os.path.exists(os.path.join(self._root, f"rest_{patient}.{ext}"))
                for ext in ["eeg", "vhdr", "vmrk"]
            ):
                patients.append(patient)

        return patients

    @property
    def eegfile(self):
        return os.path.join(self._root, f"rest_{self.patient}.eeg")

    @property
    def vhdrfile(self):
        return os.path.join(self._root, f"rest_{self.patient}.vhdr")

    @property
    def vmrkfile(self):
        return os.path.join(self._root, f"rest_{self.patient}.vmrk")
