import click
import glob
import os
import shutil


def _copy_notebooks(target):
    # Ensure directory existence
    os.makedirs(target, exist_ok=True)

    # Locate the notebooks in the Python installation tree
    notebook_dir = os.path.join(os.path.dirname(__file__), "notebooks")
    notebooks = glob.glob(os.path.join(notebook_dir, "*.ipynb"))

    for notebook in notebooks:
        shutil.copy(notebook, target)


@click.command()
@click.argument(
    "target",
    type=click.Path(exists=True, file_okay=False, writable=True),
    default=os.getcwd(),
)
def copy_notebooks(target=None):
    """Copy all shipped CNSR notebooks to a given target location"""

    _copy_notebooks(target)


@click.command()
@click.argument(
    "prefix", type=click.Path(file_okay=False, writable=True), required=True
)
def install_cnsr_launcher_data(prefix=None):
    """Install all CNSR launcher data into the Jupyter environment"""

    # Define the paths where to install stuff
    jupyter_dir = os.path.join(prefix, "share", "jupyter")
    config_dir = os.path.join(jupyter_dir, "jupyter_app_launcher")
    notebook_dir = os.path.join(jupyter_dir, "cnsr")

    # Copy all notebooks
    _copy_notebooks(notebook_dir)

    # Copy the launcher config
    config = os.path.join(
        os.path.dirname(__file__), "jupyter_app_launcher", "config.yaml"
    )
    os.makedirs(config_dir, exist_ok=True)
    shutil.copy(config, config_dir)


if __name__ == "__main__":
    install_cnsr_launcher_data()
