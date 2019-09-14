# SMM Posting
A script posts text with image in different media: Telegram, VK, FB.

# How to install
The script uses enviroment file with Instagram authorization data. The file '.env' must include following data:
- VK [group id](http://regvk.com/id/) "VK_GROUP_ID", album id "VK_ALBUM_ID" and [token](https://vk.com/dev/implicit_flow_user) "VK_ACCESS_TOKEN" with following permissions: photos, groups, wall and offline. 
- Telegram Bot [token](https://smmplanner.com/blog/otlozhennyj-posting-v-telegram/) "TELEGRAM_BOT_TOKEN" and channel id "TELEGRAM_CHANNEL_ID".
- FaceBook application [marker](https://developers.facebook.com/tools/explorer/) "FB_APP_TOKEN" and group id "FB_GROUP_ID"

Python3 should be already installed. Then use pip3 (or pip) to install dependencies:

```bash
pip3 install -r requirements.txt
```

# How to launch
Launch main.py to publish post in three social media.  
The Example of launch in Ubunru is:

```bash
$ python3 main.py text.txt image.jpg
Post is published in Telegram.
Post is published in FB.
Post is published in VK.
```
If any error occured you get message as:

```bash
$ python3 main.py
Error occured while authentification in Telegram: Invalid token
Error occured, post can't be published in FB:
{'error': {'message': 'Invalid OAuth access token.', 'type': 'OAuthException', 'code': 190, 'fbtrace_id': 'AGiMx-CZhK7lVqDmG3gx9Ua'}}
VK Api Error occured while uploading photo to VK server:
[5] User authorization failed: invalid access_token (4).
```
The launch in Windows and OS is the same.

# Project Goals

The code is written for educational purposes on online-course for web-developers dvmn.org, module Python for SMM.
