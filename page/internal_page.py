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

    @property
    def count_of_film(self):
        return self.driver.find_element_by_css_selector("span.cart-count")

    # @property
    # def is_this_page(self):
    #     return self.driver.find_element_by_link_text()