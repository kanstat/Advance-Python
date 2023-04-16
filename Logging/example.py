import logging

logging.basicConfig(filename='log.log', level=logging.DEBUG, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',filemode='w')
# logger = logging.getLogger(__name__)

logger = logging.getLogger()

def add(x, y):
    result = x + y
    logger.info(f'Added {x} and {y} to get {result}')
    return result

def subtract(x, y):
    result = x - y
    logger.info(f'Subtracted {y} from {x} to get {result}')
    return result

def multiply(x, y):
    result = x * y
    logger.info(f'Multiplied {x} by {y} to get {result}')
    return result

def divide(x, y):
    try:
        result = x / y
        logger.info(f'Divided {x} by {y} to get {result}')
        return result
    except ZeroDivisionError:
        logger.error('Attempted to divide by zero')
        return None


if __name__ == "__main__":
    result = add(2, 3)
    # Logs: "Added 2 and 3 to get 5"

    result = subtract(5, 1)
    # Logs: "Subtracted 1 from 5 to get 4"

    result = multiply(4, 6)
    # Logs: "Multiplied 4 by 6 to get 24"

    result = divide(10, 0)
    # Logs: "Attempted to divide by zero", returns None
