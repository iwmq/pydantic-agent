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


def rename_file(name: str, new_name: str) -> str:
    """
    Rename a file.

    Args:
        name (str): The name of the file to rename.
        new_name (str): The new name for the file.
    Returns:
        str: Success or error message.
    """
    print(f"(rename_file) name: {name}, new_name: {new_name}")

    file_path = BASE_DIR / name
    new_file_path = BASE_DIR / new_name

    try:
        file_path.rename(new_file_path)
        return f"File renamed from {name} to {new_name}"
    except Exception as e:
        return f"Error renaming file {name}: {e}"


def delete_file(name: str) -> str:
    """
    Delete a file.

    Args:
        name (str): The name of the file to delete.
    Returns:
        str: Success or error message.
    """
    print(f"(delete_file) name: {name}")

    file_path = BASE_DIR / name

    try:
        file_path.unlink()
        return f"File {name} deleted successfully"
    except Exception as e:
        return f"Error deleting file {name}: {e}"


tools = [list_files, read_file, rename_file, delete_file]


__all__ = ["tools"]