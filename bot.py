from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.get("https://www.newegg.com/evga-geforce-rtx-3060-12g-p5-3657-kr/p/N82E16814487539?Description=rtx%203060&cm_re=rtx_3060-_-14-487-539-_-Product")
assert "Python" in driver.title


#
outOfStockChecker = driver.find_element_by_name_xpath('//*[@id="app"]/div[2]/div[1]/div/div/div[2]/div[1]/div[5]/div[3]/div/strong/text()')
if (outOfStockChecker != " OUT OF STOCK.")  {
    buyButton = driver.find_element_by_class("btn btn-primary btn-wide")
    buyButton.click()


    #Skip the confirmation page
    driver.sendKeys(Keys.SPACE) 

    #This xpath may need to be changed
    addToCartConfirm = driver.find_element_by_xpath('//*[@id="modal-intermediary"]/div/div/div[2]/div[1]/button[2]')
    addToCartConfirm.click()

    #Reusing this button since it is the same button on the checkout page
    buyButton.click()
} else {
    print("It is still out of stock")
}
driver.close()