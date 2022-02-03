import datetime
import sys
from time import sleep, time

from scrapers.scraper import (
    connect_to_base,
    get_driver,
    parse_html,
    write_to_file,
)


def run_process(filename, browser):
    if connect_to_base(browser):
        sleep(2)
        html = browser.page_source
        output_list = parse_html(html)
        write_to_file(output_list, filename)
    else:
        print("Error connecting to Wikipedia")


if __name__ == "__main__":

    # headless mode?
    headless = False
    if len(sys.argv) > 1 and sys.argv[1] == "headless":
        print("Running in headless mode")
        headless = True

    # set variables
    start_time = time()
    output_timestamp = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
    output_filename = f"output_{output_timestamp}.csv"

    # init browser
    browser = get_driver(headless=headless)

    # scrape and crawl
    for current_attempt in range(1, 21):
        print(f"Scraping Wikipedia #{current_attempt} time(s)...")
        run_process(output_filename, browser)
    # exit
    browser.quit()
    end_time = time()
    elapsed_time = end_time - start_time
    print(f"Elapsed run time: {elapsed_time} seconds")
