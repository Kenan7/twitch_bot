# Escape From Tarkov Twitch Bot

![forthebadge made-with-python](http://ForTheBadge.com/images/badges/made-with-python.svg)

![GitHub license](https://img.shields.io/github/license/Kenan7/twitch_bot?style=for-the-badge)

# Installation 

Create the virtual environment
```bash
python3 -m virtualenv env
```
Activate the virtual environment
```bash
. env/bin/activate
```
Install the dependencies
```bash
pip install -r requirements.txt
```


# Configuration

Rename the `.env.example` to `.env`
```bash
mv .env.example .env
```

**JobStore will be handled later(memory), it will work without the scheduler with the current configurations**

## Well, how do I get my tokens?

#### For [IRC_TOKEN](https://twitchapps.com/tmi/)

#### For [CLIENT_ID](https://dev.twitch.tv/console/apps)
Create new app in [twitch dev console](https://dev.twitch.tv/console/apps) first. Then you will get [CLIENT_ID](https://dev.twitch.tv/console/apps)

#### Nick is actually your channel name if you did not create new account for your bot. If you did, then there you go.
