import re
import time 

fin = open('getinfo.html')
content = fin.read();
"""
content =  fin.read()
fin.close()
myre = re.compile(r'"https://www.zhihu.com/people/[A-Za-z0-9_]+"')
result = myre.findall(content)
result = set(result)
result = list(result)
print result
time.sleep(10)
"""
x = 'gaocegege'
get_chinesename_re = re.compile(r"<title>[^<]+")
chinese_name  = get_chinesename_re.findall(content)[0][8:-21]
get_location_re = re.compile(r"<span class=\"location item\" title=\"[^\"]*\">")
location = get_location_re.findall(content)[0][35:-2]
get_employment_re =re.compile(r'<span class="employment item" title="[^>]+>')
employment = get_employment_re.findall(content)[0][37:-2]
get_education_re = re.compile(r'<span class="education item" title="[^>]+>')
education =  get_education_re.findall(content)[0][36:-2]
get_position_re = re.compile(r'<span class="position item" title="[^>]+')
position = get_position_re.findall(content)[0][35:-1]
print chinese_name
print location
print employment
print position
print education
