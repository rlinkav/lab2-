url:str=input("url:")
result =url.count("--")
while ("--" in url):
    url=url.replace("--","-",1)
    print(url)
    print(result)