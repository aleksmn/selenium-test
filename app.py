import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import pandas as pd

url = 'https://www.youtube.com/c/JohnWatsonRooney/videos?view=0&sort=p&flow=grid'


driver = webdriver.Chrome()

driver.get(url)
time.sleep(3)

# driver.execute_script('window.scrollTo(0, 30000)')

element = driver.find_element("tag name", 'body')

for i in range(30):
        element.send_keys(Keys.PAGE_DOWN)
        time.sleep(0.3)  

videos = driver.find_elements("class name",
                              "style-scope ytd-grid-video-renderer")


video_list = []

for v in videos:
    title = v.find_element('xpath', './/*[@id="video-title"]').text
    views = v.find_element('xpath', './/*[@id="metadata-line"]/span[1]').text
    when = v.find_element('xpath', './/*[@id="metadata-line"]/span[2]').text

    print(title, views, when)

    vid_item = {
        'title': title,
        'views': views,
        'posted': when
    }

    video_list.append(vid_item)


df = pd.DataFrame(video_list)

print(df)
