#!/bin/bash
#generate your certificate self-signed using on local
openssl req -new -x509 -sha256 -nodes -newkey rsa:2048 -days 365 -keyout cert.pem -out cert.pem