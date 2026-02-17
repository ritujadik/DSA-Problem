import logging


def add(a,b):
    return a + b

def divide(a,b):
    try:
        result = a/b
        logging.info(f"Division Successful: {a}/{b} = {result}")
        return result
    except ZeroDivisionError as e:
        logging.error(f"Error occured:{e},exc_info=True")
    except Exception as e:
        logging.critical(f"Unexpected error:{e}",exc_info=True)


print(divide(10,5))
print(divide(10,0))
print(divide("a",5))