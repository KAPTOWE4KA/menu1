import os

from file_manager import save_bill, save_history, load_bill, load_history


def test_save_bill():
    assert save_bill(500, "test_bill.txt") == True
    assert save_bill("ddd", "test_bill.txt") == False
    os.remove("test_bill.txt")


def test_save_history():
    assert save_history([["name", 150], ["name", 20]], "test_history.txt") == True
    assert isinstance(save_history(["name", 150, 22222], "test_history.txt"), Exception)
    os.remove("test_history.txt")


def test_load_bill():
    assert load_bill() == 0


def test_load_history():
    assert load_history() == 0
