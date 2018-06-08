from page.index_page import Page

class ExternalPage(Page):

    @property
    def login_link(self):
        return self.driver.find_element_by_css_selector("a[href='/users/login']")

    @property
    def register_link(self):
        return self.driver.find_element_by_css_selector("a[href='/users/register")