#!/usr/bin/python
# -*- coding: UTF-8 -*-
import mechanize
import time
from getpass import getpass

MAX_DELAY = 60
loginURL = "https://m.facebook.com/login"
pokeURL = "https://m.facebook.com/pokes"

def login(user, passw):
	browser = mechanize.Browser()
	cj=mechanize.CookieJar()
	browser.set_cookiejar(cj)
	browser.set_handle_robots(False)
	browser.addheaders = [('User-agent', 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:20.0) Gecko/20100101 Firefox/20.0')]
	browser._factory.is_html = True
	loginpage=browser.open(loginURL)

	browser.select_form(nr=0)
	browser.form["email"] = user
	browser.form["pass"] = passw

	browser.submit()

	loginpage.close()
	if browser.title() != "Facebook":
		print "Wrong id or password"
		return False
	else:
		print "Login Success"
		return browser

def main():
	browser=False
	while browser==False:
		user=raw_input("User ID: ").strip()
		passw=getpass().strip()
		browser=login(user, passw)
	
	try:
		delay=1
		while True:
			pokepage=browser.open(pokeURL)
			pokelinks=[]
			for pokelink in browser.links(text_regex="나도 콕 찔러보기"):
				print "we found a poke!"
				pokelinks.append(pokelink.url)
			find=len(pokelinks)
			for link in pokelinks:
				res=browser.open(link)
				res.close()
				print "poke back!!"
			pokepage.close()
			if find==0:
				delay=(delay*2)%MAX_DELAY;
			else:
				delay=(delay/2)+1;
			time.sleep(delay);
	except:
		print "Error!!!!"

if __name__=="__main__":
	main()
