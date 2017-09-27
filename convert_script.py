import os
import sys
import json
from json2assignment import convert, etree2xml
import xml.etree.ElementTree as etree
import traceback
import itertools


convo_counts = {}


def get_convos_files(dir):
    global convo_counts
    basedir = dir
    convos = []
    print("Files in ", os.path.abspath(dir), ": ")
    subdirlist = []
    for item in os.listdir(dir):
        item = os.path.join(basedir, item)
        if os.path.isfile(item):
            if os.path.splitext(item)[1] == ".txt":
                try:
                    new_convos = convert(item)
                    if item not in convo_counts:
                        convo_counts[item] = len(new_convos)
                    convos.extend(new_convos)
                except json.JSONDecodeError:
                    traceback.print_exc()
        else:
            subdirlist.append(item)
    for subdir in subdirlist:
        convos.extend(get_convos_files(subdir))
    return convos


convos = get_convos_files(sys.argv[1])
thread_conv_counts = {}
word_count = 0
comment_count = 0
threads = set()
root = etree.Element("dialog")
number_speakers = 0
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
        # Also count the words
        word_count += len(utt.text.split(" "))
        comment_count += 1
        # utt.text = utt.text.replace("\n", "")
    # get number of speakers
    number_speakers += next(count) - 1
    root.append(convo)
    if convo.attrib["thread"] not in thread_conv_counts:
        thread_conv_counts[convo.attrib["thread"]] = 0
    threads.add(convo.attrib["thread"])
    thread_conv_counts[convo.attrib["thread"]] += 1
print("Created xml file %s with %d entries." % (sys.argv[2],
                                                len(root.getchildren())))
print("Number of unique threads in corpus: %d" % len(threads))
print("Average count of conversation per threads: %f" %
      float(sum(thread_conv_counts.values()) / float(len(thread_conv_counts))))
print("Average count of comments per conversation: %f" %
      float(sum(convo_counts.values()) / float(len(convo_counts))))
print("Average count of words per comment: %f" % (word_count / comment_count,))
print("Average count of speakers per conversation: %f" %
      (number_speakers / len(convo_counts),))

# with open(sys.argv[2], "wb") as file:
#     etree2xml(root, file)
