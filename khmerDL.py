from __future__ import unicode_literals
import youtube_dl
import sys, re
from websites.phumiKhmer import phumiKhmerURLs

ACCEPTED_SITE_REGEXES = [
    ".*(phumikhmer9.com).*"
]

if len(sys.argv) == 1:
    print("khmerDL.py must be called with a URL argument. Exiting.")
    sys.exit()
else:
    # Scan all the parameters to make sure they're valid URLs
    for url in sys.argv[1:]:
        combined = "(" + ")|(".join(ACCEPTED_SITE_REGEXES) + ")"

        # If any one of the URLs don't match any of our URLs, quit
        if re.match(combined, url) == None:
            print("One of the URLs provided isn't currently supported. Exiting.")
            sys.exit()

# If you made it this far, all the URLs are valid
# So far it will be hard-coded to just download from PhumiKhmer.

# Put all the URLs to download in one list
urlsToDL = []
for url in sys.argv[1:]:
    urlsToDL += getPhumiKhmerURLs(url)

print("URLS to download" + str(urlsToDL))

# Now download them
ydl_opts = {}
with youtube_dl.YoutubeDL(ydl_opts) as ydl:
    for url in urlsToDL:
        ydl.download([url])
