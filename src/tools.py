from pathlib import Path


BASE_DIR = Path('.')


def list_files() -> list[str]:
    """
    List all files in the base directory.

    Returns:
        list[str]: List of file paths as strings.
    """

    print(f"(list_files) base_dir: {BASE_DIR}")

    file_list = []
    for i in BASE_DIR.iterdir():
        if i.is_file():
            file_list.append(i)

    return file_list


tools = [
    list_files
]

__all__ = [
    "tools",
]