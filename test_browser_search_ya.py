from selene import browser, be, have

def test_browser_search_ya():
    browser.open('https://ya.ru/')
    browser.element('[name="q"]').should(be.blank).type('qa.guru').press_enter()
    browser.element('html').should(have.text('Курсы тестировщиков'))
def test_browser_search_ya_empty():
    browser.open('https://ya.ru/')
    browser.element('[name="q"]').should(be.blank).type('XCVBNM,KLOIUYTFR').press_enter()
    browser.element('html').should(have.text('Ничего не нашли'))
