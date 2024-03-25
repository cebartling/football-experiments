from dotenv import load_dotenv
from playwright.sync_api import sync_playwright

from scraping_tools.ras_football.RasQueryPage import RasQueryPage

load_dotenv()



class Driver:
    def __init__(self):
        pass

    def execute(self) -> None:
        with sync_playwright() as p:
            browser = p.chromium.launch(headless=False)
            page = browser.new_page()
            ras_query_page = RasQueryPage(page)

            ras_query_page.goto()
            ras_query_page.verify_page()
            ras_query_page.query()
            browser.close()

            # with open('pff_big_board_players.csv', 'w') as f:
            #     f.write('Name,Position,School,Rank\n')
            #     for player in players:
            #         f.write(','.join(player) + '\n')
