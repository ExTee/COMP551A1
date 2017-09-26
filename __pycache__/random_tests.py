# -*- coding: utf-8 -*-
import re

sentence = '<utt uid="1">Ref http://www.reddit.com/r/AskReddit/comments/2m29u6/mostamericansoundingword/</utt><utt uid="2">Merde !</utt></s>';


reg = r"(?i)\b((?:[a-z][\w-]+:(?:/{1,3}|[a-z0-9%])|www\d{0,3}[.]|[a-z0-9.\-]+[.][a-z]{2,4}/)(?:[^\s()<>]+|\(([^\s()<>]+|(\([^\s()<>]+\)))*\))+(?:\(([^\s()<>]+|(\([^\s()<>]+\)))*\)|[^\s`!()\[\]{};:'\".,<>?«»“”‘’]))"

sentence = re.sub(reg, 'url',sentence);
print(sentence)