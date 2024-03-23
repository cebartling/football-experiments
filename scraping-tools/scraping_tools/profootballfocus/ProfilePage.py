import os


class ProfilePage:
    def __init__(self, page):
        self.page = page

    def verify_page(self) -> None:
        assert self.page.title() == 'PFF Login'
        print('Page verified')

    def sign_in(self) -> None:
        self.page.fill('input[name="login[email]"]', os.getenv('PRO_FOOTBALL_FOCUS_EMAIL'))
        self.page.fill('input[name="login[password]"]', os.getenv('PRO_FOOTBALL_FOCUS_PASSWORD'))
        self.page.click('button[type="submit"]')
        print(self.page.title())
