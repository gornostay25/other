#!/usr/bin/bash
pkg install clang
pkg install libzmq
pkg install python
pkg install openssl
pkg install libffi
pkg install libcrypt
pkg install libzmq-dev
pkg install python-dev 
pkg install openssl-dev 
pkg install libffi-dev 
pkg install libcrypt-dev
LD_PRELOAD="/data/data/com.termux/files/usr/lib/libzmq.so" 
TERMUX_PKG_HOMEPAGE=http://www.tldp.org/HOWTO/Software-Building-HOWTO.html
TERMUX_PKG_DESCRIPTION="Collection of packages to build Linux software"
TERMUX_PKG_VERSION=0.1
TERMUX_PKG_DEPENDS="clang, gawk, make, sed"
TERMUX_PKG_METAPACKAGE=yes
TERMUX_PKG_PLATFORM_INDEPENDENT=yes
pip3 install --upgrade pip
pip3 install click
pip3 install typing 
pip3 install cffi
pip3 install pycparser
pip3 install six asn1crypto
pip3 install idna
pip3 install pretty_cron 
pip install pipenv
pip3 install netifaces
pip3 install zeroconf 
pip3 install attrs 
pip3 install appdirs
pip3 install cryptography
pip3 install construct==2.8.21
CFLAGS=-I/usr/include/libffi/include pip3 install pyOpenSSL
pip3 install certifi
pip3 install homeassistant
pip3 indtall python3-cffi-backend
pip3 install -U https://github.com/rytilahti/python-miio/archive/master.zip
pip3 install python-mirobo
