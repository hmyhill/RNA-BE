import flask
import requests
from flask import app, request, Flask
from newsdataapi import NewsDataApiClient

# Initialises the API key
api = NewsDataApiClient(apikey='pub_317102f7a1f35b5bb1aad1bc348030fc41397')


# Request Parameters
def top_news():
    response = api.news_api(country='gb', language='en', domain='bbc', full_content=True, max_result=13)
    print(response)


def tech_news():
    response = api.news_api(country='gb', language='en', domain='bbc', full_content=True, max_result=13,
                            category='technology')
    print(response)


def sport_news():
    response = api.news_api(country='gb', language='en', domain='bbc', full_content=True, max_result=13,
                            category='sports')
    print(response)


def entertainment_news():
    response = api.news_api(country='gb', language='en', domain='bbc', full_content=True, max_result=13,
                            category='entertainment')
    print(response)


def world_news():
    response = api.news_api(country='gb', language='en', domain='bbc', full_content=True, max_result=13,
                            category='world')
    print(response)