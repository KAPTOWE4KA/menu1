import os.path

from main import buy, author_name, create_folder


def test_author_name():
    assert author_name() == "Создатель программы: KAPTOWE4KA"


def test_buy():
    assert buy(100,25) == 75
    assert buy(100, 25) == 75


def test_menu_askdef():
    if os.path.exists('testdirtest'):
        os.rmdir('testdirtest')
    assert create_folder('testdirtest') == 1

