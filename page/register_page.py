from page.external_page import ExternalPage


class RegisterPage(ExternalPage):

    @property
    def username_field(self):
        return self.driver.find_element_by_id("user_email")

    @property
    def password_field(self):
        return self.driver.find_element_by_id("user_password")

    @property
    def confirm_password_field(self):
        return self.driver.find_element_by_id("user_password_confirmation")

    @property
    def submit_button(self):
        return self.driver.find_element_by_name("commit")