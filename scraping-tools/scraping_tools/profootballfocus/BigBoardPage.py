import os


class BigBoardPage:

    def __init__(self, page):
        self.page = page

    def goto(self):
        self.page.goto(os.getenv('PRO_FOOTBALL_FOCUS_BIG_BOARD_URL'))

    def verify_page(self):
        assert self.page.title() == 'NFL Draft Big Board | PFF'

    def select_slim_mode(self):
        self.page.get_by_text("View THICC").first.click()
        self.page.get_by_text("SLIM").first.click()

    def get_players(self) -> list[list[str]]:
        rows = self.page.locator('div.g-card__content').all()
        players = []
        for row in rows:
            rank = row.locator('span.g-label').first.text_content()
            name = row.locator('button').first.text_content()
            position = row.locator('span').all()[1].text_content()
            school = row.locator('span').all()[2].text_content()
            players.append([name, position, school, rank])
        return players
