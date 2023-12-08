<p align="center">
	<b>ip-logger-revamped</b>
	<br>
  <i>IP Logger Revamped is a Python script built with Flask to log client IP addresses and user agents.</i>
	<br><br><img alt="vid" src="https://github.com/hXR16F/ip-logger-revamped/assets/48186982/9ac3c0cf-c1e2-4dfd-b298-20ce0d380919">
</p>

# Overview
IP Logger Revamped is a Python script built with Flask to log client IP addresses and user agents.\
It provides the ability to redirect clients to a specified URL and generates shortened links for easy access to the logging endpoint.\
This project is a continuation of my previous version: [hXR16F/IP-Logger](https://github.com/hXR16F/IP-Logger).

# Features
* Logs client IP addresses, user agents, and timestamps into a designated file (ip-logger-revamped.txt).
* Option to redirect clients to a specified URL.
* Generates shortened links using various URL shortening services.

# Installation
1. Install the required Python libraries:
```
pip install flask requests pyngrok colorama waitress
```
2. Install Ngrok by following the instructions at [ngrok.com](https://ngrok.com).
3. Clone the repository:
```
git clone https://github.com/hXR16F/ip-logger-revamped.git
cd ip-logger-revamped
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
URL shortening services may have rate limits.

# Donate
If you support my work or like my projects, [you can donate me some money](https://github.com/hXR16F/donate/blob/master/README.md). Thank you 💙
