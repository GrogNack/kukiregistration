from page.index_page import Page

class InternalPage(Page):

    @property
    def cart_link(self):
        return self.driver.find_element_by_css_selector("a[href='/cart']")

    @property
    def logout_link(self):
        return self.driver.find_element_by_css_selector("a[href='/users/logout']")

    @property
    def edit_link(self):
        return self.driver.find_element_by_css_selector("a[href='/users/edit']")