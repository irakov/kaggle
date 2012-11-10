#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Copyright (c) 2012, Ivan Yurchenko <ivan0yurchenko@gmail.com>
#
# Permission is hereby granted, free of charge, to any person obtaining
# a copy of this software and associated documentation files (the
# "Software"), to deal in the Software without restriction, including
# without limitation the rights to use, copy, modify, merge, publish,
# distribute, sublicense, and/or sell copies of the Software, and to
# permit persons to whom the Software is furnished to do so, subject to
# the following conditions:
#
# The above copyright notice and this permission notice shall be
# included in all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
# EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
# MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
# NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE
# LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION
# OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION
# WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

import sys, re
from getpass import getpass
import urllib.request, urllib.parse
import codecs

def handle_general_error():
    print('Something went wrong!')
    exit(1)

def print_usage():
    print('Usage:')
    print('  kaggle_login.py username password out_file')
    print('or:')
    print('  kaggle_login.py out_file')
    print('and input username and password interactively.')

def main(argv):
    if len(argv) == 2:
        username = input('Username: ')
        password = getpass('Password: ')
        out_file = argv[1]
    elif len(argv) == 4:
        username = argv[1]
        password = argv[2]
        out_file = argv[3]
    else:
        print_usage()
        exit(1)

    url = "https://kaggle.com"
    page = urllib.request.urlopen(url).read().decode('utf-8')
    # make one line 
    page = page.replace('\n', '').replace('\r', '')
    # parse (I do know about non-regularity of HTML, but it's ok here)
    m = re.search('\<form.+?id\s*=\s*"signin".+?\<\/form\>', page, re.I)
    if not m:
        handle_general_error()

    form_text = m.group(0)
    # action url
    m = re.search('action\s*=\s*"(.+?)"', form_text, re.I)
    if not m:
        handle_general_error()
    action_url = m.group(1)

    # find request token, returnUrl and other data
    reqTokenTagName = '__RequestVerificationToken'
    token = None
    returnUrl = None
    for input_text in re.findall('\<input.+?\>', form_text, re.I):
        m = re.search('name\s*=\s*"{0}"'.format(reqTokenTagName), input_text, re.I)
        if m:
            token = re.search('value\s*=\s*"(.+?)"', input_text, re.I).group(1)
            continue

        m = re.search('name\s*=\s*"returnUrl"', input_text, re.I)
        if m:
            returnUrl = re.search('value\s*=\s*"(.+?)"', input_text, re.I).group(1)
            continue
    if not token or not returnUrl:
        handle_general_error()

    pass_data = {}
    pass_data['JavaScriptEnabled'] = 'true'
    pass_data['returnUrl'] = returnUrl
    pass_data['rememberMe'] = 'true'
    pass_data[reqTokenTagName] = token
    pass_data['UserName'] = username
    pass_data['Password'] = password
    params = urllib.parse.urlencode(pass_data).encode('utf-8')

    import http.cookiejar

    authTokenName = '.ASPXAUTH'
    cj = http.cookiejar.CookieJar()
    opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cj))
    r = opener.open(action_url, data=params)

    page = r.read().decode('utf-8').replace('\n', '').replace('\r', '')
    invalid_login_error_text = 'The username or password provided is incorrect.'
    if invalid_login_error_text in page:
        sys.stderr.write(invalid_login_error_text + '\n')
        exit(1)

    for cookie in cj:
        if cookie.name != authTokenName:
            continue
        cookies_string = '{0}\tTRUE\t/\tFALSE\t{1}\t{2}\t{3}'.format('.kaggle.com', cookie.expires, cookie.name, cookie.value)
        break

    f = codecs.open(out_file, mode='w', encoding='utf8')
    f.write(cookies_string)
    f.write('\n')
    f.close()

#---
if __name__ == "__main__":
    main(sys.argv)
