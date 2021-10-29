import tweepy
import datetime

# import pytz
import config


def get_oauth():
    consumer_key = config.consumer_key
    consumer_secret = config.consumer_secret
    access_key = config.access_key
    access_secret = config.access_secret
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_key, access_secret)
    api = tweepy.API(auth)
    return api


def search(api, search_word, scince_minute=10):
    """
    Input:
        api: tweepy.API
        search_word: str
        scince_minute: int
    Output:
        image_url_list: list
        [[tweer_url, image_url], [tweer_url, image_url], ...]
    """
    query = search_word  # 検索したい単語を入力
    count = 30  # 検索したい数を入力
    # YYYY-MM-DD_hh:mm:ssの形式で時間を入力
    sinceDate = str(
        (datetime.datetime.now() - datetime.timedelta(minutes=scince_minute)).strftime(
            "%Y-%m-%d_%H:%M:%S"
        )
    )
    # print(sinceDate)
    image_url_list = []
    sratchStr = query + " since:" + sinceDate + "_JST exclude:retweets"
    for result in api.search(q=sratchStr, count=count):
        # print(result)

        if "media" in result.entities:
            for media in result.entities["media"]:
                url = media["media_url_https"]
                tweet_url = (
                    f"https://twitter.com/{result.user.screen_name}/status/{result.id}"
                )
                image_url_list.append([tweet_url, url])
    return image_url_list


if __name__ == "__main__":
    api = get_oauth()
    print(search(api, "青りんご"))
