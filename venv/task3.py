import sys
from pathlib import Path
from colorama import init, Fore, Style

def print_directory_structure(directory, indent=""):
    try:
        for path in sorted(directory.iterdir()):
            if path.is_dir():
                print(f"{indent}{Fore.BLUE}{path.name}{Style.RESET_ALL}/")
                print_directory_structure(path, indent + "  ")
            else:
                print(f"{indent}{Fore.GREEN}{path.name}{Style.RESET_ALL}")
    except PermissionError:
        print(f"{indent}{Fore.RED}Permission denied{Style.RESET_ALL}")

def main():
    if len(sys.argv) != 2:
        print("Usage: python hw03.py <directory_path>")
        return

    directory_path = Path(sys.argv[1])

    if not directory_path.exists():
        print(f"The path {directory_path} does not exist.")
        return

    if not directory_path.is_dir():
        print(f"The path {directory_path} is not a directory.")
        return

    init(autoreset=True)
    print_directory_structure(directory_path)

if __name__ == "__main__":
    main()
