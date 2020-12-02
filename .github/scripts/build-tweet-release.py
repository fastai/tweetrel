from fastcore.all import *
from ghapi import *
import tweepy

def twitter_api():
    consumer_key,consumer_secret,access_token,access_token_secret = context_secrets.TWITTER.split()
    auth = tweepy.OAuthHandler(consumer_key,consumer_secret)
    auth.set_access_token(access_token,access_token_secret)
    return tweepy.API(auth)

def tweet_text(payload):
    rel = payload.release
    owner,repo = re.findall(r'https://api.github.com/repos/([^/]+)/([^/]+)/', rel.url)[0]
    tweet_tmpl = "New #{repo} release: v{tag_name}. {html_url}\n\n{body}"
    res = tweet_tmpl.format(repo=repo, tag_name=rel.tag_name, html_url=rel.html_url, body=rel.body)
    if len(res)<=280: return res
    return res[:279] + "…"

def send_tweet():
    payload = context_github.event
    if 'workflow' in payload: payload = example_payload(Event.release)
    if payload.action == 'published': return twitter_api().update_status(tweet_text(payload))

send_tweet()

