"""
Модуль DataManager отвечает за работу с файлом.
"""
from pathlib import Path


class DataManager:
    def __init__(self, filename: str):
        self._filename = filename
        if not Path(self._filename).is_file():
            with open(self._filename, 'w'):
                pass

    def add_line(self, line: str):
        """Метод добавляет строку в конец файла"""
        with open(self._filename, 'a', encoding='UTF-8') as file:
            file.write(line)

    def rewrite(self, lines: list):
        """Метод перезаписывает файл"""
        with open(self._filename, 'w', encoding='UTF-8') as file:
            file.writelines(lines)

    def read(self) -> list:
        """Метод читает файл и возвращает список строк"""
        with open(self._filename, encoding='UTF-8') as file:
            return [line.strip() for line in file]
