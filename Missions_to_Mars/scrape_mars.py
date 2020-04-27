#!/usr/bin/env python
# coding: utf-8

# Dependencies
from bs4 import BeautifulSoup as bs
from splinter import Browser
import requests
import pandas as pd

def init_browser(): 
    executable_path = {'executable_path': 'chromedriver.exe'}
    return Browser('chrome', **executable_path, headless=False)

def scrape():
    browser = init_browser()

    mars_data = {}

    # URL of the Page
    url = 'https://mars.nasa.gov/news/'
    browser.visit(url)

    # Parsing HTML
    html= browser.html
    soup = bs(html, 'html.parser')

    news_title = soup.title.text.strip()
    news_p = soup.body.find('p').text

    mars_data["news_title"] = news_title
    mars_data["news_p"] = news_p 

    # # JPL Mars Space Images - Featured Image

    # URL of the page
    url2 = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
    browser.visit(url2)

    # Parsing HTML
    html2 = browser.html
    image_soup = bs(html2, 'html.parser')

    start_url = requests.get('https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars')
    three_soup = bs(html2, 'html.parser')
    image_url = three_soup.find('div', class_='carousel_items').article

    footer = image_url.find('footer')
    ref = footer.find('a')
    path = ref['data-fancybox-href']

    # adding path to image url to print the featured image url
    featured_image_url = f'https://www.jpl.nasa.gov{path}'

    mars_data["featured_image_url"] = featured_image_url 

    # # Mars Weather

    # URL of the page
   
    # # Mars Facts

    # URL of the page
    url4 = 'https://space-facts.com/mars/'
    browser.visit(url4)
    html4 = browser.html

    tables = pd.read_html(url4)

    mars_facts= tables[0]

    mars_facts = tables[1]

    mars_facts.columns = ['MARS DESCRIPTION','Mars Value','Earth']
    mars_facts.set_index('MARS DESCRIPTION', inplace=True)

    html_table = mars_facts.to_html()
    mars_data["mars_facts"] = html_table
    # # Mars Hemispheres

    # URL of Cerebrus Hemisphere
    cerebrus_main_url = 'https://astrogeology.usgs.gov/search/map/Mars/Viking/cerberus_enhanced'
    browser.visit(cerebrus_main_url)

    # Parsing HTML
    htmlcerebrus = browser.html
    cerebrus_soup = bs(htmlcerebrus, 'html.parser')

    cerebrus_url = cerebrus_soup.find('div', class_='downloads')
    cerebrus_link = cerebrus_url.find('a')
    cerebrus_image = cerebrus_link['href']

    mars_data["cerebrus hem"] = cerebrus_image

    # ### Schiaparelli Hemisphere

    # URL of Schiaparelli Hemisphere
    schiaparelli_main_url = 'https://astrogeology.usgs.gov/search/map/Mars/Viking/schiaparelli_enhanced'
    browser.visit(schiaparelli_main_url)

    # Parsing HTML
    htmlschiaparelli = browser.html
    schiaparelli_soup = bs(htmlschiaparelli, 'html.parser')

    # Attaining image url
    schiaparelli_url = schiaparelli_soup.find('div', class_='downloads')
    schiaparelli_link = schiaparelli_url.find('a')
    schiaparelli_image = schiaparelli_link['href']

    # ### Syrtis Major Hemisphere

    # URL of Syrtis Major Hemisphere
    syrtis_main_url = 'https://astrogeology.usgs.gov/search/map/Mars/Viking/syrtis_major_enhanced'
    browser.visit(syrtis_main_url)

    # Parsing HTML
    htmlsyrtis = browser.html
    syrtis_soup = bs(htmlsyrtis, 'html.parser')

    # Attaining image url
    syrtis_url = syrtis_soup.find('div', class_='downloads')
    syrtis_link = syrtis_url.find('a')
    syrtis_image = syrtis_link['href']

    # ### Valles Marineris Hemisphere

    # URL of Valles Marineris Hemisphere
    valles_main_url = 'https://astrogeology.usgs.gov/search/map/Mars/Viking/valles_marineris_enhanced'
    browser.visit(valles_main_url)

    # Parsing HTML
    htmlvalles = browser.html
    valles_soup = bs(htmlvalles, 'html.parser')

    # Attaining image url
    valles_url = valles_soup.find('div', class_='downloads')
    valles_link = valles_url.find('a')
    valles_image = valles_link['href']

    hemispheres_dict = [
    {"title": "Cerberus Hemisphere", "img_url": cerebrus_image},
    {"title": "Schiaparelli Hemisphere", "img_url": schiaparelli_image},
    {"title": "Syrtis Major Hemisphere", "img_url": syrtis_image},
    {"title": "Valles Marineris Hemisphere", "img_url": valles_image}]

    hemispheres_dict

    mars_data["hemispheres_dict"] = hemispheres_dict



    # Store data in a dictionary
    mars_data = {
        "news_title": news_title,
        "news_p": news_p,
        "featured_image_url": featured_image_url,
        "mars_facts": html_table,
        "cerebrus_hem": cerebrus_image,
        "schiaparelli_image": schiaparelli_image,
        "syrtis_image": syrtis_image,
        "valles_image": valles_image
    }
    # Close the browser after scraping
    browser.quit()

    # Return results
    return mars_data

if __name__ == '__main__':
    scrape()


