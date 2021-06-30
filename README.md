# slack-cleaner

Slack Cleaner, Alex edition.  Deletes all messages from a given slack channel.

I wrote this as the other slack-cleaners I tried using after a quick Google search turned up many projects using the old Slack API.

This one uses the official [python-slack-sdk](https://github.com/slackapi/python-slack-sdk)

It's designed to be ran as a script, so first thing's first, let's set up your environment.

## Create a Slack Token

You can create a new Slack App [here](https://api.slack.com/apps).  Make sure it's targeted to your desired workspace.  You can name the app as you wish, in my Workspace, it's named Cleaner.

Click "OAuth & Permissions" on the left sidebar, and provide the following User Token Scopes.  Note, I'm clearing messages from a private channel, so you might need less scopes.

* `channels:read` To read info about channels
* `groups:read` To read info about private channels
* `channels:history` To read the channel message history
* `groups:history` To read the private channel message history
* `users:read` To read the user details
* `chat:write` To delete messages

Note in my slack workspace, only Administrators can delete messages per the Workspace configuration.  I'm authorizing this app as my admin account in the Slack API website.

Once you've added the scopes, click "Connect Workspace" or "Reconnect Workspace" at the top, and authorize the app.  Note down the User OAuth Token.

## Clone the repo & setup python

This assumes you have python3 installed on your system.

```
git clone https://github.com/alex4108/slack-cleaner.git
cd slack-cleaner
pip3 install -r requirements.txt
```

## Set up your .env file

Create a file in the repo's root, eg `~/slack-cleaner`, named `.env`.  The `.env` should have three parameters.

You can also use `sample.env` as your starting point, however it must be named `.env`

* `SLACK_CHANNEL_ID` The ID of the Slack Channel, eg C1234567890
* `SLACK_BOT_TOKEN` The User OAuth Token provided by api.slack.com.
* `SEND_SPAM` Set to 0 for most cases.  Set to 1 if you want to send some spam to your target channel (for testing pagination)

## Run it?

`python3 cleaner.py` will delete all messages from the provided `SLACK_CHANNEL_ID`

# Contributing

Contributions are what make the open source community such an amazing place to be learn, inspire, and create. Any contributions you make are **greatly appreciated**.

1. Fork the project
1. Create your feature branch (`git checkout -b feature/AmazingFeature`)
1. Make changes, and update `CHANGELOG.md` to describe them.
1. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
1. Push to the branch (`git push origin feature/AmazingFeature`)
1. [Open a pull request](https://github.com/alex4108/slack-cleaner/compare)