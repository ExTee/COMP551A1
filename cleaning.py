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
        line = re.sub('[_*]','', line);
        line = re.sub('\(http.*\)', '',line);
        new_data.append(line)

#write to file

file_out.writelines(new_data);

# Print file sans empty lines 
print "done";


file_in.close();
file_out.close();
