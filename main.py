from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import time
import requests

# false to watch it work
HEADLESS = True

options = Options()
options.headless = HEADLESS
options.add_argument("--window-size=1920,1200")

driver = webdriver.Chrome(options=options)
driver.get("https://www.gutenberg.org/")
search_box = driver.find_element_by_class_name("searchInput")
search_box.send_keys("Heart of Darkness")
search_box.send_keys(Keys.RETURN)

book_results = driver.find_elements_by_class_name("booklink")
print(f"Found {len(book_results)} results for 'Heart of Darkness':" )
result_array = []
for result in book_results:
	book_element = result.find_element_by_class_name("content")
	book_title = book_element.find_element_by_class_name("title").text
	book_author = book_element.find_element_by_class_name("subtitle").text
	book_downloads = book_element.find_element_by_class_name("extra").text
	print(f"{book_title}, {book_author}, downloads: {book_downloads}")
	result_array.append({"link element": result, "title": book_title, "downloads": book_downloads})

result_array_filtered = list(filter(lambda book: (book["title"] == "Heart of Darkness"), result_array))
download_candidate = result_array_filtered[0]["link element"]
download_candidate.find_element_by_class_name("link").click()
driver.implicitly_wait(3)
download_links = driver.find_elements_by_xpath("//td[@class='unpadded icon_save']//a")
epub_download_link = list(filter(lambda download_link: download_link.text == "EPUB (no images)", download_links))[0]
epub_download_url = epub_download_link.get_attribute('href')
print(f"Found epub url: {epub_download_url}")

r = requests.get(epub_download_url, allow_redirects=True)
print("Downloading...")
open("Heart of Darkness.epub", 'wb').write(r.content)
print("Done")
driver.quit()