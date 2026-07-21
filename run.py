import os

from login_modify_actual import modify_post
from login_modify_normal import modify_normal_post

print("GitHub Actions 시작")

mode = os.environ["INPUT_MODE"]
user_id = os.environ["INPUT_ID"]
user_pw = os.environ["INPUT_PW"]
modify_url = os.environ["INPUT_URL"]
html = os.environ["INPUT_HTML"]
text = os.environ["INPUT_TEXT"]

if mode == "html":

    result = modify_post(
        user_id=user_id,
        user_pw=user_pw,
        modify_url=modify_url,
        html=html
    )

elif mode == "text":

    result = modify_normal_post(
        user_id=user_id,
        user_pw=user_pw,
        modify_url=modify_url,
        text=text
    )

else:
    raise ValueError(f"Unknown mode: {mode}")

print(result)
