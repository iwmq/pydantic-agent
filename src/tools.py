from pathlib import Path
import subprocess


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


def create_file(name: str, content: str) -> str:
    """
    Create a new file with the given name and content.

    Args:
        name (str): The name of the file to create.
        content (str): The content to write to the file.
    Returns:
        str: Success or error message.
    """
    print(f"(create_file) name: {name}, content: {content}")

    file_path = BASE_DIR / name

    try:
        file_path.write_text(content)
        return f"File {name} created successfully"
    except Exception as e:
        return f"Error creating file {name}: {e}"


def replace_in_file(name: str, start: int, end: int, content: str) -> str:
    """
    Replace a range of lines in a file with new content.

    Args:
        name (str): The name of the file to modify.
        start (int): The starting line number (1-indexed).
        end (int): The ending line number (1-indexed).
        content (str): The new content to insert.
    Returns:
        str: Success or error message.
    """
    print(f"(replace_in_file) name: {name}, start: {start}, end: {end}, content: {content}")

    file_path = BASE_DIR / name

    try:
        lines = file_path.read_text().splitlines()
        new_lines = content.splitlines()
        lines[start - 1:end] = new_lines
        file_path.write_text("\n".join(lines))
        return f"Lines {start} to {end} in {name} replaced successfully"
    except Exception as e:
        return f"Error replacing lines in file {name}: {e}"


def run_python(script_path: str) -> str:
    """
    Run a Python script.

    Args:
        script_path (str): The path to the Python script to run.
    Returns:
        str: The output of the script.
    """
    print(f"(run_python) script_path: {script_path}")

    try:
        result = subprocess.run(
            ["python", script_path],
            capture_output=True,
            text=True,
            check=True
        )
        return result.stdout
    except subprocess.CalledProcessError as e:
        return f"Error running script {script_path}: {e.stderr}"


tools = [
    list_files,
    read_file,
    rename_file,
    delete_file,
    create_file,
    replace_in_file,
    run_python
]


__all__ = ["tools"]