# Python3-SimpleHTTPServer-with-SSL

## Usage
1. Git clone https://github.com/noobpk/Python3-SimpleHTTPServer-with-SSL.git
2. cd Python3-SimpleHTTPServer-withSSL/
3. Generate your certificate : 
	1. `chmod +x generate-cert-selfsign.sh`
	2. `./generate-cert-selfsign.sh`
4. Add your path of file `cert.pem`  to `server.py`
3. Start server: `python3 server.py`

## Configure browsers to allow your certificate

### Google Chrome
Access : `chrome://flags/#allow-insecure-localhost` and click `Enable`
### Firefox
Access: `about:config` then search `security.enterprise_roots.enabled` and click `True`


