import unittest
from unittest.mock import patch, mock_open, MagicMock
import requests

from utils.file_utils import download_file, read_file


class TestFileUtils(unittest.TestCase):

    @patch('requests.get')
    def test_download_file_success(self, mock_get):
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.content = b'Test content'
        mock_get.return_value = mock_response

        with patch('builtins.open', mock_open()) as mocked_file:
            download_file('http://example.com/file.txt', 'data/articles/file.txt')
            mocked_file.assert_called_once_with('data/articles/file.txt', 'wb')
            mocked_file().write.assert_called_once_with(b'Test content')

    @patch('requests.get')
    def test_download_file_http_error(self, mock_get):
        mock_get.side_effect = requests.exceptions.HTTPError('HTTP Error')
        with patch('builtins.print') as mock_print:
            download_file('http://example.com/file.txt', 'data/articles/file.txt')
            mock_print.assert_called_with('Błąd podczas pobierania pliku: HTTP Error')

    @patch('requests.get')
    def test_download_file_connection_error(self, mock_get):
        mock_get.side_effect = requests.exceptions.ConnectionError('Connection Error')
        with patch('builtins.print') as mock_print:
            download_file('http://example.com/file.txt', 'data/articles/file.txt')
            mock_print.assert_called_with('Błąd podczas pobierania pliku: Connection Error')

    @patch('builtins.open', new_callable=mock_open, read_data='File content')
    def test_read_file_success(self, mock_file):
        result = read_file('data/articles/file.txt')
        self.assertEqual(result, 'File content')
        mock_file.assert_called_once_with('data/articles/file.txt', 'r', encoding='utf-8')

    @patch('builtins.open', side_effect=FileNotFoundError)
    def test_read_file_not_found(self, mock_file):
        with patch('builtins.print') as mock_print:
            result = read_file('data/articles/nonexistent.txt')
            mock_print.assert_called_with('Plik nie został znaleziony.')
            self.assertIsNone(result)

    @patch('builtins.open', side_effect=IOError('Read Error'))
    def test_read_file_io_error(self, mock_file):
        with patch('builtins.print') as mock_print:
            result = read_file('data/articles/file.txt')
            mock_print.assert_called_with('Błąd podczas odczytu pliku: Read Error')
            self.assertIsNone(result)


if __name__ == '__main__':
    unittest.main()
