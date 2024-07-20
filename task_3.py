import sys
from pathlib import Path
from colorama import init, Fore, Style

init(autoreset=True)


def print_directory_structure(directory, prefix=""):
    try:
        entries = list(directory.iterdir())
    except PermissionError:
        print(Fore.RED + f"{prefix}[Permission Denied]")
        return

    entries.sort()
    for index, entry in enumerate(entries):
        connector = "└── " if index == len(entries) - 1 else "├── "
        if entry.is_dir():
            print(Fore.BLUE + f"{prefix}{connector}{entry.name}")
            print_directory_structure(
                entry, prefix + ("    " if index == len(entries) - 1 else "│   "))
        else:
            print(Fore.GREEN + f"{prefix}{connector}{entry.name}")


def main():
    if len(sys.argv) != 2:
        print(Fore.RED + "Usage: python hw03.py <directory_path>")
        return

    directory_path = Path(sys.argv[1])

    if not directory_path.exists():
        print(Fore.RED + f"Error: The path '{directory_path}' does not exist.")
        return

    if not directory_path.is_dir():
        print(
            Fore.RED + f"Error: The path '{directory_path}' is not a directory.")
        return

    print(Fore.YELLOW + f"Directory structure of '{directory_path}':")
    print_directory_structure(directory_path)


if __name__ == "__main__":
    main()
