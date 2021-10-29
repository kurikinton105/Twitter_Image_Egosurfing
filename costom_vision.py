import json
import config
import requests


def prediction_image_url(image_url, threshold=0.5):
    """
    AzureのCustom Visionを利用して画像の分類をする
    Input:
        image_url: （画像のURL）
        threshold: 閾値（デフォルト0.5）
    Output:
        return_text: 認識された時、確率とURL
                     認識されなかった時空の文字列
    """
    api_url = config.api_url
    prediction_key = config.prediction_key
    payload = {"Url": image_url}
    headers = {"content-type": "application/json", "Prediction-Key": prediction_key}
    r = requests.post(api_url, data=json.dumps(payload), headers=headers)
    r_json = r.json()
    # 検索を行う
    return_text = ""
    for target in r_json["predictions"]:
        if target["probability"] > threshold:
            return_text += f"{target['tagName']}が{round(target['probability'] * 100)}%の確率で含まれています\n"

    return return_text


if __name__ == "__main__":
    image_url = config.image_url_test
    print(prediction_image_url(image_url, threshold=0.5))
