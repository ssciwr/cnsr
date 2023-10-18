import glob
import ipywidgets
import ipyfilechooser
import os
import re


class DataManagerBase:
    def __init__(self, root=None, participant=None):
        self.root = root
        self.participant = participant

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
    def participant(self):
        if self._participant is None:
            raise ValueError("No participant was selected.")

        return self._participant

    @participant.setter
    def participant(self, participant):
        if participant is None:
            self._participant = None
            return

        if participant not in self.find_participants():
            raise FileNotFoundError(
                f"Data for participant '{participant}' missing or incomplete"
            )

        self._participant = participant

    def find_participants(self):
        return []

    def _repr_mimebundle_(self, **kwargs):
        # Create interactive UI elements
        root = ipyfilechooser.FileChooser(
            path=self._root if self._root is not None else os.getcwd(),
            select_default=True,
        )
        root.show_only_dirs = True
        root.title = "Data Root Directory"
        participant = ipywidgets.Dropdown(description="Participant:")

        def _root_callback(c):
            self.root = c.value
            participant.options = self.find_participants()

        root.register_callback(_root_callback)

        def _participant_callback(p):
            if p["type"] == "change":
                self.participant = p["new"]

        participant.observe(_participant_callback, names="value")
        participant.options = self.find_participants()

        return ipywidgets.VBox(children=[root, participant])._repr_mimebundle_(**kwargs)


class EDADataManager(DataManagerBase):
    def find_participants(self):
        participants = []
        for f in glob.glob(f"{self._root}{os.sep}*.txt"):
            participant = re.match(
                "([0-9]*).txt", os.path.relpath(f, self._root)
            ).groups()[0]
            participants.append(participant)

        return participants

    @property
    def filename(self):
        return os.path.join(self.root, f"{self.participant}.txt")


class ERNDataManager(DataManagerBase):
    def find_participants(self):
        participants = []
        for f in glob.glob(f"{self._root}{os.sep}sart_*.eeg"):
            participant = re.match(
                "sart_([0-9]*).eeg", os.path.relpath(f, self._root)
            ).groups()[0]
            if all(
                os.path.exists(os.path.join(self._root, f"sart_{participant}.{ext}"))
                for ext in ["eeg", "vhdr", "vmrk"]
            ):
                participants.append(participant)

        return participants

    @property
    def eegfile(self):
        return os.path.join(self._root, f"sart_{self.participant}.eeg")

    @property
    def vhdrfile(self):
        return os.path.join(self._root, f"sart_{self.participant}.vhdr")

    @property
    def vmrkfile(self):
        return os.path.join(self._root, f"sart_{self.participant}.vmrk")


class FAADataManager(DataManagerBase):
    def find_participants(self):
        participants = []
        for f in glob.glob(f"{self._root}{os.sep}*.eeg"):
            participant = re.match(
                "([0-9]*).eeg", os.path.relpath(f, self._root)
            ).groups()[0]
            if all(
                os.path.exists(os.path.join(self._root, f"{participant}.{ext}"))
                for ext in ["eeg", "vhdr", "vmrk"]
            ):
                participants.append(participant)

        return participants

    @property
    def eegfile(self):
        return os.path.join(self._root, f"{self.participant}.eeg")

    @property
    def vhdrfile(self):
        return os.path.join(self._root, f"{self.participant}.vhdr")

    @property
    def vmrkfile(self):
        return os.path.join(self._root, f"{self.participant}.vmrk")


class HRVDataManager(DataManagerBase):
    def find_participants(self):
        participants = []
        for f in glob.glob(f"{self._root}{os.sep}rest_*.eeg"):
            participant = re.match(
                "rest_([0-9]*).eeg", os.path.relpath(f, self._root)
            ).groups()[0]
            if all(
                os.path.exists(os.path.join(self._root, f"rest_{participant}.{ext}"))
                for ext in ["eeg", "vhdr", "vmrk"]
            ):
                participants.append(participant)

        return participants

    @property
    def eegfile(self):
        return os.path.join(self._root, f"rest_{self.participant}.eeg")

    @property
    def vhdrfile(self):
        return os.path.join(self._root, f"rest_{self.participant}.vhdr")

    @property
    def vmrkfile(self):
        return os.path.join(self._root, f"rest_{self.participant}.vmrk")
