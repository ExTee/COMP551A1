# -*- coding: utf-8 -*-
import re

sentence = '<utt uid="1">Ref http://www.reddit.com/r/AskReddit/comments/2m29u6/mostamericansoundingword/</utt><utt uid="2">Merde !</utt></s>';
sentence2= "d'armagnac.- 🎶 Allumez le feu🎶 pour faire flamb délicieux m poêle";

reg = r"(?i)\b((?:[a-z][\w-]+:(?:/{1,3}|[a-z0-9%])|www\d{0,3}[.]|[a-z0-9.\-]+[.][a-z]{2,4}/)(?:[^\s()<>]+|\(([^\s()<>]+|(\([^\s()<>]+\)))*\))+(?:\(([^\s()<>]+|(\([^\s()<>]+\)))*\)|[^\s`!()\[\]{};:'\".,<>?«»“”‘’]))"

#sentence = re.sub(reg, 'url',sentence);
#sentence2 = sentence2.decode('utf-8','ignore').encode("utf-8")

print(sentence2)