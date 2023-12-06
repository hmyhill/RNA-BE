from flask import request, Flask, jsonify
from newsdataapi import NewsDataApiClient

from flask_cors import CORS, cross_origin

# Initialises the API key
api = NewsDataApiClient(apikey='pub_317102f7a1f35b5bb1aad1bc348030fc41397')

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'


@app.route('/news/top', methods=['GET'])
def top_news():
    response = api.news_api(country='gb', language='en', domain='bbc', full_content=True, max_result=13)
    return response


@app.route('/news/tech', methods=['GET'])
def tech_news():
    response = api.news_api(country='gb', language='en', domain='bbc', full_content=True, max_result=13,
                            category='technology')
    return response


@app.route('/news/sport', methods=['GET'])
def sport_news():
    response = api.news_api(country='gb', language='en', domain='bbc', full_content=True, max_result=13,
                            category='sports')
    return response


@app.route('/news/entertainment', methods=['GET'])
def entertainment_news():
    response = api.news_api(country='gb', language='en', domain='bbc', full_content=True, max_result=13,
                            category='entertainment')
    return response


@app.route('/news/world', methods=['GET'])
def world_news():
    response = api.news_api(country='gb', language='en', domain='bbc', full_content=True, max_result=13,
                            category='world')
    return response


@app.route('/user/create', methods=['POST'])
def user_create():
    name = request.json['name']
    role = request.json['role']
    email = request.json['email']
    password = request.json['password']
    return request.json


@app.route('/user/login', methods=['GET'])
def user_login():
    email = request.json['email']
    password = request.json['password']
    return request.json


@app.route('/user', methods=['GET'])
def user():
    if request.method == 'GET':
        userID = request.form['userID']
        name = request.form['name']
        role = request.form['role']
        email = request.form['email']
        password = request.form['password']
        response = jsonify({'User Created'})
        response.status_code = 200
    else:
        response = jsonify({'Invalid Request'})
        response.status_code = 400
        return response


@app.route('/user/changepassword', methods=['GET'])
def user_changepassword():
    if request.method == 'GET':
        email = request.form['email']
        newpassword = request.form['newpassword']
        response = jsonify({'Password Changed'})
        response.status_code = 200
        return response
    else:
        response = jsonify({'Invalid Request'})
        response.status_code = 400
        return response


@app.route('/user/delete', methods=['DELETE'])
def user_delete():
    if request.method == 'DELETE':
        role = request.form['role']
        response = jsonify({'Role Changed'})
        response.status_code = 200
        return response
    else:
        response = jsonify({'Invalid Request'})
        response.status_code = 400
        return response


@app.route('/user/changepermissions', methods=['GET'])
def user_changepermissions():
    if request.method == 'GET':
        role = request.form['role']
        response = jsonify({'Role Changed'})
        response.status_code = 200
        return response
    else:
        response = jsonify({'Invalid Request'})
        response.status_code = 400
        return response


@app.route('/story/upload', methods=['POST'])
def story_upload():
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']
        category = request.form['category']
        image_url = request.form['image_url']
        response = jsonify({'Story Created'})
        response.status_code = 200
        return response
    else:
        response = jsonify({'Invalid Request'})
        response.status_code = 400
        return response


@app.route('/story/search', methods=['GET'])
def story_search():
    if request.method == 'GET':
        keyword = request.form['keyword']
        response = jsonify({'Story Retrieved'})
        response.status_code = 200
        return response
    else:
        response = jsonify({'Invalid Request'})
        response.status_code = 400
        return response


@app.route('/story/delete', methods=['DELETE'])
def story_delete():
    if request.method == 'DELETE':
        articleID = request.form['articleID']
        response = jsonify({'Story Deleted'})
        response.status_code = 200
        return response
    else:
        response = jsonify({'Invalid Request'})
        response.status_code = 400
        return response


if __name__ == '__main__':
    app.run(debug=True)
