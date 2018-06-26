from selenium import webdriver
import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
import os
import sys

def main():
    driver = ""
    if os.name == "nt":
        driver = webdriver.Chrome("./vendor/chromedriver.exe") 
    else:
        driver = webdriver.Chrome("./vendor/chromedriver") 

    TARGET_URL = "https://docs.google.com/forms/d/e/1FAIpQLSemP__cLWzYqZ-JSlSMGwekHtkuiPRv7dDET8p3pQqbpXHirw/viewform"

    driver.get(TARGET_URL)

    time.sleep(0.5)
    ## input id
    driver.find_element_by_css_selector('#mG61Hd > div > div.freebirdFormviewerViewFormContent > div.freebirdFormviewerViewItemList > div:nth-child(1) > div:nth-child(2) > div > content > div > label:nth-child(2) > div.freebirdMaterialScalecontentInput > div > div.quantumWizTogglePaperradioRadioContainer > div').click()

    ## input pass
    driver.find_element_by_css_selector('#mG61Hd > div > div.freebirdFormviewerViewFormContent > div.freebirdFormviewerViewItemList > div.freebirdFormviewerViewItemsItemItem.freebirdFormviewerViewItemsTextTextItem > div.freebirdFormviewerViewItemsTextItemWrapper > div > div.quantumWizTextinputPaperinputMainContent.exportContent > div > div.quantumWizTextinputPaperinputInputArea > input').send_keys("this is test")
    driver.find_element_by_css_selector('#mG61Hd > div > div.freebirdFormviewerViewFormContent > div.freebirdFormviewerViewItemList > div:nth-child(3) > div.freebirdFormviewerViewItemsGridContainer > div > div.freebirdFormviewerViewItemsGridScrollContainer > div > div:nth-child(2) > label:nth-child(2) > div > div > div.quantumWizTogglePapercheckboxInnerBox.exportInnerBox').click()
    driver.find_element_by_css_selector('#mG61Hd > div > div.freebirdFormviewerViewFormContent > div.freebirdFormviewerViewItemList > div:nth-child(3) > div.freebirdFormviewerViewItemsGridContainer > div > div.freebirdFormviewerViewItemsGridScrollContainer > div > div:nth-child(2) > label:nth-child(4) > div > div > div.quantumWizTogglePapercheckboxInnerBox.exportInnerBox').click()

    driver.find_element_by_css_selector('#mG61Hd > div > div.freebirdFormviewerViewFormContent > div.freebirdFormviewerViewItemList > div:nth-child(3) > div.freebirdFormviewerViewItemsGridContainer > div > div.freebirdFormviewerViewItemsGridScrollContainer > div > div:nth-child(4) > label:nth-child(4) > div > div > div.quantumWizTogglePapercheckboxInnerBox.exportInnerBox').click()

    driver.find_element_by_css_selector('#mG61Hd > div > div.freebirdFormviewerViewFormContent > div.freebirdFormviewerViewItemList > div:nth-child(4) > div.quantumWizMenuPaperselectEl.docssharedWizSelectPaperselectRoot.freebirdFormviewerViewItemsSelectSelect.freebirdThemedSelectDarkerDisabled > div:nth-child(1) > div.quantumWizMenuPaperselectOptionList > div.quantumWizMenuPaperselectOption.freebirdThemedSelectOptionDarkerDisabled.exportOption.isSelected.isPlaceholder').click()
    time.sleep(0.5) 
    driver.find_element_by_css_selector('#mG61Hd > div > div.freebirdFormviewerViewFormContent > div.freebirdFormviewerViewItemList > div:nth-child(4) > div.quantumWizMenuPaperselectEl.docssharedWizSelectPaperselectRoot.freebirdFormviewerViewItemsSelectSelect.freebirdThemedSelectDarkerDisabled.isOpen > div.exportSelectPopup.quantumWizMenuPaperselectPopup > div:nth-child(3)').click()
    time.sleep(0.5) 
    driver.find_element_by_css_selector('#mG61Hd > div > div.freebirdFormviewerViewFormContent > div.freebirdFormviewerViewNavigationNavControls > div.freebirdFormviewerViewNavigationButtonsAndProgress > div > div > content > span').click()



    time.sleep(2)
    driver.quit()


if __name__ == '__main__':

    main()