"""Lab 3: Regexes and reformatting."""

# Dominique Mendes

#######################################
# Instructions:
#
# The contact information below is not properly formatted.  Use regular expressions and Python code to reorganize the
# contact information into this format:
#
# Last name, First name, Middle Initial
# Location
# (xxx) xxx-xxxx
#
# Use regular expressions to decompose the data as much as possible and Python to reformat it.
#
# Print the reformatted information to show that it has been correctly reorganized.
#
# Extra Credit: Produce the reformatted contact info sorted programmatically by last name, ascending.
#
#######################################
import re

names= []

contacts = ["Kiayada D. Levy,(570)7924192,Sint-Laureins-Berchem",
            "Gretchen F. Manning,(1-656)-285-0869,Spoleto",
            "Ashton Richards,(974) 843-9297,Annapolis Royal",
            "Demetrius J. Ferguson,1-906-206-4323,Rea",
            "Blair Nelson,1-121-171-3665,Bertiolo",
            "Cynthia J. Farley,632 691 2180,Moen",
            "Nayda M. Lloyd,1-864-250-6977,Sarrev",
            "Miranda Edith Sexton,1-597-689-8316,Shipshaw",
            "Fulton Mays,(725)789-9517,Pierrefonds",
            "Shea Kim,1-697-854-4139,Bihain",
            "Emma-Mae Winters,1-137-630-5601,Gulfport",
            "Inez W. Depew,1-833-470-5664,Johnstone",
            "Darrel F. Key,1-878-918-2161,Olympia",
            "Tobias L. Stephens,1-119-939-6704,Unnao",
            "Elmo Pate,1-869-333-7341,Griesheim"]

s="\n"
s=s.join(contacts)
#print(s)

pattern= re.compile(r'^(\w+(\-\w+)?)(\s)([A-Z]\.\s)*(\w+)(\s\w+)?\,((\(|1\-|\(1\-)*\d{3}(\)(\s)?|-|\s|\)\-)?\d{3}\-*\s?\d{4})\,(\w+)(\-\w+\-\w+)?(\s\w+$)?', re.MULTILINE)
m=pattern.findall(s)

for match in m:
    print(match[4]+", "+ match[0]+", "+match[3])
    print(match[10],match[11])
    print(match[6])
    print("\n")
    #for item in match:
        #print(item)

