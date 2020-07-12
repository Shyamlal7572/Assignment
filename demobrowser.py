from selenium import webdriver

driver=webdriver.Chrome(executable_path="C:\\chromedriver.exe")

driver.get("https://www.amazon.com")
driver.maximize_window()

print(driver.title)
print(driver.current_url)

driver.get("https://www.primevideo.com/detail/0OSEWAWFH8U83BJON2GV8UJQPP/ref=atv_hm_hom_c_8pZiqd_2_2")
driver.minimize_window()
driver.back()
driver.refresh()
driver.close()