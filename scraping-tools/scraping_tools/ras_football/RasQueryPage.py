import os


class RasQueryPage:

    def __init__(self, page):
        self.page = page

    def goto(self):
        self.page.goto(os.getenv('RAS_URL'))

    def verify_page(self):
        assert self.page.title().startswith('RASRelative Athletic Scores')

    def query(self):
        self.page.get_by_placeholder('1987').first.fill('2024')
        self.page.get_by_placeholder('2024').first.fill('2024')
        self.page.select_option('#nt_cf_1_table_77073', 'FS')
        self.page.pause()

    # def select_slim_mode(self):
    #     self.page.get_by_text("View THICC").first.click()
    #     self.page.get_by_text("SLIM").first.click()
    #
    # def get_players(self) -> list[list[str]]:
    #     rows = self.page.locator('div.g-card__content').all()
    #     players = []
    #     for row in rows:
    #         rank = row.locator('span.g-label').first.text_content()
    #         name = row.locator('button').first.text_content()
    #         position = row.locator('span').all()[1].text_content()
    #         school = row.locator('span').all()[2].text_content()
    #         players.append([name, position, school, rank])
    #     return players
