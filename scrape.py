from bs4 import BeautifulSoup
from selenium import webdriver
import requests

BASE_URL = "https://mars.nasa.gov/news/"



def scrapeArticles():
    driver = webdriver.Firefox()
    driver.get(BASE_URL)
    driver.implicitly_wait(10)
    html = driver.page_source
    driver.close()
    soup = BeautifulSoup(html, "html.parser")

    title_list_div = soup.find_all("div", class_="list_text")
    title_div_tags = [e.find("div", class_="content_title") for e in title_list_div]
    content_div_tags = soup.find_all("div", class_= "article_teaser_body")
    article_title = [title_div.next_element.string for title_div in title_div_tags]
    article_teaser = [content_div.next_element.string for content_div in content_div_tags]
    articles_combined = dict(zip(article_title, article_teaser))
    return(articles_combined)