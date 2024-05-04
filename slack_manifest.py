import os
from dotenv import load_dotenv
from slack_bolt import App

load_dotenv(".env")
TOKEN = os.getenv('TOKEN')

app = App(token=TOKEN)

manifest = {
  "display_information": {
      "name": "Test Manifest App",
  }
}
resp = app.client.apps_manifest_create(token=TOKEN, manifest=manifest)

if not resp["ok"]:
    raise Exception(resp)

app_credentials = resp["credentials"]
app_id = resp["app_id"]

manifest = {
  "display_information": {
      "name": "Test Manifest App",
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
        "connections"
      ]
    },
  },
  "oauth_config": {
    "scopes": {
      "bot": [
        "chat:write",
        "chat:write.public",
        "connections:write",
      ]
    },
    "redirect_urls": [
      "https://slack.com/oauth/v2/authorize?client_id=3069876617.7053870738663"
    ]
  }
}

resp = app.client.apps_manifest_update(
    token=TOKEN,
    app_id=app_id,
    manifest=manifest,
)

print(resp)

# slack のAPIを使ってSlackBotを作成する
# 必要なトークンはTOKENに格納してある

