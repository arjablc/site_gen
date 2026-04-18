from pathlib import Path
import shutil
import os


def copy_static_to_public(c_public_path: Path, c_static_path: Path):
    contents = os.listdir(c_static_path)
    print(f"contents: {contents}")
    for content in contents:
        content_path = c_static_path.joinpath(content)  # static one
        print(f"content path: {content_path}")
        if os.path.isdir(content_path):
            print("folder: recursive")
            content_path_p = c_public_path.joinpath(content)
            print(f"public content path: {content_path_p}")
            os.mkdir(content_path_p)
            copy_static_to_public(content_path_p, content_path)
        else:
            print("file: copying")
            content_path_p = c_public_path.joinpath(content)
            shutil.copyfile(content_path, content_path_p)


def clean_public(public_path):
    print("==Deleting public==")
    if os.path.exists(public_path):
        shutil.rmtree(public_path)
    print("==Public deleted==")
    os.mkdir(path=public_path)
    print("==Public created==")
