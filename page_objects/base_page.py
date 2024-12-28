from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from conftest import driver


class BasePageBurgers:

    def __init__(self, driver):
        self.driver = driver

    def go_to_page(self, page):
        self.driver.get(page)

    def driver_find_element(self, locator):
        return self.driver.find_element(*locator)

    def driver_find_elements(self, locator):
        return self.driver.find_elements(*locator)

    def driver_wait_for_visibile_element(self, locator, time=10):
        WebDriverWait(self.driver, time).until(expected_conditions.visibility_of_element_located(locator))

    def driver_wait_for_clickable_element(self, locator, time=10):
        WebDriverWait(self.driver, time).until(expected_conditions.element_to_be_clickable(locator))

    def driver_click_element(self, element):
        self.driver.execute_script("arguments[0].click();", element)

    def driver_send_keys_to_element(self, element, info):
        element.send_keys(info)

    def driver_scroll_to_element(self, element):
        self.driver.execute_script("return arguments[0].scrollIntoView(true);", element)

    def driver_current_url(self):
        return self.driver.current_url

    def driver_drag_and_drop_element(self, source_element, target_element):
        script = """

        function
        simulateHTML5DragAndDrop(sourceNode, destinationNode)
        {
        var
        dataTransfer = new
        DataTransfer();
        var
        dragStartEvent = new
        DragEvent('dragstart', {
            bubbles: true,
            cancelable: true,
            dataTransfer: dataTransfer
        });
        sourceNode.dispatchEvent(dragStartEvent);

        var
        dropEvent = new
        DragEvent('drop', {
            bubbles: true,
            cancelable: true,
            dataTransfer: dataTransfer
        });

        destinationNode.dispatchEvent(dropEvent);

        var
        dragEndEvent = new
        DragEvent('dragend', {
            bubbles: true,
            cancelable: true,
            dataTransfer: dataTransfer
        });
        sourceNode.dispatchEvent(dragEndEvent);
        }

        simulateHTML5DragAndDrop(arguments[0], arguments[1]);
        """

        self.driver.execute_script(script, source_element, target_element)
