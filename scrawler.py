from lxml import html
import requests

hearder = {"user-ageent":'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36'}

def get_comment_url(url=''):
    # url = 'http://guba.eastmoney.com/default,99_2.html'
    root_url = 'http://guba.eastmoney.com'
    response = requests.get(url=url, headers=hearder)
    page_text = response.text
    etree = html.fromstring(page_text)
    news_list_raw = etree.xpath('//ul[@class="newlist"]/li')

    news_list = []
    for news in news_list_raw:
        news_list.append(news.xpath('./span/a[2]/@href')[0])

    print(news_list)
    return news_list


def get_comment(url=''):
    response = requests.get(url=url, headers=hearder)
    etree = html.fromstring(response.text)
    comments = etree.xpath('//div[@class="stockcodec .xeditor"]/text()')

    # print(response.text)
    # print(comments)
    return comments


def get_all_comment():
    fp = open('comments.txt','w',encoding='utf-8')
    comments = []
    for index in range(1, 3):
        url = 'http://guba.eastmoney.com/default,99_'+str(index)+'.html'
        url_list = get_comment_url(url)
        for url in url_list:
            comment = get_comment('http://guba.eastmoney.com'+url)
            comments.append(comment)
            print("index"+str(index)+" :")
            print(comment)
            fp.write(str(comment)+'\n')

    fp.close()


if __name__=='__main__':
    # get_comment_url()
    get_all_comment()
    # get_comment()

