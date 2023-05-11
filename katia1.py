# This is a Katia Ioffe stuff do not tuch!!!


import time
from csv import writer
from selenium import webdriver
from selenium.webdriver.chrome.service import Service


GOOGLE_URL = 'https://www.google.com'
FACH_URL = 'https://www.fachinfo.de/suche/'
XPATH = 'xpath'
FILE_NAME = 'medications.csv'
NEXT_PAGE_XPATH = '(//jhi-pagination//span)[4]'
LAST_PAGE_XPATH = '(//jhi-pagination//span)[5]'
PAGE_NUM_XPATH = '(//jhi-pagination//span)[3]'


def move_page() -> None:
    """This fucntion will move to next page"""
    nxt_btn = driver.find_element(XPATH, NEXT_PAGE_XPATH)
    driver.execute_script("arguments[0].click();", nxt_btn)


def get_titles() -> None:
    """This fucntion will write all titles"""
    with open(FILE_NAME, 'a', encoding='utf8', newline='') as f:
        thewriter = writer(f)
        titles_xpath = "//span//a[text()]"
        titles = driver.find_elements(XPATH, titles_xpath)
        for title in titles:
            t = title.text.strip().lower()
            thewriter.writerow([t])


def get_page_num(later: str) -> int:
    """This fucntion will get later and will get num pages per this later"""
    nxt_btn = driver.find_element(XPATH, LAST_PAGE_XPATH)
    driver.execute_script("arguments[0].click();", nxt_btn)
    time.sleep(2)
    page_num = int(driver.find_element(XPATH, PAGE_NUM_XPATH).text)
    driver.get(f'{FACH_URL}{later}')
    return page_num

if __name__ == "__main__":
    s=Service(r"/Users/medixdigital/Desktop/katia_projects/chromedriver_mac_arm64.exe")
    driver = webdriver.Chrome(service=s)
    driver.get(GOOGLE_URL)
    driver.maximize_window() # For maximizing window
    driver.implicitly_wait(20) # gives an implicit wx`ait for 5 seconds

    # writing title
    with open(FILE_NAME, 'w', encoding='utf8', newline='') as f:
        thewriter = writer(f)
        thewriter.writerow(['medecation'])
    # external loop for a-z 
    # internal loop for 1-n
    # nested tags for element content
    for cha in [chr(i) for i in range(ord('a'), ord('z') + 1)]:
        driver.get(f'{FACH_URL}{cha}')
        num_pages = get_page_num(cha)
        for i in range(num_pages):
            get_titles()
            move_page()
