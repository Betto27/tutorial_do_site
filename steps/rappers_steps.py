from behave import when, then
from selenium import webdriver
from time import sleep

driver = webdriver.Chrome()
driver.maximize_window()


@when(u'preencho o campo de pesquisa')
def step_impl(context):
    for row in context.table:
        driver.find_element_by_id('search').send_keys(['rappers'])


@then(u'o video é selecionado')
def step_impl(context):
    pass
    sleep(3)
    driver.close()
