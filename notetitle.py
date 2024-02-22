import pandas as pd
import requests
from bs4 import BeautifulSoup as bs


def title():
    # Define the base URL
    base_url = "https://dantri.com.vn/suc-khoe.htm"

    # Create an empty list to store all review
    all_pages_post = []


    # Create a Scraper function
    def scraper():
        # Web scraping - fetching the reviews from the webpage using BeautifulSoup

        # loop through a range of page numbers
        for i in range(0, 1):  # fetching reviews from five pages

            # Creating an empty list to store the reviews of each page
            pagewise_reviews = []

            # Query parameter
            query_parameter = "?trang-=" + str(i)

            # Constructing the URL
            url = base_url + query_parameter

            # Send HTTP request to the URL
            response = requests.get(url)

            # Create a soup object and parse the HTML page
            soup = bs(response.content, 'html.parser')

            # Finding all the elements having reviews using class attribute
            rev_div = soup.findAll("div", attrs={"main", "article list", "article-content", "article-title"})
            # 	print(sub_heading.text)

            # loop through all the divs and append
            for j in range(len(rev_div)):
                # finding all the p tags to fetch only the review text
                pagewise_reviews.append(rev_div[j].find("a").text)

            # writing all the reviews into a list
            for k in range(len(pagewise_reviews)):
                all_pages_post.append(pagewise_reviews[k])

            # return the final list of reviews
        return all_pages_post


    # Driver code
    reviews = scraper()

    # Storing in a dataframe
    i = range(1, len(reviews) + 1)
    reviews_df = pd.DataFrame({'title': reviews}, index=i)

    # Writing to a text file
    reviews_df.to_csv('test.txt', sep='\t')

    print(reviews_df)

title = title()