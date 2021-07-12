from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time


s = Service("D:\SETUPS\chromedriver.exe")

driver = webdriver.Chrome(service=s)

#print(type(driver))

driver.maximize_window()
driver.get("https://www.thesparksfoundationsingapore.org/")

sitetitle = driver.title

#print(sitetitle)

#assert "The Sparks Foundation | Home" in sitetitle
#print("successful")


# Test Case 1: Title Testing

print("\nTest Case 1:Title Testing:")

if sitetitle:
    print("Title is present:",sitetitle)
else:
    print("Title not found")

if sitetitle=="The Sparks Foundation | Home":
    print("Present title verified sucessfully:",sitetitle)
else:
    print("Verification failed")


# Test Case 2: Logo Testing

print("\nTest Case 2: Logo Testing:")
try:
    driver.find_element(By.XPATH,'//*[@id="home"]/div/div[1]/h1/a/img')
    print("Logo is verified \n")
except NoSuchElementException:
    print("Logo is not available")


# Test case 3: Navbar Testing
print("\nTest case 3: Navbar Testing:")

try:
    driver.find_element(By.CLASS_NAME,"navbar")
    print("Navigation Bar is available")
except NoSuchElementException:
    print("Navigation Bar is not available")

# Test case 4: Back to Home Link testing

print("\nTest case 4: Back to Home Link testing:")

try:
    driver.find_element(By.PARTIAL_LINK_TEXT,"The Sparks Foundation")
    print("Sucessfully Visit back to Home Page")
except NoSuchElementException:
    print("Can't open Home Page")


# Test case 5: About Us page Testing

print("\nTest case 5: About Us page Testing:")

try:
    driver.find_element(By.LINK_TEXT,'About Us').click()
    time.sleep(1)
    driver.find_element(By.LINK_TEXT,'Vision, Mission and Values').click()
    time.sleep(1)
    driver.find_element(By.LINK_TEXT, 'Guiding Principles').click()
    time.sleep(1)
    driver.find_element(By.LINK_TEXT, 'Advisors and Patrons').click()
    time.sleep(1)
    driver.find_element(By.LINK_TEXT, "Executive Team").click()
    time.sleep(1)
    driver.find_element(By.LINK_TEXT, "Corporate Partners").click()
    time.sleep(1)
    driver.find_element(By.LINK_TEXT, "Expert Mentors").click()
    time.sleep(1)
    print("Expert Mentors Page is Not Yet Ready!")
    driver.find_element(By.LINK_TEXT, 'About Us').click()
    time.sleep(1)
    driver.find_element(By.LINK_TEXT, "News").click()
    time.sleep(1)
    print("All about us pages are available and verified successfully")
except NoSuchElementException:
    print("Can't open the pages")


# Test case 6: Policies and Code page Testing

print("\nTest case 6: Policies and Code page Testing:")

try:
    driver.find_element(By.LINK_TEXT,'Policies and Code').click()
    time.sleep(1)
    driver.find_element(By.LINK_TEXT,'Policies').click()
    time.sleep(1)
    driver.find_element(By.LINK_TEXT, 'Code of Ethics and Conduct').click()
    time.sleep(1)
    driver.find_element(By.LINK_TEXT, 'Personal Data Policy').click()
    time.sleep(1)
    driver.find_element(By.LINK_TEXT, 'Whistle Blowing Policy').click()
    time.sleep(1)
    driver.find_element(By.LINK_TEXT, 'Service Quality Values').click()
    time.sleep(1)
    print("All Policies and Code pages are available and verified successfully")
except NoSuchElementException:
    print("Can't open the pages")


# Test case 7: Programs pages Testing

print("\nTest case 7: Programs pages Testing:")

try:
    driver.find_element(By.LINK_TEXT,'Programs').click()
    time.sleep(1)
    driver.find_element(By.LINK_TEXT,'Student Scholarship Program').click()
    time.sleep(1)
    driver.find_element(By.LINK_TEXT, 'Student Mentorship Program').click()
    time.sleep(1)
    driver.find_element(By.LINK_TEXT, 'Student SOS Program').click()
    time.sleep(1)
    driver.find_element(By.LINK_TEXT, 'Workshops').click()
    time.sleep(1)
    driver.find_element(By.LINK_TEXT, 'Corporate Programs').click()
    time.sleep(1)
    print("All Programs pages are available and verified successfully")
