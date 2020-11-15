from splinter import Browser
from bs4 import BeautifulSoup as bs
import time

mars_data = {}
def init_browser():
    executable_path = {"executable_path": "/usr/local/bin/chromedriver"}
    browser = Browser("chrome", **executable_path, headless=False)

def scrape ():
    browser = init_browser()
    # 1- news healines and articles
    #===============================
    news_url = "https://mars.nasa.gov/news/"
    browser.visit(news_url)
    news_html = browser.html
    news_soup = bs(news_html, "html.parser")
    news_list = news_soup.find('ul', class_='item_list')
    headline = news_list.find('div', class_="content_title").text
    articles = news_list.find("div", class_="article_teaser_body").text
    # assign & strip titles& paragraghs
    #-----------------------------------
    news_title = headline.strip()
    news_p = articles.strip()    
    #======================================================================
    # 2- Mars Images [ JPL Images]
    #==============================
    featured_image_url = []
    jpl_url = "https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars"
    browser.visit(jpl_url)
    jpl_html = browser.html
    jpl_soup = bs(jpl_html, 'html.parser')
    image_url = jpl_soup.find("ul", class_="articles")
    ###########################
    href = results.find("a",class_='fancybox')['data-fancybox-href']
    featured_image_url.append("https://www.jpl.nasa.gov" + href)
    #======================================================================
    # 3- Mars Facts:
    #================
    facts_url = "https://space-facts.com/mars/"
    facts_df = pd.read_html(facts_url)
    df = pd.DataFrame(facts_df[0])
    df.columns = ["Planet Profile", "Mars"]
    df.set_index("Planet Profile")
    mars_facts = df.to_html(index = True, header =True)
    #======================================================================
    # 4- Mars Hemispheres:
    #======================
    hemisphere_image_urls = {}
    hemispheres_url = "https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"
    browser.visit(hemispheres_url)
    hemispheres_html = browser.html
    hemispheres_soup = bs(hemispheres_html, 'html.parser')
    h3_div = hemispheres_soup.find_all("h3")
    for title in h3_div:
        browser.links.find_by_partial_text("Hemisphere")
        discription_div = hemispheres_soup.find_all("div", class_="description")
        for div in discription_div:
            div_a = div.find('a')
            img_href = div_a['href']
            title_img = div_a.find('h3').text
            image_url = "https://astrogeology.usgs.gov" + img_href
            browser.visit(image_url)
            download_html = browser.html
            download_soup = bs(download_html, 'html.parser')
            full_img = download_soup.find("a", target="_blank")
            full_image = full_img['href']
            hemisphere_image_urls = {
                "title": title, 
                "img_url": full_image
                }
            mars_data = {
                "news_title": news_title,
                "news_p": news_p,
                "mars_facts": mars_facts,
                "jpl_image": featured_image_url,
                "hemisphere_image_urls": hemisphere_image_urls
            }
            ###From Internet to get all images not just one 
            #=================================================
    #======================================================================
    # mars_data dict to collect mars data
    browser.quit()
    return mars_data
    #========================================================================
    #========================================================================