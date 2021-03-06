import os

from decorators import simple_logger as logged


@logged
def load_bill(filename="bill.txt"):
    if os.path.exists(filename):
        bill_f = open(filename, "r", encoding="utf-8")
        try:
            bill = int(bill_f.readline())
            bill_f.close()
            return bill
        except Exception as e:
            return e
    else:
        bill_f = open(filename, "w", encoding="utf-8")
        bill_f.write("0")
        bill_f.close()
        return 0


@logged
def save_bill(newbill, filename="bill.txt"):
    bill_f = open(filename, "w", encoding="utf-8")
    if isinstance(newbill, int):
        bill_f.write(str(newbill))
        bill_f.close()
        return True
    else:
        return False


@logged
def load_history(filename="history.txt"):
    if os.path.exists(filename):
        hist_f = open(filename, "r", encoding="utf-8")
        history = []
        try:
            for line in hist_f:
                name, cost = line.split(':')
                history.append([name, int(str(cost).strip('\n'))])
            return history
        except Exception as e:
            return e
    else:
        return 0


@logged
def save_history(hist_append, filename="history.txt"):
    hist_f = open(filename, "w", encoding="utf-8")
    try:
        for name, cost in hist_append:
            hist_f.write(str(name)+":"+str(cost)+"\n")
        hist_f.close()
        return True
    except Exception as e:
        return e
