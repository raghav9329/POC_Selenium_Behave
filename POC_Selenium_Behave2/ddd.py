from behave import *
from selenium import webdriver
import time
@given(u"Open browser visit application")
def step_impl(context):
    context.browser=webdriver.Chrome()
    context.browser.get("https://www.facebook.com")
@when(u"the page is loaded fill the  login id and password")
def step_impl(context):
    login=context.browser.find_element_by_id("email")
    login.send_keys("24jdsdsd")
    password=context.browser.find_element_by_id("pass")
    password.send_keys("123456789")
@then(u"click on login button and verify the page")
def step_impl(context):
    sub=context.browser.find_element_by_xpath("//input[@value='Log In']")
    time.sleep(6)
    sub.click()
    assert context.browser.title!="facebook"
    time.sleep(6)
    context.browser.quit
