"""
Sort files based on extensions
"""

from pathlib import Path
from shutil import copyfile

source = "picture"
output = "Backup/"

def read_folder(path: Path) -> None:
    for el in path.iterdir():
        if el.is_dir():
            read_folder(el)
        else:
            copy_file(el)


def copy_file(file: Path) -> None:
    ext = file.suffix
    new_path = output_folder / ext
    new_path.mkdir(exist_ok=True, parents=True)
    copyfile(file, new_path / file.name)


output_folder = Path(output)  # dist
read_folder(Path(source))
