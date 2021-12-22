#!/usr/bin/env python
# coding: utf-8

import pandas as pd
from bs4 import BeautifulSoup as soup 
from splinter import Browser
from webdriver_manager.chrome import ChromeDriverManager

def scrape():
    return_dict  = {}

    # Set up Splinter
    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=False)
    url = 'https://redplanetscience.com/'
    browser.visit(url)

    html = browser.html
    red_planet_soup =soup(html,"html.parser") 

    newselement = red_planet_soup.select_one("div.list_text")

    newstitle  = newselement.find("div", class_= "content_title").get_text()
    return_dict["key_newstitle"] = newstitle

    newspara = newselement.find("div", class_= "article_teaser_body").get_text()
    return_dict["key_newspara"] = newspara

    newsdate = newselement.find("div", class_= "list_date").get_text()
    return_dict["key_newsdate"] = newsdate

    url = 'https://spaceimages-mars.com/'
    browser.visit(url)

    html = browser.html
    space_image_soup =soup(html,"html.parser") 

    image_element = space_image_soup.select_one("img.headerimage.fade-in")
   
    featured_image_url = url + image_element["src"]
    return_dict["key_featured_image_url"] = featured_image_url
    
    url = 'https://galaxyfacts-mars.com/'
    tables = pd.read_html(url)

    df_Mars_facts = tables[0]
    df_Mars_facts.columns =df_Mars_facts.iloc[0]
    df_Mars_facts = df_Mars_facts.drop([0])
    
    html_Mars_facts = df_Mars_facts.to_html(classes="table")
    return_dict["key_html_Mars_facts"] = html_Mars_facts

    url = 'https://marshemispheres.com/'
    browser.visit(url)

    links = browser.find_by_css("a.product-item img")
    number_of_links = range(len(links))
    mars_hemispheres = []


    for index in number_of_links:
        hemispheres = {}
        browser.find_by_css("a.product-item img")[index].click()
        title_text = browser.find_by_css("h2.title").text
        mars_image = browser.links.find_by_text("Sample").first["href"]
        hemispheres["key_title"] = title_text
        hemispheres["key_url"] = mars_image
        mars_hemispheres.append(hemispheres)
        browser.back()

    return_dict["mars_hemispheres"]  = mars_hemispheres              
    browser.quit()

    return (return_dict)


