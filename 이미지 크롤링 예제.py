import requests
import json

def save_image(image_url, file_name):
    img_response = requests.get(image_url)
    if img_response.status_code == 200:
        with open(file_name, "wb") as fp:
            fp.write(img_response.content)

tofind = "영진 구론산 바몬드 오리지날"
url = "https://dapi.kakao.com/v2/search/image"
headers = {
    "Authorization" : "KakaoAK 67db11fcdbb05a32b9788d0ea29fe7f5"
}
data = {
    "query" : tofind
}

response = requests.post(url, headers=headers, data=data)
if response.status_code != 200:
    print("error! because ",  response.json())
else:
    print(list(response.json().values())[0][0])
    file_name = "{0}.jpg".format(tofind)
    save_image(list(response.json().values())[0][0]['image_url'], file_name)