except NoSuchElementException:
    print("Can't open the pages")



# Test case 8: Links page Testing

print("\nTest case 8: Links page Testing:")

try:
    driver.find_element(By.LINK_TEXT,'LINKS').click()
    time.sleep(1)
    driver.find_element(By.LINK_TEXT,'Software & App').click()
    time.sleep(1)
    driver.find_element(By.LINK_TEXT, 'Salient Features').click()
    time.sleep(1)
    driver.find_element(By.LINK_TEXT, 'AI in Education').click()
    time.sleep(1)
    print("All Links pages are available and verified successfully")
except NoSuchElementException:
    print("Can't open the pages")



# Test case 9: Join Us page Testing

print("\nTest case 9: Join Us page Testing:")

try:
    driver.find_element(By.LINK_TEXT,'Join Us').click()
    time.sleep(1)
    driver.find_element(By.LINK_TEXT,'Why Join Us').click()
    time.sleep(1)
    driver.find_element(By.LINK_TEXT, 'Expert Mentor').click()
    time.sleep(1)
    driver.find_element(By.LINK_TEXT, 'Events Volunteer').click()
    time.sleep(1)
    driver.find_element(By.LINK_TEXT, 'Management Volunteer').click()
    time.sleep(1)
    driver.find_element(By.LINK_TEXT, 'Internship Positions').click()
    time.sleep(1)
    driver.find_element(By.LINK_TEXT, 'Brand Ambassador').click()
    time.sleep(1)
    print("All Join Us pages are available and verified successfully")
except NoSuchElementException:
    print("Can't open the pages")


# Test Case 10: Contact Us page Testing

print("\nTest Case 10: Contact Us page Testing")

try:
    driver.find_element(By.LINK_TEXT,"Contact Us")
    time.sleep(1)
    print("Contact Us page is available")
except NoSuchElementException:
    print("Can't open the page")


# Test case 11: Contact Text Testing

print("\nTest case 11: Contact Text Testing")
try:
    driver.find_element(By.LINK_TEXT,"Contact Us").click()
    time.sleep(1)
    info1 = driver.find_element(By.XPATH,'/html/body/div[2]/div/div/div[3]/div[2]/p[1]')
    info2 = driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div[3]/div[2]/p[2]')
    time.sleep(1)

    print("Info1:",info1.text)
    print("Info2:",info2.text)

    if info1.text == "(for Non-Internship/GRIP Queries Only)" and info2.text == "+65-8402-8590, info@thesparksfoundation.sg":
        print('Info1 and Info2 are corrects!')
    else:
        print("Contact information is Incorrect!")
    print("Contact Page Verification Successful!\n")
except NoSuchElementException:
    print("Contact Page Verification Unsuccessful!")


# Test case 12: Address Text Testing

print("\nTest case 12: Address Text Testing")
try:
    driver.find_element(By.LINK_TEXT,"Contact Us").click()
    time.sleep(1)
    info = driver.find_element(By.XPATH,'/html/body/div[2]/div/div/div[2]/div[2]/p')
    time.sleep(1)

    print("Info:",info.text)
    if info.text != info.text:
        print("Info is Incorrect")
    print("Contact Page Verification Successful!\n")
except NoSuchElementException:
    print("Contact Page Verification Unsuccessful!")


# TestCase 13: Check the Form
print("\nTestCase 13:")
try:
    driver.find_element(By.LINK_TEXT,'Join Us').click()
    time.sleep(1)
    driver.find_element(By.LINK_TEXT,'Why Join Us').click()
    time.sleep(1)
    driver.find_element(By.NAME,'Name').send_keys('Shweta Thikekar')
    time.sleep(1)
    driver.find_element(By.NAME,'Email').send_keys('shwetathikekar17@gmail.com')
    time.sleep(1)
    select = Select(driver.find_element(By.CLASS_NAME,'form-control'))
    time.sleep(1)
    select.select_by_visible_text('Intern')
    time.sleep(1)
    driver.find_element(By.CLASS_NAME,'button-w3layouts').click()
    time.sleep(1)
    print("Form Verification Successful!\n")
except NoSuchElementException:
    print("Form Verification Failed!\n")
    time.sleep(1)




driver.quit()