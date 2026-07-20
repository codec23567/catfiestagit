import os

from login_modify_actual import modify_post

print("GitHub Actions 시작")

user_id = os.environ["INPUT_ID"]
user_pw = os.environ["INPUT_PW"]
modify_url = os.environ["INPUT_URL"]
html = os.environ["INPUT_HTML"]

result = modify_post(
    user_id=user_id,
    user_pw=user_pw,
    modify_url=modify_url,
    html=html
)

print(result)
