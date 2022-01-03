from gensim.summarization.summarizer import summarize
from konlpy.tag import Kkma

kkma = Kkma()
import sys
import os
import re
import tensorflow
import keras
from hanspell import spell_checker


def preprocessing(content):
    total_content = ''
    for idx in range(len(content)):
        r = content[idx]
        for sentence in kkma.sentences(r):
            sentence = re.sub('([a-zA-Z])', '', sentence)
            sentence = re.sub('[ㄱ-ㅎㅏ-ㅣ]+', '', sentence)
            sentence = re.sub('[-=+,#/\?:^$.@*\"※~&%ㆍ!』\\‘|\(\)\[\]\<\>`\'…》]', '', sentence)
            if len(sentence) == 0:
                continue
            sentence += '. '
            total_content += sentence
    return total_content


def summary_content(contents):
    sentence = []
    contents = [contents]
    for content in contents:
        processed = preprocessing([content])
        if len(processed.split(".")) < 5:
            continue
        summary = summarize(processed, word_count=35)
        summary = re.sub("\n", " ", summary)
        if len(summary) == 0:
            continue
        spelled_summary = spell_checker.check(summary)
        summary = spelled_summary.checked
        sentence.append(summary)
    return sentence[0]


def original_and_summary(original, summary):
    original = [original]
    originals = []
    summaries = []
    for key in summary:
        originals.append(original[key])
        summaries.append(summary[key])
    return originals, summaries
