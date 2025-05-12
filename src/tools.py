from pathlib import Path


BASE_DIR = Path(__file__).parent.parent / "demo"


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


def read_file(name: str) -> str:
    """
    Read the contents of a file.

    Args:
        name (str): The name of the file to read.
    Returns:
        str: The contents of the file.
    """
    print(f"(read_file) name: {name}")

    file_path = BASE_DIR / name

    try:
        content: str = file_path.read_text()
        return content
    except Exception as e:
        return f"Error reading file {name}: {e}"


tools = [list_files, read_file]


__all__ = ["tools"]