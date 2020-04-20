from selenium import webdriver

driver = webdriver.Chrome('D:/Downloads/chromedriver.exe')
driver.get('https://web.whatsapp.com/')

name = input('User or group to send message to: ')
msg = input('Enter your message: ')
count = int(input('Times to send the message: '))

input('Enter anything after scanning QR code')

user = driver.find_element_by_xpath('//span[@title = "{}"]'.format(name))
user.click()

msg_box = driver.find_elements_by_class_name('input-container')

for i in range(count):
	msg_box.send_keys(msg)
	button = driver.find_elements_by_class_name('compose-btn-send')
	button.click()