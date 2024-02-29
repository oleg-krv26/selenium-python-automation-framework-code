import pytest
import softest
from pages.yatra_launch_page import LaunchPage
from utilities.utils import Utils
from ddt import ddt, data, unpack, file_data


@pytest.mark.usefixtures("setup")
@ddt
class TestSearchAndVerifyFilter(softest.TestCase):
    log = Utils.cust_logger()

    @pytest.fixture(autouse=True)
    def class_setup(self):
        self.lp = LaunchPage(self.driver)
        self.ut = Utils()

    # @data(("New Delhi", "JFK", "24/03/2024", "1 Stop"), ("BOM", "JFK", "28/03/2024", "2 Stop"))
    # @unpack
    # @file_data("../testdata/testdata.json")
    # @file_data("../testdata/testyml.yaml")
    # @data(*Utils.read_data_from_excel("C:\\Python-selenium\\testFrameworkDemo\\testdata\\tdataexcel.xlsx", "Sheet1"))
    @data(*Utils.read_data_from_csv("C:\\Python-selenium\\testFrameworkDemo\\testdata\\tdatacsv.csv"))
    @unpack
    def test_search_flights_1_stop(self, goingfrom, goingto, date, stops):
        search_flight_result = self.lp.searchFlights(goingfrom, goingto, date)
        self.lp.page_scroll()
        search_flight_result.filter_flights_by_stop(stops)
        allstops1 = search_flight_result.get_search_flight_results()
        self.log.info(len(allstops1))
        self.ut.assertListItemText(allstops1, stops)

    # def test_search_flights_2_stops(self):
    #     search_flight_result = self.lp.searchFlights("New Delhi", "JFK", "25/03/2024")
    #     self.lp.page_scroll()
    #     search_flight_result.filter_flights_by_stop("2 Stops")
    #     allstops1 = search_flight_result.get_search_flight_results()
    #     print(len(allstops1))
    #     self.ut.assertListItemText(allstops1, "2 Stops")

        # lp = LaunchPage(self.driver)
        # lp.departfrom("New Delhi")
        # lp.enterDepartFromLocation("New Delhi")
        # # Provide going to location
        # lp.enterGoingToLocation("New York")
        # # Select departure date
        # lp.enterDepartureDate("24/03/2024")
        # # Click on flight search button
        # lp.clickSearchFlightButton()
        # To handle dynamic scroll
        # Select filter 1 stop
        # sf = SearchFlightsResults(self.driver)

        # Verify that verified results show flights having only 1 stop
        # allstops1 = self.wait.until(EC.presence_of_all_elements_located((By.XPATH, "//span[contains(text(),'Non Stop') or contains(text(),'1 Stop') or contains(text(),'2 Stop')]")))
        # allstops1 = lp.wait_for_presence_of_all_elements(By.XPATH, "//span[contains(text(),'Non Stop') or contains(text(),'1 Stop') or contains(text(),'2 Stop')]")

        # ut = Utils()
        # for stop in allstops1:
        #     print("The text is: "+ stop.text)
        #     assert stop.text == "1 Stop"
        #     print("assert pass")

# Launching browser and open the travel website
# Provide going from location
# Provide going to location
# To resolve sync issues
# select departure date
# Click on flight search button
# To handle dynamic scroll
# Select filter 1 stop
# Verify that verified results show flights having only 1 stop
