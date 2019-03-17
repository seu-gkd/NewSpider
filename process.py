def pro1():
    test = set()
    with open('test.txt','r',encoding='utf-8') as f:
        while True:
            lines = f.readline()
            if lines:
                try:
                    test.add(lines.split(',')[1])
                except:
                    print(lines)
            else:
                break

def pro2():
    with open('temp.txt','r',encoding='utf-8') as f:
        targets = f.readlines()

    with open('city_url.txt', 'r', encoding='utf-8') as f:
        urls = f.readlines()

    with open('final_url.txt','a+',encoding='utf-8') as f:
        for url in urls:
            if url.split(',')[1] in targets:
                f.write(url)
if __name__ == '__main__':
    pro2()
