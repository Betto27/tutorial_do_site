from behave import given, when, then
from selenium import webdriver
from nose.tools import assert_equal
from time import sleep

driver = webdriver.Chrome()

@given(u'que acesso o {site}')
def step_impl(context, site):
    driver.maximize_window()
    driver.get(site)


@when(u'preencho o campo de pesquisa com {pesquisa} e clico em pesquisar')
def step_impl(context, pesquisa):

    driver.find_element_by_id('search').send_keys(pesquisa)
    driver.find_element_by_css_selector("#search-icon-legacy").click()
    sleep(3)


@then(u'é exibido o resultado da pesquisa e o titulo da pagina é {res}')
def step_impl(context, res):

    assert_equal(str(driver.title), res)
    sleep(3)
    driver.close()