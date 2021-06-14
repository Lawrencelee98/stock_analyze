import tushare as ts
import pandas as pd
import jieba
from evaluate import EmotionDict

token = '89cb45f5ae2d86f0faaf64b6b757f2fb9b6d69ff728914af064f15d2'
emo_dic = EmotionDict()

def get_api(token):
    ts.set_token(token)
    pro = ts.pro_api()
    return pro


def emo_pol(content):
    word_list = []
    pos_words_pol = []
    neg_words_pol = []

    for word in jieba.cut(content, use_paddle=True):
        word_list.append(word)

    for word in word_list:
        emo = emo_dic.evaluate(word)
        if emo == None:
            pass
        else:
            if emo[3] == 1:
                pos_words_pol.append(emo[2])
            elif emo[3] == 2:
                neg_words_pol.append(emo[2])
            else:
                pass

    pos_num = sum(pos_words_pol)
    neg_num = sum(neg_words_pol)
    pos_count = len(pos_words_pol)
    neg_count = len(neg_words_pol)
    return tuple((pos_num, neg_num,pos_count,neg_count))




if __name__=='__main__':
   # 获取tushare api
   #  api = get_api(token)

    # df = api.news(src='eastmoney', start_date='2021-06-11 18:00:00', end_date='2021-06-12 18:00:00')
    # news_list = list(df['content'])

    # for news in news_list:
    #     words = jieba.lcut(news)
    #
    #     for word in words:
    #         emo = emo_dic.evaluate(word)
    #         print(emo)

    emotion = 0
    emotion_rate = 0
    # for news in news_list:
    #     rate = emo_pol(news)
    #     emotion += rate[0]-rate[1]
    #     print(rate[0], rate[1], emotion)
    # print('情感的极性为：', emotion)

    with open('./comments.txt','r',encoding='utf-8') as fp:
        lines = fp.readlines()
        for line in lines:
            rate = emo_pol(line)
            emotion_rate += rate[0] - rate[1]
            emotion = rate[2]-rate[3]
            print(line,' :', str(rate[0]), str(rate[1]), str(rate[2]),str(rate[3]) )


    print('情感极性为： ', emotion, emotion_rate)
