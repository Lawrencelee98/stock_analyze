import jieba
import pandas as pd

string = '【这类基金发行创9年新高 今年最高暴赚超59%！投向34个市场】外围市场令人眼热，QDII基金发行热度创下2012年7月份以来新高！据统计，今年以来，178只纳入统计的QDII基金中，有110只基金实现正收益，占比达61.8%，平均收益率为5.75%，跑赢同期股票型开放式基金与混合型开放式基金，以及沪深300指数。（券商中国）'

emo_dict = pd.read_csv('./emotion_dict.csv', encoding='utf-8')

print(emo_dict.shape)
# for index in range(0, emo_dict.shape[1]):
#     print(emo_dict.loc[index])