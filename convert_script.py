import os
import sys
import json
from json2assignment import convert, etree2xml
import xml.etree.ElementTree as etree
import traceback
import itertools


def get_convos_files(dir):
    basedir = dir
    convos = []
    print("Files in ", os.path.abspath(dir), ": ")
    subdirlist = []
    for item in os.listdir(dir):
        item = os.path.join(basedir, item)
        if os.path.isfile(item):
            if os.path.splitext(item)[1] == ".txt":
                try:
                    convos.extend(convert(item))
                except json.JSONDecodeError:
                    traceback.print_exc()
        else:
            subdirlist.append(item)
    for subdir in subdirlist:
        convos.extend(get_convos_files(subdir))
    return convos


convos = get_convos_files(sys.argv[1])
root = etree.Element("dialog")
for convo in convos:
    if len(convo.getchildren()) <= 1:
        continue
    if not convo.getchildren()[0].text:
        continue
    # Normalize the conversation uids
    uids = {}
    count = itertools.count(start=1)
    for utt in convo.getchildren():
        if utt.attrib["uid"] not in uids:
            uids[utt.attrib["uid"]] = str(next(count))
        utt.attrib["uid"] = uids[utt.attrib["uid"]]
        # utt.text = utt.text.replace("\n", "")
    root.append(convo)
print("Created xml file %s with %d entries." % (sys.argv[2],
                                                len(root.getchildren())))

with open(sys.argv[2], "wb") as file:
    etree2xml(root, file)
