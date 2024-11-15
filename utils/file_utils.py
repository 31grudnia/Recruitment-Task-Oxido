from typing import Optional
import requests
import os


def download_file(url: str, file_path: str) -> None:

    os.makedirs(os.path.dirname(file_path), exist_ok=True)
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()  

    except requests.exceptions.RequestException as req_err:
        print(f"Błąd podczas pobierania pliku: {req_err}")
        return None

    try:
        with open(file_path, "wb") as file:
            file.write(response.content)
        print(f"Plik został zapisany jako {file_path}")

    except IOError as io_err:
        print(f"Błąd podczas zapisu pliku: {io_err}")


def read_file(file_path: str) -> Optional[str]:
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            return file.read()
        
    except FileNotFoundError:
        print("Plik nie został znaleziony.")
        return None
    except IOError as io_err:
        print(f"Błąd podczas odczytu pliku: {io_err}")
        return None
