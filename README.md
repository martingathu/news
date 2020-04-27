# Global News Highlight
An application that will help users to preview news articles from various sources around the globe.   

## Built By [Martin Gathu](https://github.com/martingathu/)

## Description
Global News Highlight is a web application that displays a list of various news sources like BBC and ABC. On choosing a news source, it will preview the top news articles of the day. Clicking a news article will redirect the user to read it fully from the news source. It achieves this by using the [News API](https://newsapi.org/).

#### You can view the site at: 

## User Stories
These are the behaviours/features that the application implements for use by a user.

As a user I would like to:
* See various news sources 
* Select the ones they prefer
* See the top news articles from that news source
* See the image, description and time the news article was created
* Click on an article and read it fully from the news source

## Specifications
| Behaviour | Input | Output |
| :---------------- | :---------------: | ------------------: |
| Display news sources | **On page load** | List of various news sources is displayed per category |
| Display articles from a news source | **Click on View A rticles on a news source** | Redirected to a page with a list of articles from the source |
| Display the preview of an article | **On page load** | Each article displays an image, title, description and publication date |
| Read an entire article | **Click Read More** | Redirected to the news source's site to read the entire article |
| Go back to news sources | **Click on Global News Highlight** | Redirected to the news source list |
## SetUp / Installation Requirements
### Prerequisites
* python3.6
* pip
* virtualenv

