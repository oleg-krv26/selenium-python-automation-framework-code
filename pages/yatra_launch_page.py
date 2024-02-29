import logging
import time
from selenium import webdriver
from selenium.common import StaleElementReferenceException
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from base.base_driver import BaseDriver
from pages.search_flight_result_page import SearchFlightsResults
from utilities.utils import Utils


class LaunchPage(BaseDriver):
    log = Utils.cust_logger()
    def __init__(self,driver):
        super().__init__(driver)
        self.driver = driver
        # self.wait = wait
        # Provide going from location
    # Locators
    DEPART_FROM_FIELD = "//input[@id='BE_flight_origin_city']"
    GOING_TO_FIELD = "//input[@id='BE_flight_arrival_city']"
    GOING_TO_RESULTS_lIST = "//div[@class='viewport']//div[1]/li"
    SELECT_DATE_FIELD = "//input[@id='BE_flight_origin_date']"
    ALL_DATES = "//div[@id='monthWrapper']//tbody//td[@class!='inActiveTD']"
    SEARCH_BUTTON = "//input[@value='Search Flights']"

    def getDepartFromField(self):
        return self.wait_until_element_is_clickable(By.XPATH, self.DEPART_FROM_FIELD)

    def getGoingToField(self):
        return self.wait_until_element_is_clickable(By.XPATH, self.GOING_TO_FIELD)

    def getGoingToResults(self):
        return self.wait_for_presence_of_all_elements(By.XPATH, self.GOING_TO_RESULTS_lIST)

    def getDepartureDateField(self):
        return self.wait_until_element_is_clickable(By.XPATH, self.SELECT_DATE_FIELD)

    def getAllDatesField(self):
        return self.wait_until_element_is_clickable(By.XPATH, self.ALL_DATES)

    def getSearchButton(self):
        return self.driver.find_element(By.XPATH, self.SEARCH_BUTTON)

    def enterDepartFromLocation(self, departlocation):
        self.getDepartFromField().click()
        self.getDepartFromField().send_keys(departlocation)
        self.getDepartFromField().send_keys(Keys.ENTER)

    # def departfrom(self,departlocation):
    #     depart_from = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@id='BE_flight_origin_city']")))
    #     depart_from = self.wait_until_element_is_clickable(By.XPATH, "//input[@id='BE_flight_origin_city']")
    #     depart_from.click()
    #     depart_from.send_keys(departlocation)
    #     depart_from.send_keys(Keys.ENTER)

        # Provide going to location
    def enterGoingToLocation(self, goingtolocation):
        self.getGoingToField().click()
        self.log.info("Clicked on going to")
        time.sleep(2)
        self.getGoingToField().clear()
        time.sleep(1)
        self.getGoingToField().send_keys(goingtolocation)
        self.log.info("Typed text into going to field successfully")
        time.sleep(2)
        search_results = self.getGoingToResults()
        for results in search_results:
            if goingtolocation in results.text:
                results.click()
                break

    # def goingto(self,goingtolocation):
    #     # going_to = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@id='BE_flight_arrival_city']")))
    #     going_to = self.wait_until_element_is_clickable(By.XPATH, "//input[@id='BE_flight_arrival_city']")
    #     # time.sleep(2)
    #     going_to.click()
    #     time.sleep(2)
    #     going_to.clear()
    #     # time.sleep(2)
    #     going_to.send_keys(goingtolocation)
    #     time.sleep(3)
    #     going_to.send_keys(Keys.ENTER)
    #     time.sleep(2)

    #     # search_results = self.wait_for_presence_of_all_elements(By.XPATH, "//div[@class='viewport']//div[1]/li")
        # for results in search_results:
        #     try:
        #         if "New York (JFK)" in results.text:
        #             results.click()
        #         break
        #     except StaleElementReferenceException:
        #      # If the element becomes stale, re-locate it and try again
        #      search_results = self.wait_for_presence_of_all_elements(By.XPATH, "//div[@class='viewport']//div[1]/li")
        #      for new_result in search_results:
        #         if "New York (JFK)" in new_result.text:
        #             new_result.click()
        #             break

        # search_results = self.wait.until(EC.presence_of_all_elements_located((By.XPATH, "//div[@class='viewport']//div[1]/li")))
        # search_results = self.wait_for_presence_of_all_elements(By.XPATH, "//div[@class='viewport']//div[1]/li")
        # for results in search_results:
        #     if "New York (JFK)" in results.text:
        #         results.click()
        #         break

    def enterDepartureDate(self, departuredate):
        self.getDepartureDateField().click()
        all_dates = self.getAllDatesField().find_elements(By.XPATH, self.ALL_DATES)
        for date in all_dates:
            if date.get_attribute("data-date") == departuredate:
                date.click()
                break

    def clickSearchFlightButton(self):
        self.getSearchButton().click()
        time.sleep(4)

    # def selectdate(self, departuredate):
    #     # Insert the wait for invisibility of element here
    #     # self.wait.until(EC.invisibility_of_element_located((By.CLASS_NAME, "ac_airportname")))
    #     self.wait_until_invisibility_of_element_located(By.CLASS_NAME, "ac_airportname")
    #     # self.wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@id='BE_flight_origin_date']")))
    #     self.wait_until_element_is_clickable(By.XPATH, "//input[@id='BE_flight_origin_date']").click()
    #     # Now, click the element
    #     # self.driver.find_element(By.ID, "BE_flight_origin_date").click()
    #
    #     # select departure date
    #     # all_dates = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@id='monthWrapper']//tbody//td[@class!='inActiveTD']")))\
    #     #     .find_elements(By.XPATH, "//div[@id='monthWrapper']//tbody//td[@class!='inActiveTD']")
    #     all_dates = self.wait_until_element_is_clickable(By.XPATH, "//div[@id='monthWrapper']//tbody//td[@class!='inActiveTD']")\
    #         .find_elements(By.XPATH, "//div[@id='monthWrapper']//tbody//td[@class!='inActiveTD']")
    #     for date in all_dates:
    #         if date.get_attribute("data-date") == departuredate:
    #             date.click()
    #             break
    #     # Click on flight search button
    # def clicksearch(self):
    #     self.driver.find_element(By.XPATH, "//input[@value='Search Flights']").click()
    #     time.sleep(4)

    def searchFlights(self, departlocation, goingtolocation, departuredate):
        self.enterDepartFromLocation(departlocation)
        self.enterGoingToLocation(goingtolocation)
        self.enterDepartureDate(departuredate)
        self.clickSearchFlightButton()
        search_flights_result = SearchFlightsResults(self.driver)
        return search_flights_result
