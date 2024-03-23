from dotenv import load_dotenv
from playwright.sync_api import sync_playwright

from scraping_tools.profootballfocus.AuthenticationPage import AuthenticationPage
from scraping_tools.profootballfocus.BigBoardPage import BigBoardPage

load_dotenv()


class Driver:
    def __init__(self):
        pass

    def execute(self) -> None:
        with sync_playwright() as p:
            browser = p.chromium.launch()
            page = browser.new_page()

            authentication_page = AuthenticationPage(page)
            big_board_page = BigBoardPage(page)

            authentication_page.goto()
            authentication_page.verify_page()
            authentication_page.sign_in()

            big_board_page.goto()
            big_board_page.verify_page()
            big_board_page.select_slim_mode()
            big_board_page.process_player_rows()

            # page.pause()
            browser.close()
