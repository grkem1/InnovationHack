import requests


def read_kw(fname):
    rv = []
    with open(fname) as f:
        for line in f:
            line = line.rstrip('\n')
            rv.append(set(line.split(' ')))
    return rv


def dangerous(tags, keywords):
    for cur_set in keywords:
        set_ok = False
        for cur_word in cur_set:
            if cur_word in tags:
                set_ok = True
                break
        if not set_ok:
            return False
    return True


def request_tags(image_path, subscription_key):
    vision_base_url = "https://westcentralus.api.cognitive.microsoft.com/vision/v1.0/"
    vision_analyze_url = vision_base_url + "analyze"

    headers = {'Ocp-Apim-Subscription-Key': subscription_key}
    params = {'visualFeatures': 'Description'}
    img_bin = open(image_path, 'rb')
    files = {'file': img_bin}
    response = requests.post(vision_analyze_url, headers=headers, params=params, files=files)
    img_bin.close()
    response.raise_for_status()
    return set(response.json()['description']['tags'])


def discriminate(subscription_key, keywords, image_path):
    tags = request_tags(image_path, subscription_key)
    return dangerous(tags, keywords)



