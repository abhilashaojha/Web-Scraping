# Web Scraping Algorithms

Web scraping is the process of automatically extracting information from websites. 

* It involves using programs or scripts to access and parse the HTML or other markup languages of web pages, retrieving specific data, and then storing or manipulating that data for various purposes. 

* Web scraping can be done using various programming languages and tools, and it is often used to gather data for analysis, research, or automation.

<br>

<img src="imgs/imageScraping.png">

## Image Scraper 

<i> image_scraper.py </i> is a web scraping script using Selenium, a tool for automating web browsers.

* It is an automated process of loading and saving images from the web in local folders of your systems. 

* Selenium is an open-source framework for automating web applications. It provides a suite of tools for controlling web browsers through programs and performing automated testing of web applications.

* For installation and usage of Selenium and Web drivers, visit this html page: https://selenium-python.readthedocs.io/installation.html

### Code Implementation: 

1. Open the Google Images website.
2. Search for a specified query, in this case, "electronic waste."
3. Scroll through the search results dynamically to load more images.
4. Capture and save a specified number of images related to the query ("electronic waste") from the search results.

Here's a breakdown of the main parts of the code:

### Web Driver Setup:

* A  `Chrome WebDriver` instance is created to automate the Google Chrome browser.

### Google Images Search:

* The script navigates to the Google Images website and enters the search query "electronic waste" into the search box.

### Dynamic Scrolling:

* The `scroll_to_load` function is defined to scroll dynamically to the bottom of the search results, loading more images as it goes.

### Image Capture:

* The script captures and saves each image from the search results by finding the image elements using `XPath`.

* The images are saved in a specified folder with filenames indicating the query and a numerical index.

### Example Usage:

* The script is executed with the example usage ` scrape_images("electronic waste", 100)` , which searches for "electronic waste" and captures 100 images.

### Web Driver Closure:

Finally, the web driver instance is closed to release browser resources.

This code essentially `automates the process of searching for images on Google, scrolling through the results, and capturing a specified number of images related to the given query.`


### References: 

https://www.geeksforgeeks.org/download-google-image-using-python-and-selenium/