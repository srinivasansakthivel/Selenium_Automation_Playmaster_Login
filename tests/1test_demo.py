import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--disable-notifications")
driver = webdriver.Chrome(executable_path="C:\\Softwares\\ChromeDriver\\chromedriver.exe", options=chrome_options)
driver.maximize_window()
driver.get("https://protonmail.com/")
# driver.execute_script("document.body.style.zoom='80%'")
print(driver.current_url)
print(driver.title)
# clicking the login in button in protonmail home page
driver.find_element(By.XPATH, "//a[contains(text(),'LOG IN')]").click()
wait = WebDriverWait(driver, 20)
wait.until(expected_conditions.presence_of_element_located((By.XPATH, "//button[@id='login_btn']")))
driver.find_element(By.XPATH, "//input[@id='username']").send_keys("logitest11@protonmail.com")
driver.find_element(By.XPATH, "//input[@id='password']").send_keys("$LogiTest$")
# clicking the login in button
driver.find_element(By.XPATH, "//button[@id='login_btn']").click()
wait.until(expected_conditions.presence_of_element_located((By.XPATH, "//header/div[1]/a[1]")))
time.sleep(3)
# logged into protonmail successfully
driver.find_element(By.XPATH, "//span[contains(text(),'Your Twitch Login Verification Code')]").click()
time.sleep(5)
# last_verification_code = driver.find_element_by_xpath("//p[contains(text(),'740753')]")
# driver.execute_script("arguments[0].scrollIntoView();", last_verification_code)
# driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
# taking the email count to get the correct otp message
email_count = driver.find_element(By.XPATH,
                                  "//body/div[@id='body']/div[@id='pm_main']/div[@id='wrapper']/div[@id='conversation-list-columns']/section[1]/div[1]/div[2]/div[1]/h4[1]/span[2]").text
email_count_str = str(email_count)
print(str(email_count))
print(email_count_str[1:-1])
exact_email_count_1 = email_count_str[1:-1]
exact_email_count_2 = int(exact_email_count_1) - 1
exact_email_count_3 = str(exact_email_count_2)
print(exact_email_count_3)
time.sleep(5)
message_locator = driver.find_element(By.XPATH, "//body/div[@id='body']/div[@id='pm_main']/div[@id='wrapper']/div["
                              "@id='conversation-view']/element-view[1]/div[1]/section[1]/div[1]/article[%s]/div["
                              "2]/div[3]" % str(exact_email_count_1))
message_locator.click()
driver.execute_script("arguments[0].scrollIntoView();", message_locator)
time.sleep(2)
last_email_code_text = driver.find_element_by_xpath("/html[1]/body[1]/div[2]/div[2]/div[1]/div[2]/element-view[1]/div[1]/section[1]/div[1]/article[%s]/div[2]/div[3]/div[1]/table[1]/tbody[1]/tr[1]/td[1]/center[1]/table[2]/tbody[1]/tr[1]/td[1]/table[5]/tbody[1]/tr[1]/th[1]/table[1]/tbody[1]/tr[1]/th[1]/div[1]/p[1]" % str(exact_email_count_1)).text
# last_email_code_text = driver.find_element(By.XPATH, "/html[1]/body[1]/div[2]/div[2]/div[1]/div[2]/element-view[1]/div[1]/section[1]/div[1]/article[%s]/div[2]/div[3]/div[1]/table[1]/tbody[1]/tr[1]/td[1]/center[1]/table[2]/tbody[1]/tr[1]/td[1]/table[5]/tbody[1]/tr[1]/th[1]/table[1]/tbody[1]/tr[1]/th[1]/div[1]/p[1]" % str(exact_email_count_1))).
print(last_email_code_text)



