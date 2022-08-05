import time

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.action_chains import ActionChains


def open_chrome():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://www.carrefour.fr")
    cookie = driver.find_element(By.CSS_SELECTOR, "div.banner-actions-container > button")
    cookie.click()
    barre_recherche = driver.find_element(By.CSS_SELECTOR, "input.pl-input-text__input--text.pl-input-text__input--no-auto-zoom")
    barre_recherche.send_keys("1664")
    barre_recherche = driver.find_element(By.CSS_SELECTOR, "div.pl-input-text-group__append > button")
    barre_recherche = driver.find_element(By.ID, "")
    select_menu = select(driver.find_element(By.CSS_SELECTOR, "div.mainbar__section button"))
    barre_recherche.click()
    time.sleep(2)
    driver.quit()

def css_correction():
    driver = webdriver.Chrome()

    driver.maximize_window()
    driver.get("https://www.carrefour.fr/")

    wait = WebDriverWait(driver, 10)
    close_cookies_button = wait.until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR, "#onetrust-accept-btn-handler")))
    close_cookies_button.click()

    search_bar = driver.find_element(By.CSS_SELECTOR, "input[required]")
    # possibilite utilisation [required]
    search_bar.send_keys("1664")
    search_button = driver.find_element(By.CSS_SELECTOR, "button[type=submit]")
    # possibilite utilisation [type=submit]
    search_button.click()
    first_result = driver.find_element(By.CSS_SELECTOR, ".product-grid-item:nth-child(1) .main-vertical--image")
    first_result.click()

    buy_button = wait.until(
        expected_conditions.element_to_be_clickable((By.CSS_SELECTOR, ".pdp-button-container")))
    # possibilite utilisation [aria-label='ACHETER'] : mais attention au changement de langue
    buy_button.click()

    retrait_en_magasin = wait.until(
        expected_conditions.element_to_be_clickable((By.CSS_SELECTOR, ".push-services--pickers li:nth-child(1) label")))
    delivery24 = driver.find_element(By.CSS_SELECTOR, ".push-services--pickers li:nth-child(2) label")
    delivery1 = driver.find_element(By.CSS_SELECTOR, ".push-services--pickers li:nth-child(3) label")
    assert retrait_en_magasin.text == 'Drive\nRetrait gratuit en magasin'
    assert "Drive" in retrait_en_magasin.text
    assert delivery24.text == 'Livraison\nVotre plein de course en 24h'
    assert delivery1.text == 'Livraison 1h\nVos courses d’appoint en 1h'
    driver.quit()
    #deplacer la souris sur epicerie salee
    epicerie_salee_menu = driver.find_element(By.CSS_SELECTOR, ".nav-item__menu-link [alt='Epicerie salée']")
    action = ActionChains(driver)
    action.move_to_element(buy_button)
    action.perform()

def test_css_correction2():
    driver = webdriver.Chrome()

    driver.maximize_window()
    driver.get("https://www.carrefour.fr/")

    wait = WebDriverWait(driver, 10)
    close_cookies_button = wait.until(
        expected_conditions.element_to_be_clickable((By.CSS_SELECTOR, "#onetrust-accept-btn-handler")))
    close_cookies_button.click()
    action = ActionChains(driver)
    Hub_menu = driver.find_element(By.CSS_SELECTOR, "div.mainbar__section button")
    Hub_menu.click()
    epicerie_salee_menu = wait.until(
        expected_conditions.element_to_be_clickable((By.CSS_SELECTOR, ".nav-item__menu-link [alt='Epicerie salée']")))
    action = ActionChains(driver)
    action.move_to_element(epicerie_salee_menu)
    action.perform()


