#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Ядро
"""

# ######################################################################################################################
# Импорт необходимых инструментов
# ######################################################################################################################
# Подавление Warning
import warnings
for warn in [UserWarning, FutureWarning]: warnings.filterwarnings('ignore', category = warn)

from dataclasses import dataclass # Класс данных

import prettytable  # Отображение таблиц в терминале
import colorama     # Цветной текст терминала
import numpy as np  # Научные вычисления
import pandas as pd # Обработка и анализ данных

from datetime import datetime       # Работа со временем
from prettytable import PrettyTable # Отображение таблиц в терминале

# Персональные
from test_docs_python.modules.core.settings import Settings # Глобальный файл настроек

# ######################################################################################################################
# Сообщения
# ######################################################################################################################
@dataclass
class CoreMessages(Settings):
    """Класс для сообщений"""

    # ------------------------------------------------------------------------------------------------------------------
    # Конструктор
    # ------------------------------------------------------------------------------------------------------------------

    def __post_init__(self):
        super().__post_init__() # Выполнение конструктора из суперкласса

        self._libs_vers: str = self._('Версии установленных библиотек') + self._em
        self._package: str = self._('Пакет')

# ######################################################################################################################
# Ядро модулей
# ######################################################################################################################
@dataclass
class Core(CoreMessages):
    """Класс-ядро модулей"""

    # ------------------------------------------------------------------------------------------------------------------
    # Конструктор
    # ------------------------------------------------------------------------------------------------------------------

    def __post_init__(self):
        super().__post_init__() # Выполнение конструктора из суперкласса

    # ------------------------------------------------------------------------------------------------------------------
    # Внешние методы (сообщения)
    # ------------------------------------------------------------------------------------------------------------------

    def inv_args(self, class_name: str, build_name: str, out: bool = True) -> None:
        """Сообщение об указании неверных типов аргументов

        Args:
            class_name (str): Имя класса
            build_name (str): Имя метода/функции
            out (bool): Печатать процесс выполнения

        Returns:
            None
        """

        if type(out) is not bool: out = True

        try:
            # Проверка аргументов
            if type(class_name) is not str or not class_name or type(build_name) is not str or not build_name:
                raise TypeError
        except TypeError: class_name, build_name = __class__.__name__, self.inv_args.__name__

        inv_args = self._invalid_arguments.format(class_name + '.' + build_name)

        if out is True:
            print('[{}{}{}] {}'.format(
                self.color_red, datetime.now().strftime(self._format_time), self.text_end, inv_args
            ))

    def message_info(self, message: str, space: int = 0, out: bool = True) -> None:
        """Информационное сообщение

        Args:
            message (str): Сообщение
            space (int): Количество пробелов в начале текста
            out (bool): Отображение

        Returns:
            None
        """

        if type(out) is not bool: out = True

        try:
            # Проверка аргументов
            if type(message) is not str or not message: raise TypeError
        except TypeError: self.inv_args(__class__.__name__, self.message_info.__name__, out = out); return None

        if out is True: print('[{}] {}'.format(datetime.now().strftime(self._format_time), message))

    # ------------------------------------------------------------------------------------------------------------------
    # Внешние методы
    # ------------------------------------------------------------------------------------------------------------------

    def libs_vers(self, out: bool = True) -> bool:
        """Получение и отображение версий установленных библиотек

        Args:
            out (bool): Отображение

        Returns:
            bool: **True** если версии установленных библиотек отображены, в обратном случае **False**
        """

        # Сброс
        self._df_pkgs = pd.DataFrame() # Пустой DataFrame

        try:
            # Проверка аргументов
            if type(out) is not bool: raise TypeError
        except TypeError: self.inv_args(__class__.__name__, self.libs_vers.__name__, out = out); return False
        else:
            pkgs = {
                'Package': [
                    'NumPy', 'Pandas', 'Colorama', 'Prettytable'
                ],
                'Version': [i.__version__ for i in [
                    np, pd, colorama, prettytable
                ]]
            }

            self._df_pkgs = pd.DataFrame(data = pkgs) # Версии используемых библиотек
            self._df_pkgs.index += 1

            # Вывод сообщения
            if out is True:
                table_terminal = PrettyTable()
                table_terminal.add_column(self._package, self._df_pkgs['Package'].values)
                table_terminal.add_column(self._metadata[3], self._df_pkgs['Version'].values)
                table_terminal.align = 'l'

                self.message_info(self._libs_vers, space = 0, out = out)
                print(table_terminal)