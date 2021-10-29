import get_tweet
import config
import costom_vision
import slack_notification


def main(search_worrd, scince_minute=10, debug=False):
    # ツイートの取得
    api = get_tweet.get_oauth()
    image_url_list = get_tweet.search(api, search_word, scince_minute=scince_minute)
    if debug:
        print(image_url_list)

    # 画像があった時に処理を行う
    if image_url_list != []:
        for image_url in image_url_list:
            # 画像をAzureで認識する
            result = costom_vision.prediction_image_url(image_url[1], threshold=0.5)
            if result != []:
                # 検索の結果があったらSlackに通知する
                result += f"\nTwitter URL : {image_url[0]}\nImage URL : {image_url[1]}"
                if debug:
                    print(result)
                webhook_url = config.webhook_url
                slack_notification.slack_notification(result, webhook_url)


if __name__ == "__main__":
    search_word = config.search_word
    main(search_word, scince_minute=10, debug=False)
