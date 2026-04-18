from os import path
from pathlib import Path


from utils.copy_util import clean_public, copy_static_to_public


def main():
    current_file_path = path.realpath(__file__)
    root_dir = Path(path.dirname(current_file_path)).parent
    public_path = root_dir.joinpath("public")
    static_path = root_dir.joinpath("static")
    clean_public(public_path)
    copy_static_to_public(c_public_path=public_path, c_static_path=static_path)


main()
