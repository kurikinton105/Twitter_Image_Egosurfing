import requests, json
import config


def slack_notification(message, webhook_url):

    response = requests.post(
        webhook_url,
        data=json.dumps(
            {
                "text": f"{message}",  # 通知内容
                "username": "エゴサBot",  # ユーザー名
                "icon_emoji": ":smile_cat:",  # アイコン
            }
        ),
    )
    return response.text


if __name__ == "__main__":
    message = "test"
    webhook_url = config.webhook_url
    slack_notification(message, webhook_url)
