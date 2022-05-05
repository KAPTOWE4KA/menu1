import datetime


def bank_history_decorator(f):
    def inner(*args, **kwargs):
        print('-*' * 10+'-')
        result = f(*args, **kwargs)
        print('-*' * 10+'-')
        return result
    return inner


def simple_logger(f):
    def inner(*args, **kwargs):
        result = f(*args, **kwargs)
        try:
            logger = open("log_"+datetime.date.today().__str__()+".txt","a+",encoding="utf-8")
            logger.write(datetime.datetime.now().__str__()+" >>> Function invoking: "+f.__name__+"")
            if args is not None:
                logger.write(f"\tArgs: {args}")
            if kwargs is not None:
                logger.write(f"\tKwargs: {kwargs}\n")
            logger.close()
        except Exception as e:
            print("Ошибка логгера: "+e.__str__())
        return result
    return inner