import sys
from websites.phumiKhmer import phumiKhmerURLs


ACCEPTED_SITE_REGEXES = [
    "(.*).(phumikhmer9\.com).*"
]

if len(sys.argv == 1):
    print("khmerDL.py must be called with a URL argument. Exiting.")
    sys.exit()
else:
    # Scan all the parameters to make sure they're valid URLs
    for url in sys.argv[1:]:
        combined = "(" + ")|(".join(ACCEPTED_SITE_REGEXES) + ")"

        # If any one of the URLs don't match any of our URLs, quit
        if !re.match(combined, url):
            print("One of the URLs provided isn't currently supported. Exiting.")
            sys.exit()

# If you made it this far, all the URLs are valid
# So far it will be hard-coded to just download from PhumiKhmer.
for url in sys.arg[1:]:
