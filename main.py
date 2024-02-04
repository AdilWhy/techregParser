from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from models import Serts
import orm
from RemoteDriver import remoteDriver
from bs4 import BeautifulSoup

driver = remoteDriver
session = orm.Session()


def insert_to_db(*args):
    (id,
     iin,
     reg_number,
     registrated_at,
     certificated_at,
     end_at,
     status,
     name_organization,
     name_arrc,
     type_management) = args
    new_Sert = Serts(id,
                     iin,
                     reg_number,
                     registrated_at,
                     certificated_at,
                     end_at, status,
                     name_organization,
                     name_arrc,
                     type_management)
    try:
        differences = get_differences(orm.select_value(session, id), new_Sert)
        orm.update_value(session=session, target_id=id, differences=differences)
    except Exception as e:
        orm.insert_value(session=session, serts=new_Sert)
        print("New serts has been inserted")


def get_differences(existing_sert, new_sert):
    differences = {}
    for key in existing_sert.__dict__:
        existing_value = getattr(existing_sert, key)
        new_value = getattr(new_sert, key)
        if existing_value != new_value:
            differences[key] = new_value
    return differences

def getBIN(href):
    main_window = driver.current_window_handle

    url = f"https://techreg.kezekte.kz{href}"

    driver.switch_to.new_window('tab')
    driver.get(url)

    s = BeautifulSoup(driver.page_source, features="html.parser")

    BIN = s.findAll("i", {"class": "text-font-12"})[1].get_text(strip=True).split(',')[0].strip()

    driver.close()

    driver.switch_to.window(main_window)
    return BIN


def main():
    url = "https://techreg.kezekte.kz/ru/cert/certification/managment-cert"
    driver.get(url)
    try:
        while True:
            soup = BeautifulSoup(driver.page_source, features='html.parser')

            trs = soup.find('table', {'class': 'sw-table-content'}).find_all('tr')

            for tr in trs:
                serts_list = []
                tds = tr.find_all('td')
                for td in tds:
                    if td.text == 'Открыть':
                        serts_list.append(getBIN(tr.find('a').get('href')))
                        continue
                    serts_list.append(td.text.strip())

                insert_to_db(serts_list)

            btn = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, "//a[@class='page-link'][@aria-label='Следующая страница']")))
            btn.click()
    except Exception as e:
        print("Entire table has been parsed", e)
        driver.quit()


if __name__ == '__main__':
    main()
