# `DISCORD-BOT`

[<img src="https://img.icons8.com/color/48/000000/discord-logo.png" align="right" width="15%" padding-right="350">]()

<p align="left">
	<img src="https://img.shields.io/github/license/TejasShinkar12/Discord-Bot?style=flat&logo=opensourceinitiative&logoColor=white&color=0080ff" alt="license">
	<img src="https://img.shields.io/github/languages/top/TejasShinkar12/Discord-Bot?style=flat&color=0080ff" alt="repo-top-language">
	<img src="https://img.shields.io/github/languages/count/TejasShinkar12/Discord-Bot?style=flat&color=0080ff" alt="repo-language-count">
</p>
<p align="left">
		<em>Built with the tools and technologies:</em>
</p>
<p align="center">
	<img src="https://img.shields.io/badge/Replit-F26207.svg?style=flat&logo=Replit&logoColor=white" alt="Replit">
	<img src="https://img.shields.io/badge/C-A8B9CC.svg?style=flat&logo=C&logoColor=black" alt="C">
	<img src="https://img.shields.io/badge/Poetry-60A5FA.svg?style=flat&logo=Poetry&logoColor=white" alt="Poetry">
	<img src="https://img.shields.io/badge/Discord-5865F2.svg?style=flat&logo=Discord&logoColor=white" alt="Discord">
	<img src="https://img.shields.io/badge/PowerShell-5391FE.svg?style=flat&logo=PowerShell&logoColor=white" alt="PowerShell">
	<br>
	<img src="https://img.shields.io/badge/Python-3776AB.svg?style=flat&logo=Python&logoColor=white" alt="Python">
	<img src="https://img.shields.io/badge/pandas-150458.svg?style=flat&logo=pandas&logoColor=white" alt="pandas">
	<img src="https://img.shields.io/badge/NumPy-013243.svg?style=flat&logo=NumPy&logoColor=white" alt="NumPy">
	<img src="https://img.shields.io/badge/Flask-000000.svg?style=flat&logo=Flask&logoColor=white" alt="Flask">
	<img src="https://img.shields.io/badge/JSON-000000.svg?style=flat&logo=JSON&logoColor=white" alt="JSON">
</p>

<br>

<hr>

##  Overview

**Discord Bot** is a custom solution designed to keep members of a college tech club informed with daily updates from the tech world. The bot automates the process of scraping a specific email newsletter received by me and delivers it as a well-formatted message to a designated Discord server channel. This ensures that all members can stay up to date with the latest tech news and trends without needing to subscribe to individual newsletters.

This project aims to provide a seamless way for a group of people to access valuable information in one central place, fostering a sense of community and ensuring that no one misses important updates.

### Key Points:
- **Target Audience**: Club members and anyone interested in tech-related news.
- **Tech Stack**: Python for the bot logic, Flask for keeping the script continuously running, BeautifulSoup4 for web scraping and tools like Pandas and NumPy for HTML data cleaning.
- **Motivation**: The bot was created to streamline access to tech news, avoiding the hassle of individual subscriptions and enabling easy access for the entire community.

---

##  Features

- **Automated Newsletter Scraping**: The bot automatically scrapes a tech newsletter received via email, extracting the most relevant content for the Discord server.
- **Discord Integration**: Posts daily updates as a message to a designated channel in the Discord server, providing an organized and centralized source of tech news.
- **Continuous Running Script**: A simple Flask server ensures the bot runs continuously by being pinged every 10 minutes from an external site.
- **Customization Options**: The output format is customizable, with ongoing improvements aimed at making the newsletter message more visually appealing.
- **Community-Friendly**: Provides value to all members of the Discord server, eliminating the need for individual registrations to newsletters.

### Planned Features:
- **Improved Message Formatting**: The next step is to enhance the aesthetics of the Discord messages to improve readability and engagement.

---

##  Repository Structure

```sh
└── Discord-Bot/
    ├── bot.py
    ├── get_mail.py
    ├── keep_alive.py
    ├── main.py
    ├── poetry.lock
    ├── pyproject.toml
    ├── reddit_posts.py
    ├── replit.nix
    ├── responses.py
    └── venv
        ├── bin
        ├── lib
        ├── lib64
        ├── pyvenv.cfg
        └── src
```

---

##  License

This project is protected under the [SELECT-A-LICENSE](https://choosealicense.com/licenses) License. For more details, refer to the [LICENSE](https://choosealicense.com/licenses/) file.

---
