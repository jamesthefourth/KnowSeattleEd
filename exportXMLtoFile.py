
import urllib.request
from requests import get  # to make GET request
#url = "http://api.greatschools.org/schools/nearby?key=rouznrbdxyk3bnblrcaxqaxx&state=WA&q=seattle&limit=5"
url = ("http://api.greatschools.org/search/schools?key=rouznrbdxyk3bnblrcaxqaxx&state=WA&q=Seattle&limit=10")
def download(url, file_name):
    # open in binary mode
    with open(file_name, "wb") as file:
        # get request
        response = get(url)
        # write to file
        file.write(response.content)

download(url, 'output.xml')
