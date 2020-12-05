# How to tweet your releases
> Send a tweet to let people know when you release software on GitHub.


It's great to release software. And even better when people actually know about it!

One way to let people know about your new software releases is to tell them on Twitter. But we're software developers, not social media managers -- so that means we *automate all the things*.

With tweetrel, you can have GitHub send a tweet for you whenever you make a release.

## Install

`pip install tweetrel`

## How to use

First, you need to add your Twitter API details as [GitHub secrets](https://docs.github.com/en/free-pro-team@latest/actions/reference/encrypted-secrets). You'll need to sign up for a [Twitter API](https://developer.twitter.com/en/docs) account if you don't already have one. Once you've signed up, Twitter will give you four keys: `consumer_key`, `consumer_secret`, `access_token`, and `access_token_secret`. Create a new secret called `TWITTER`, and paste those four keys in, with a space between each one.

If you need to send Tweets on behalf of a different user to the one attached to your login, you'll need to authenticate with Twitter as that user. Run `tweetrel-auth` in your terminal and follow the instructions, and it will give you the `access_token` and `access_token_secret` you need -- paste them (after a space) after your `consumer_key` and `consumer_secret` and that will let you send tweets as the user you authenticated as.

Next, in your terminal, `cd` to the root of your repo, and then run:

```bash
tweetrel-install
```

That will set `tweetrel` up for you to run automatically upon release. You'll see two folders added to your `.github` folder, containing the YAML workflow and python script. No additional setup is needed, other than pushing these to GitHub:

```bash
git add -A .github
git commit -am 'Add tweetrel`
git push
```

You can test this without actually making a release by going to your GitHub repo in your browser, clicking the *Actions* tab, then clicking on the *tweet* action, and clicking the *run workflow* button. That will use GitHub's example release payload for testing.

Once you've confirmed it's working, try making a release on GitHub, and check that you see the green tick in the Actions tab showing a successful run of the *tweet* action.
