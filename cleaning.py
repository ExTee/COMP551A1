import re


file_in = open("test.xml", "rb")
file_out = open("test_cleaned.xml", "wb")


data = file_in.readlines();
new_data = [];


# Get rid of empty lines
for line in data:
    # Strip whitespace, should leave nothing if empty line was just "\n"
    if not line.strip():
        continue
    # We got something, save it
    else:
        #getting rid of weird characters
        line = re.sub('[\[\]_*~]','', line);
        line = re.sub('\n', '',line);

        #deleting removed posts
        line = re.sub('<utt.*removed.*<\/utt>', '', line);
        #deleting urls
        line = re.sub('\(http.*\)', '',line);
        line = re.sub('(https?:\/\/(www\.)?[-a-zA-Z0-9@:%._\+~#=]{2,256}\.[a-z]{2,6}\b([-a-zA-Z0-9@:%_\+.~#?&//=]*))', '', line);

        #gt,lt etc.
        line = re.sub('#*&.*;', '',line);
        #"ce sujet genere par .."
        line = re.sub('\^\(.*\) \^\w*.', '',line);
        line = re.sub('\^\(.*\)*\^', '', line);

        #skip a like whenever theres a new <s>
        line = re.sub('<s>', '\n<s>',line);
        #skip a line whenever there's a new utt
        line = re.sub('<utt', '\n\t<utt',line);

        new_data.append(line)

#write to file

file_out.writelines(new_data);

# Print file sans empty lines 
print "done";


file_in.close();
file_out.close();
