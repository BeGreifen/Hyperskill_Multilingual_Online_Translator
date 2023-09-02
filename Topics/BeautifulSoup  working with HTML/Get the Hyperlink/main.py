import requests
import inspect
import logging
from bs4 import BeautifulSoup


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
def get_input() -> (int, str):
    return_id: int = int(input()) or 1
    return_url = "https://cogniterra.org/media/attachments/lesson/24996/4._Pygmalion.htm"
    return_url: str = str(input()) or return_url
    return return_id, return_url


@logger
def get_soup(url) -> BeautifulSoup:
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    return soup


@logger
def get_act(soup, bookmark: int) -> str:
    # Find the link with name attribute equal to 'act1'
    link = soup.find('a', attrs={'name': bookmark})
    anchors = soup.find_all('a')
    # Get the address of the link
    return anchors[bookmark-1].get('href')


def main() -> None:
    html_act_id, html_url = get_input()
    beautiful_soup = get_soup(html_url)
    print(get_act(beautiful_soup, html_act_id))


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO,
                        format='%(asctime)s - %(levelname)s - %(message)s',
                        filename='app.log',  # Specify the file name for logging
                        filemode='w'  # Use 'w' mode to overwrite the log file on each run, or 'a' to append
                        )
    main()
