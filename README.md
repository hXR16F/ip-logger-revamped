<p align="center">
	<b>ip-logger-revamped</b>
	<br>
  <i>IP Logger Revamped is a Python script built with Flask to log client IP addresses and user agents.</i>
	<br><br><img alt="vid" src="https://github.com/hXR16F/ip-logger-revamped/assets/48186982/9ac3c0cf-c1e2-4dfd-b298-20ce0d380919">
</p>

# Overview
**IP Logger Revamped** is a Python script utilizing Flask, aimed at logging client IP addresses and user agents.\
This tool not only records crucial information but also offers the flexibility to redirect clients to a specified URL and generate shortened links for convenient access to the logging endpoint.\
This project is an evolution of its predecessor: [hXR16F/IP-Logger](https://github.com/hXR16F/IP-Logger).

# Features
* Logs client IP addresses, user agents, and timestamps into a designated file (ip-logger-revamped.txt).
* Option to redirect clients to a specified URL.
* Generates shortened links using various URL shortening services.

# Installation
1. Install Ngrok by following the instructions at [ngrok.com](https://ngrok.com) and add it to environment variable.
2. Clone this repository:
```
git clone https://github.com/hXR16F/ip-logger-revamped.git
cd ip-logger-revamped
```
3. Install the required Python libraries:
```
pip install -r requirements.txt
```
4. Run the script:
```
python ip-logger-revamped.py
```

# Usage
Once the script is running, it listens for incoming connections.\
Client IP addresses, user agents, and timestamps are logged into the ip-logger-revamped.txt file.\
If a redirect URL is specified, clients are redirected; otherwise, a 404 error is returned.

# Notes
Please be aware that URL shortening services may have rate limits.

# Donate
If you support my work or like my projects, [you can donate me some money](https://github.com/hXR16F/donate/blob/master/README.md). Thank you 💙
