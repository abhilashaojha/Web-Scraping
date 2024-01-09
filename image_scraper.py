# importing necessary libraries

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time


#creating a function 'scrape_images' with two arguements
# query - image one needs to load
# num_images - number of images reuired

def scrape_images(query:str,num_images:int):	

	# Creating a webdriver instance
	driver = webdriver.Chrome()

	# Maximize the screen
	driver.maximize_window()

	# Open Google Images in the browser
	driver.get('https://images.google.com/')

	# Finding the search box with the help of 'Tag_name'. In our case it is 'textarea'
	box = driver.find_element(By.TAG_NAME,"textarea")

	# Type the search query in the search box
	box.send_keys(query)

	# Pressing enter
	box.send_keys(Keys.ENTER)

	# Function for scrolling to the bottom of Google
	# Images results
	def scroll_to_load():
          
		last_height = driver.execute_script('\
				return document.body.scrollHeight')

		while True:
			
			driver.execute_script('window.scrollTo(0, document.body.scrollHeight)')
			
			time.sleep(5)

			new_height = driver.execute_script('\
				return document.body.scrollHeight')
			
			try:
				driver.find_element(By.CLASS_NAME,"LZ4I").click()
 
            # waiting for the results to load
            # Increase the sleep time if your internet is slow
				
				time.sleep(3)
			
			except Exception as e:
				pass

            # Break the loop if no new images are loaded
			
			if new_height == last_height:
				break
			
			last_height = new_height

    # Scroll to load more images by calling the function
	scroll_to_load()

	allimgs = driver.find_elements(By.XPATH,"//img[@class='rg_i Q4LuWd']")

	# Loop to capture and save each image
	for i in range(1, num_images + 1):

		allimgs[i].screenshot(f'imgs/sample_image/{query} ({i}).png')

		# Just to avoid unwanted errors
		time.sleep(0.3)
		
	#finally, close the instance of the web driver.
	driver.quit()

# Example usage:
scrape_images("electronic waste", 100)