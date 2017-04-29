from flask import Flask
from netifaces import interfaces, ifaddresses, AF_INET
from flask.ext.runner import Runner
app = Flask(__name__)
runner = Runner(app)

def ipv4_addresses():
    ip_list = []
    for interface in interfaces():
        try:
            for link in ifaddresses(interface)[AF_INET]:
                ip_list.append(link['addr'])
        except:
            pass
    return ip_list

@app.route('/')
def root():
    return '<br/>'.join(ipv4_addresses())

if __name__ == '__main__':
    runner.run()
