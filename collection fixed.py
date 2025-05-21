"""
Name: Mitansh
Date: 05/03/2024
Description: This program creates a dictionary of authors and their death years,
             then prints each entry in a formatted string showing when each author died.
"""

authors = {
    "Charles Dickens": "1870",
    "William Thackeray": "1863",
    "Anthony Trollope": "1882",
    "Gerard Manley Hopkins": "1889"
}

for author, date in authors.items():
    print("%s died in %s." % (author, date))