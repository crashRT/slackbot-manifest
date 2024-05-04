import os
from dotenv import load_dotenv
from slack_bolt import App

# BOT_NUMの数だけSlack Appを作成する
BOT_NUM = 1

load_dotenv(".env")
TOKEN = os.getenv('TOKEN')

app = App(token=TOKEN)



for i in range(BOT_NUM):

  app_name = "SlackBot-team" + str(i)

  # まずアプリを作成
  init_manifest = {
    "display_information": {
        "name": app_name,
    }
  }

  resp = app.client.apps_manifest_create(token=TOKEN, manifest=init_manifest)

  if not resp["ok"]:
      raise Exception(resp)

  app_id = resp["app_id"]
  oauth_url = resp["oauth_authorize_url"]

  # 受け取った app_id と oauth_redirect_url を使って、manifest を更新
  # 権限の追加などを行う
  # TOKENは管理画面から取得するしかない

  manifest = {
    "display_information": {
        "name": str(app_name),
    },
    "features": {
      "bot_user": {
          "display_name":"hoge"
      },
    },
    "settings": {
      "socket_mode_enabled": True,
      "event_subscriptions": {
        "bot_events": [
        ]
      },
    },
    "oauth_config": {
      "scopes": {
        "bot": [
          "chat:write",
          "chat:write.public",
        ]
      },
      "redirect_urls": [
        str(oauth_url)
      ]
    }
  }

  resp = app.client.apps_manifest_update(
      token=TOKEN,
      app_id=app_id,
      manifest=manifest,
  )

  print("------------------")
  print(app_name + " を作成しました")
  print('''
  トークン等は管理画面から取得してください
  管理画面：https://api.slack.com/apps/'''+app_id)



