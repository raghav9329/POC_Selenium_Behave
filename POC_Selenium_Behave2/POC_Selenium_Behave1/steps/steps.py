from behave import *
from selenium import webdriver
import time
@given(u"Open browser visit application")
def step_impl(context):
    context.browser=webdriver.Chrome()
    context.browser.get("https://www.facebook.com")
    time.sleep(6)
@when(u"the page is loaded check that it is loaded with secure certificates or not")
def step_impl(context):
    if(context.browser.title=="untrusted Connection"):
        print("This certificate is incorrect")
