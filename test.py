import requests
import  json

slack_web_hook = 'https://hooks.slack.com/services/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'

def send_slack(event, context):
    print(str(event))
    slack_message = {'text':'EC2 Stopped'}
    resp = requests.post(slack_web_hook, data=json.dumps(slack_message))
    return resp.text