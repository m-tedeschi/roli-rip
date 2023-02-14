from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

driver = webdriver.Chrome()

def delay():
    time.sleep(1)
    return

def scrape_owners_page(fname):
    odds = driver.find_elements(By.CLASS_NAME ,"odd")
    evens = driver.find_elements(By.CLASS_NAME, "even")
    print("Odds and evens found!")
    print("Odds: ", len(odds))
    print("Evens: ", len(evens))
    f = open(fname, "a")
    element_num_odd = 0
    element_num_even = 0
    for i in range(len(odds)+len(evens)):
        print(i)
        if i % 2 == 0:
            print("writing odds")
            f.write(odds[element_num_odd].text.split(" ")[0]+"\n")
            element_num_odd = element_num_odd + 1
        else:
            print("writing evens")
            f.write(evens[element_num_even].text.split(" ")[0]+"\n")
            element_num_even = element_num_even + 1
    f.close()

def scrape(item_id, fname):
    driver.get("https://www.rolimons.com/item/"+item_id)
    delay()
    resultsPerPage = Select(driver.find_element(By.NAME, "bc_owners_table_length"))
    delay()
    resultsPerPage.select_by_value("100")
    data_info = driver.find_element(By.CLASS_NAME, "dataTables_info")
    data_info_tab = data_info.text.split(" ")
    currentPage = data_info_tab[3]
    finalPage = data_info_tab[5]
    scrape_owners_page(fname)
    while currentPage != finalPage:
        button = driver.find_element(By.ID, "bc_owners_table_next")
        button.click()
        delay()
        scrape_owners_page(fname)
        data_info = driver.find_element(By.CLASS_NAME, "dataTables_info")
        data_info_tab = data_info.text.split(" ")
        currentPage = data_info_tab[3]
        finalPage = data_info_tab[5]
    return

def main():
    fname = input("Enter output file name (with extension): ")
    item_id = input("Enter item ID to scrape: ")
    scrape(item_id, fname)
    input("Script complete! Press [ENTER] to exit.")
    return

main()
