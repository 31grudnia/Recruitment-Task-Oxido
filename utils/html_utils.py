

def save_article_html(html_content: str, file_path: str) -> None:

    try:
        with open(file_path, "w", encoding="utf-8") as file:
            file.write(html_content)
        print(f"Artykuł został zapisany w pliku {file_path}")

    except IOError as io_err:
        print(f"Błąd podczas zapisu pliku: {io_err}")


def create_preview_html(template_path: str, article_html_path: str, output_path: str) -> None:
    try:
        with open(template_path, "r", encoding="utf-8") as template_file:
            template_content = template_file.read()

        with open(article_html_path, "r", encoding="utf-8") as article_file:
            article_content = article_file.read()

        full_content = template_content.replace(
            "<body>\n    <!-- Tutaj wklej wygenerowany kod artykułu -->\n</body>",
            f"<body>\n{article_content}\n</body>"
        )

        with open(output_path, "w", encoding="utf-8") as output_file:
            output_file.write(full_content)

        print(f"Podgląd artykułu został zapisany w pliku {output_path}")
    except IOError as io_err:
        print(f"Błąd podczas tworzenia podglądu artykułu: {io_err}")
