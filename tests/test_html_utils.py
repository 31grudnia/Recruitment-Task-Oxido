import unittest
from unittest.mock import mock_open, patch, call

from utils.html_utils import save_article_html, create_preview_html


class TestFileUtils(unittest.TestCase):

    @patch('builtins.open', new_callable=mock_open)
    def test_save_article_html_success(self, mock_file):
        html_content = "<h1>Tytuł Artykułu</h1>"
        file_path = "templates/artykul.html"

        save_article_html(html_content, file_path)

        mock_file.assert_called_once_with(file_path, "w", encoding="utf-8")
        mock_file().write.assert_called_once_with(html_content)

    @patch('builtins.print')
    @patch('builtins.open', side_effect=IOError("Błąd zapisu"))
    def test_save_article_html_io_error(self, mock_file, mock_print):
        html_content = "<h1>Tytuł Artykułu</h1>"
        file_path = "templates/artykul.html"

        save_article_html(html_content, file_path)

        mock_print.assert_called_with("Błąd podczas zapisu pliku: Błąd zapisu")

    @patch('builtins.print')
    @patch('builtins.open', side_effect=IOError("Błąd odczytu"))
    def test_create_preview_html_io_error(self, mock_file, mock_print):
        template_path = "templates/szablon.html"
        article_html_path = "templates/artykul.html"
        output_path = "podglad.html"

        create_preview_html(template_path, article_html_path, output_path)

        mock_print.assert_called_with("Błąd podczas tworzenia podglądu artykułu: Błąd odczytu")


if __name__ == '__main__':
    unittest.main()
