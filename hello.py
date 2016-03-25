import urllib2,urllib,re,time
cookies = urllib2.HTTPCookieProcessor()
print cookies
opener = urllib2.build_opener(cookies)
myre = re.compile(r'name="_xsrf" value="[a-zA-Z0-9]+"')
opener.addheaders = [('User-agent', 'Mozilla/5.0 (Windows NT 6.2; rv:16.0) Gecko/20100101 Firefox/16.0'),('Origin','1.bloodycoder.sinaapp.com'),('Accept','text/html'),('Connection','keep-alive')]
f = opener.open('http://www.zhihu.com')
xsrf = myre.findall(f.read())
xsrf = xsrf[0][19:]
formdata = { "email" : "510297127@qq.com","password": "992288" ,"remember_me":"true","_xsrf":xsrf}
data_encoded = urllib.urlencode(formdata)
response = opener.open("http://www.zhihu.com/login/email", data_encoded)
print response.read();
response = opener.open("https://www.zhihu.com/people/er-de-cha/followers");
find_name = re.compile(r'"https://www.zhihu.com/people/[A-Za-z0-9_]+"')
get_chinesename_re = re.compile(r"<title>[^<]+")
get_location_re = re.compile(r"<span class=\"location item\" title=\"[^\"]*\">")
get_employment_re =re.compile(r'<span class="employment item" title="[^>]+>')
get_education_re = re.compile(r'<span class="education item" title="[^>]+>')
get_position_re = re.compile(r'<span class="position item" title="[^>]+')
result = find_name.findall(response.read())
result = set(result)
result = list(result)
print result
x=0
name_set = set()
name_set.add('er-de-cha')
fout = open('data','a')
while(1):
    time.sleep(0.5)
    now_to_process = result[x];
    now_to_process = now_to_process[1:-1]
    hisid = now_to_process.split('/')
    hisid = hisid[-1]
    if(hisid in name_set):
        x = x+1;
        continue;
    name_set.add(hisid)
    website_to_get = "https://www.zhihu.com/people/"+hisid+"/followers"
    response = opener.open(website_to_get);
    html = response.read()
    new_result = find_name.findall(html)
    new_result = set(new_result)
    new_result = list(new_result)
    try:
        chinese_name = get_chinesename_re.findall(html)[0][7:-21]
    except:
        chinese_name = 'null'
    try:
        location = get_location_re.findall(html)[0][35:-2]
    except:
        location = 'null'
    try:
        employment = get_employment_re.findall(html)[0][37:-2]
    except:
        employment = 'null'
    try:
        education = get_education_re.findall(html)[0][36:-2]
    except:
        education = 'null'
    try:
        position = get_position_re.findall(html)[0][35:-1]
    except:
        position = 'null'
    print chinese_name,location,education,employment,position
    if((chinese_name=='null')+(location=='null')+(education=='null')+(employment=='null')+(position=='null')<=3):
        fout.write(chinese_name+' '+location+' '+education+' '+employment+' '+position+'\n')
    if(x>100000):
        fout.close()
        exit()
    if(x+10>= len(result)):
        for item in new_result:
            result.append(item)
    x = x+1