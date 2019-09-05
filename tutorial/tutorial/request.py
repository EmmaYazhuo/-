import urllib.request
f = urllib.request.urlopen('https://banner.apps.uillinois.edu/StudentRegistrationSSB/ssb/classRegistration/classRegistration')
result = f.read().decode('utf-8')
print(result)

