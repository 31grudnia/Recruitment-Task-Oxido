
from utils.file_utils import download_file, read_file
from config import OPENAI_API_KEY, ARTICLES_STORAGE_PATH


if __name__ == "__main__":

    file_path = ARTICLES_STORAGE_PATH + "article.txt"
    url = "https://cdn.oxido.pl/hr/Zadanie%20dla%20JJunior%20AI%20Developera%20-%20tresc%20artykulu.txt"

    download_file(url, file_path)
    tekst_artykulu = read_file(file_path)
    
    if tekst_artykulu is not None:
        print("Treść artykułu:")
        print(tekst_artykulu)
    else:
        print("Nie udało się odczytać artykułu.")