from selene import browser, be, have

def test_browser_search_google():
    browser.open('https://google.com/')
    browser.element('[name="q"]').should(be.blank).type('qa.guru').press_enter()
    browser.element('html').should(have.text('Курсы тестировщиков'))
def test_browser_search_google_empty():
    browser.open('https://google.com/')
    browser.element('[name="q"]').should(be.blank).type(')(*?:%;№"№;%:?*').press_enter()
    browser.element('html').should(have.text('По запросу «)(*?:%;№"№;%:?*» ничего не найдено.'))
