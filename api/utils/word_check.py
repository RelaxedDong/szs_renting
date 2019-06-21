import re

class WordCheck:
    address_regex = re.compile(r"[\u4e00-\u9fa5]+省|[\u4e00-\u9fa5]+市")
    fileMD5_regex = re.compile(r'^\b[A-F0-9]{32}\b$')
    uuid_regex = re.compile(r'^\w{3}_\w{12}$')
    check_number_regex = re.compile(r'^\d{6}$')
    birth_ym = re.compile(r'^\d{4}-\d{2}$')
    searchBar_regex = re.compile(r'[\'\"\*,;?=&\(\)\[\]\<\>%{}\\]|(update|delete|select)')
    username_regex = re.compile(r'[\*;?\\\+=&\(\)\[\]\<\>%{}]')
    email_regex = re.compile(r"\w[-\w.+&!#$%&'*+-/=?^_`{|}~]*@([A-Za-z0-9+-_]+\.)+[A-Za-z]{2,14}")
    url_regex = re.compile(r'(https?|ftp|file)://')
    tel_regex = re.compile(r'^1[0-9]{10}$')
    over_sea_tel_regex = re.compile(r'^[0-9\+\-\s]{11,15}$')
    digital_regex = re.compile(r'^-?\d+$')
    sso_suffix = re.compile(r'_(QQ|wb|wt)_\w{4}$')

    newline = re.compile(r'[\f\v]+|\r|</p>|</li>|</ul>|<br>|<br />', re.S)
    space = re.compile(r'<[^>]+>|\t', re.S)
    re_new_line = re.compile(r'\n{1,}', re.S)
    filepath_regex = re.compile(r'[A-F0-9][A-F0-9]/[A-F0-9][A-F0-9]/[A-F0-9]{32}.[A-Za-z]{1,10}', re.S)

    # 搜索参数格式
    searchArgs_regex = re.compile(r'[a-z]{1,2}-(?:\d+,\d+|[a-z]+|\d+)')
    pointUuid_regex = re.compile(r'\w{8}-\w{4}-\w{4}-\w{4}-\w{12}')
    intern_date_regex = re.compile(r'\d{4}-\d{2}')
    split_regex = re.compile(r',|，|;|;| |、|。')