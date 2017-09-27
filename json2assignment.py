import xml.etree.ElementTree as etree
import json
from copy import deepcopy
from itertools import count


def _traverse_comments(replies, root, uids, count_iter):
    """Helper function that traverses the comments tree"""
    convs = []
    for user, reply in replies.items():
        if user not in uids:
            uids[user] = next(count_iter)
        reply = reply[0]
        new_root = deepcopy(root)
        utt = etree.Element("utt")
        utt.attrib["uid"] = str(uids[user])
        utt.text = reply["Body"]
        new_root.append(utt)
        if reply["Replies"]:
            convs.extend(_traverse_comments(
                reply["Replies"], new_root, uids, count_iter))
        else:
            convs.append(new_root)
    return convs


def convert(filename):
    """
    Takes a filename and returns a list ElementTree formatted to
    assignment specifications
    """
    with open(filename, "r") as file:
        data = json.load(file)

    # Extract data
    # Seed the first utterance
    count_iter = count(start=1)
    uids = {}
    root = etree.Element("s")
    utt = etree.Element("utt")
    root.attrib["thread"] = filename
    utt.attrib["uid"] = "1"
    utt.text = data["selftext"]
    uids[data["author"]] = next(count_iter)
    root.append(utt)

    return _traverse_comments(data["comments"], root, uids, count_iter)


def etree2xml(tree_or_element, file):
    """Write the xml of a tree or element to a file"""
    if type(tree_or_element) == etree.Element:
        tree = etree.ElementTree(tree_or_element)
    else:
        tree = tree_or_element
    assert isinstance(tree, etree.ElementTree)
    tree.write(file, encoding='utf8', method='xml')
