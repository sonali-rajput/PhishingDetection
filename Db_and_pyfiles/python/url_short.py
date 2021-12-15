# bitly=https://bit.ly/x+
# rebrandly=rebrand.ly/
# tinyUrl=https://tinyurl.com
# bl.inl=https://bl.ink
# short.io= short.io
# sniply=sniply 
# url shortened by zapier = ptanhi
# shortby=shortby 
lt = ["bit.ly","rebrand.ly","tinyurl.com","bl.ink","short.io"]
link = "https://bit.ly/ggcfgvj"
def isWordPresent(link, word):
    k = 0
    h = 0
    for i in range(len(link)-1):
        if (link[i] == word[k]):
            k += 1
            if k>h:
                h=k
            if h == len(word):
                return True
        else:
            k = 0
    if h == len(word):
        return True
    return False
for i in range(len(lt)):
    print(isWordPresent(link,lt[i]))
