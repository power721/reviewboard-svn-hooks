#!/usr/bin/python
# -*- coding:utf8 -*-

import sys
import subprocess
import urllib2
import cookielib
import base64
import re
import json

RB_SERVER = r'http://192.168.0.109:9000/'

SVR = '192.168.0.109:9000'
USERNAME = 'admin'
PASSWORD = 'how1982'
BASE64_AUTH = base64.b64encode(USERNAME + ':' + PASSWORD)
print BASE64_AUTH
print 'jjjjjjjjjjjjjjjjjjjjjjjjjjjjjjj'

cookie_file = '/tmp/review-board-cookies.txt'
cookie_jar = cookielib.MozillaCookieJar(cookie_file)
cookie_handler = urllib2.HTTPCookieProcessor(cookie_jar)
opener = urllib2.build_opener(cookie_handler)
urllib2.install_opener(opener)


url = 'http://' + SVR + '/api/review-requests/126/diffs/1/files/757/'
print url
try:
	r = urllib2.Request(url)
	r.add_header('Authorization', 'Basic ' + BASE64_AUTH)
	r.add_header('Accept', 'text/x-patch')
	rsp = urllib2.urlopen(r)
	print dir(rsp)
	print 'X' * 80
	print rsp.read()
except urllib2.URLError, e:
	print e
	print 'error'

def debug(s):
	f = open('/tmp/svn-hook.log', 'at')
	print >>f, s
	f.close()

def make_svnlook_cmd(directive, repos, txn):
	return ['svnlook', directive, '-t',  txn, repos]

def get_cmd_output(cmd):
	return subprocess.Popen(cmd, stdout = subprocess.PIPE).communicate()[0]

def get_review_id(repos, txn):
	svnlook = make_svnlook_cmd('log', repos, txn)
	log = get_cmd_output(svnlook)
	rid = re.search(r'review:([0-9]+)', log, re.M | re.I)
	if rid:
		return rid
	raise SvnError('No review id.')

def get_patch(diff_url):
#	try:
	pass


def get_review_diff(rid):
	url = RB_SERVER + 'api/json/review-requests/' + str(rid) + 'diffs/'
	debug('HTTP GETing ' + url)
	try:
		rsp = urllib2.urlopen(url).read()
	except urllib2.HTTPError, e:
		raise SvnError('HTTP GETing ' + url + 'error.' + str(e))
	diffs = json.loads(rsp)
	diff_files_url = diffs['diffs'][-1]['links']['files']['href']
	try:
		rsp = urllib2.urlopen(url).read()
	except urllib2.HTTPError, e:
		raise SvnError('HTTP GETing' + diff_files_url + 'error.' + str(e))
	files = json.loads(rsp)
	for f in files['files']:
		diff_url = f['links']['self']['href']
		patch = get_patch(diff_Url)
		source_file = f['source_file']
		
	



class SvnError(StandardError):
	pass

def check_rb(repos, txn):
	review_id = get_review_id(repos, txn)
	review_diff = get_review_diff(review_id)


	svnlook = make_svnlook_cmd('diff', repos, txn)
	diff = get_cmd_output(svnlook)
	tmpfile = '/tmp/reviewboard-diff-' + txn
	try:
		with open(tmpfile, 'wb') as f:
			f.write(diff)
	except (OSError, IOError), e:
		raise SvnError(str(e))

#	rb_diff = get_rb_diff(

def main():
	return
	debug('command:' + str(sys.argv))

	repos = sys.argv[1]
	txn = sys.argv[2]

	svnlook = make_svnlook_cmd('changed', repos, txn)
	changed = get_cmd_output(svnlook)
	for line in changed.split('\n'):
		f = line[4:]
		debug(type(f))
		# 有提交到主干分枝的代码，触发检测。
		if 'trunk/src/server/' in f:
#			check_rb(repos, txn)
			return
	return

try:
	main()
except SvnError, e:
	print >> sys.stderr, str(e)
	exit(1)
else:
	exit(0)

