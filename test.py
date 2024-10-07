from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import unittest

class EventRegistrationTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # Initialize the webdriver
        cls.driver = webdriver.Chrome()  # Make sure you have ChromeDriver installed
        cls.driver.get("http://127.0.0.1:5500/index.html")  # Update the path to your local file

    def test_manual_submission(self):
        # Let user manually fill out the form
        input("Fill out the form manually and press Enter...")

        # After submitting the form, continue checking
        try:
            # Wait for confirmation message
            confirmation = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((By.ID, "confirmationMessage"))
            )
            self.assertTrue(confirmation.is_displayed())
            print("Test Passed: Registration successful message is displayed.")
        except Exception as e:
            print(f"Test Failed: Confirmation message not found. Error: {str(e)}")

    @classmethod
    def tearDownClass(cls):
        # Keep the browser open for user to inspect the page before closing
        input("Press Enter to close the browser...")
        cls.driver.quit()

if __name__ == "__main__":
    unittest.main()
