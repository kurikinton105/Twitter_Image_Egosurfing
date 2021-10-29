import os
from os.path import join, dirname
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

api_url = os.environ.get("api_url")
print(api_url) # 読み込めているかの確認
prediction_key = os.environ.get("prediction_key")
image_url_test = os.environ.get("image_url_test")
consumer_key = os.environ.get("consumer_key")
consumer_secret = os.environ.get("consumer_secret")
access_key = os.environ.get("access_key")
access_secret = os.environ.get("access_secret")
webhook_url = os.environ.get("webhook_url")
search_word = "#yamayamayamayama"

