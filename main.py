from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# Launch the IRCTC website
driver = webdriver.Chrome()
driver.get("https://www.irctc.co.in/nget/train-search")

# Wait for the page to load
time.sleep(5)

# Click on "LOGIN" button
login = driver.find_element_by_xpath("//a[contains(text(),'LOGIN')]")
login.click()

# Wait for the login page to load
time.sleep(5)

# Enter your username and password
username = driver.find_element_by_xpath("//input[@formcontrolname='userId']")
username.send_keys("your_username")
password = driver.find_element_by_xpath("//input[@formcontrolname='pwd']")
password.send_keys("your_password")

# Click on "Sign in"
signin = driver.find_element_by_xpath("//button[contains(text(),'SIGN IN')]")
signin.click()

# Wait for the home page to load
time.sleep(10)

# Enter the source station
source = driver.find_element_by_xpath("//input[@placeholder='From*']")
source.send_keys("Delhi")

# Enter the destination station
destination = driver.find_element_by_xpath("//input[@placeholder='To*']")
destination.send_keys("Mumbai")

# Enter the journey date
date = driver.find_element_by_xpath("//input[@placeholder='Journey Date(dd-mm-yyyy)*']")
date.send_keys("05-04-2023")

# Submit the form
submit = driver.find_element_by_xpath("//button[@type='submit']")
submit.click()

# Wait for the search results page to load
time.sleep(10)

# Extract information about available trains and fares
train_list = driver.find_elements_by_xpath("//div[@class='train_avl_enq_box']")
for train in train_list:
    train_name = train.find_element_by_xpath(".//div[@class='train_info']/a").text
    fare_element = train.find_element_by_xpath(".//div[@class='train_avl_fare']/span[@class='fare']")
    fare = fare_element.text.replace("INR ", "")
    print("Train Name: ", train_name)
    print("Fare: ", fare)

# Choose a train and fare
train = train_list[0]
train.click()
time.sleep(5)
fare_element = driver.find_element_by_xpath("//div[@class='fare_details']/span[@class='fare']")
fare = fare_element.text.replace("INR ", "")
print("Selected Train Fare: ", fare)

# Click on "Book Now"
book_now = driver.find_element_by_xpath("//button[contains(text(),'Book Now')]")
book_now.click()
time.sleep(5)

# Enter passenger details
name = driver.find_element_by_xpath("//input[@placeholder='Enter Passenger Name']")
name.send_keys("John Doe")
age = driver.find_element_by_xpath("//input[@placeholder='Enter Age']")
age.send_keys("30")
gender = driver.find_element_by_xpath("//select[@formcontrolname='passengerGender']/option[text()='Male']")
gender.click()

# Make payment
pay_now = driver.find_element_by_xpath("//button[contains(text(),'Pay Now')]")
pay_now.click()
time.sleep(5)

# Close the browser
driver.quit()
