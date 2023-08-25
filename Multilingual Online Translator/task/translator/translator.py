import logging
import inspect

DEBUG_TRANSLATOR = False


# write your code here
def logger(func):
    def wrap(*args, **kwargs):
        logging.info(
            "%s - line no: %s with args: %s, kwargs: %s",
            func.__name__,
            inspect.getframeinfo(inspect.currentframe().f_back).lineno,
            args,
            kwargs)

        # Call the original function
        result = func(*args, **kwargs)

        # Log the return value
        logging.info("%s returned: %s",
                     func.__name__,
                     result)
        # Return the result
        return result

    return wrap


@logger
def stage1() -> None:
    # steps need to solve stage 1
    target_language: str = input('Type "en" if you want to translate from French into English,'
                                 ' or "fr" if you want to translate from English into French:')
    if target_language != "en":
        target_language = "fr"
    word_to_translate: str = input('Type the word you want to translate')
    print(f'You chose "{target_language}" as a language to translate "{word_to_translate}".')


@logger
def main():
    stage1()


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO,
                        format='%(asctime)s - %(levelname)s - %(message)s',
                        filename='app.log',  # Specify the file name for logging
                        filemode='w'  # Use 'w' mode to overwrite the log file on each run, or 'a' to append
                        )
    main()
