from utils.file_utils import download_file, read_file
from utils.html_utils import save_article_html, create_preview_html
from utils.openai_utils import prepare_prompt, openai_prompt

from config import OPENAI_API_KEY, ARTICLES_STORAGE_PATH, HTML_FILEPATH


if __name__ == "__main__":

    article_html_path = HTML_FILEPATH + "artykul.html"
    file_path = ARTICLES_STORAGE_PATH + "article.txt"
    url = "https://cdn.oxido.pl/hr/Zadanie%20dla%20JJunior%20AI%20Developera%20-%20tresc%20artykulu.txt"

    download_file(url, file_path)
    article_text = read_file(file_path)
    
    if article_text:
        prompt = prepare_prompt(article_text)
        html_content = openai_prompt(prompt)
        
        if html_content:
            save_article_html(html_content, article_html_path)
        else:
            print("Nie udało się uzyskać odpowiedzi od OpenAI.")
    else:
        print("Nie udało się odczytać artykułu.")

    template_content = (
        '<!DOCTYPE html>\n'
        '<html lang="pl">\n'
        '<head>\n'
        '    <meta charset="UTF-8">\n'
        '    <title>Szablon Artykułu</title>\n'
        '    <!-- Możesz dodać tutaj style i skrypty JS -->\n'
        '    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css">\n'
        '</head>\n'
        '<body>\n'
        '    <!-- Tutaj wklej wygenerowany kod artykułu -->\n'
        '</body>\n'
        '</html>'
    )
    save_article_html(template_content, "templates/szablon.html")
    
    create_preview_html("templates/szablon.html", article_html_path, "podglad.html")

