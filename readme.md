[![MIT License](https://img.shields.io/badge/License-MIT-green.svg)](https://choosealicense.com/licenses/mit/)
![Build Passing](https://img.shields.io/badge/Build-passing-green.svg)
![Maintainer Art Krylov](https://img.shields.io/static/v1?label=Maintainer&message=ArtKrylovv&color=blue)

# Dice-resume-updater 🎲🎲🎲

I like Python and don't like updating my resume on Dice, so I created a project that does it for me.

## How it works

Project relies on Selenium WebDriver package to interact with web app, Webdriver-manager to install browser driver on you machine and Schedule to execute jobs at specif time. Profile update is done by changing first name to dummy name and then back to real name.

![Demo](https://media.giphy.com/media/Ai6cYaZ0RruKJyxYsj/giphy.gif)
## Installation

Prerequisites: Python 3.10, Google Chrome (latest version)

Install dice-updater on Linux and macOS

```zsh
  git clone ''
  cd dice-updater
  pip3 install -r requirements.txt
  
```
    
## Usage
Before running script setup configuration in config.yaml file:

```yaml
headless: True
max_attempts: 3
autorun:
  status: True
  schedule: "00:01"

email: "mail@gmail.com"
password: "password"
real_name: "John"
dummy_name: "Noname"
```

| Key               | Type    | Description                                    |
|-------------------|---------|------------------------------------------------|
| headless          | Boolean | runs browser browser w/o opening GUI           |
| max_attempts      | int     | number of restarts in case NoSuchElement error |
| autorun status    | boolean | if False script runs only once                 |
| autorun schedule* | string  | time at which script will be executed          |
| email             | string  | your Dice profile email                        |
| password          | string  | your Dice profile password                     |
| real_name         | string  | first name on your Dice profile                |
| dummy_name        | string  | temporary name that will be used for update    |

* to enable autorun status must be set to True, script will run daily at scheduled time

Success/Failure screenshots are available at:

```zsh
./sceenshots
```


## Deployment

To deploy this project run:

```zsh
  cd dice-updater
  python3 main.py
```

## Authors

[@ArtKrylovv](https://www.github.com/ArtKrylovv)

I am Art and I have created this project. If you like it, please give it a ⭐️ star.

## License

[MIT](https://choosealicense.com/licenses/mit/)
