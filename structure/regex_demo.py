import re

if __name__ == '__main__':
    reStr = r'< img src="1a66ece32e827c62cc748c6a13ce2afb.jpg" />'
    patternStr = r'^< img.*src=\"(.*)\".*/>$'
    pattern = re.compile(patternStr)
    findall = pattern.findall(reStr)
    print(re.match(patternStr, reStr))
    sub = pattern.sub(" http://img.toolcards.cn/"+re.match(patternStr, reStr).group(1), reStr)
    print(sub)
