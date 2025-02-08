import time
from functools import wraps
from typing import Any, Callable, Optional


def log(filename: Optional[str] = None) -> Callable:
    """
    Декоратор log, который будет автоматически записывать в лог начало и конец выполнения функции,
    а также ее результаты или возникшие ошибки
    """

    def my_decorator(func: Any) -> Any:
        @wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            """
            Декоратор, определяющий параметры функции, применяемой во внешнем декораторе
            """
            start_time = time.time()
            try:
                result = func(*args, **kwargs)
                end_time = time.time()
                log_message = (
                    f"{func.__name__} started at {start_time} and finished at {end_time} with result: {result}"
                )
                if filename is not None:
                    with open(filename, "a", encoding="utf-8") as file:
                        file.write(f"{func.__name__} ok\n")
                else:
                    print(log_message)

            except Exception as e:
                log_message_1 = f"{func.__name__} error {e.__class__.__name__}. Inputs: {args}, {kwargs}"
                if filename:
                    with open(filename, "a", encoding="utf-8") as file:
                        file.write(log_message_1 + "\n")
                else:
                    print(log_message_1)
                raise e
            return result

        return wrapper

    return my_decorator


@log(filename="mylog.txt")
def my_function(x: Any, y: Any) -> Any:
    """
    Результат суммирования двух чисел
    """
    return x + y


my_function(1, 2)
