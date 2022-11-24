import requests
from Logging import Logger
from web_scrappers import AmazonJobPostingScrapper


# TODO: vpn()
# TODO: get_more_links() function in AmazonJobPostingScrapper
logger = Logger()
getter = AmazonJobPostingScrapper(logger)


links = ["https://www.amazon.jobs/en/jobs/2155085/penetration-testing-engineer",\
         "https://www.amazon.jobs/en/jobs/1164273/penetration-testing-engineer",\
         "https://www.amazon.jobs/en/jobs/2155085/penetration-testing-engineer",\
         "https://www.amazon.jobs/en/jobs/2004839/offensive-security-engineer-aws",\
         "https://www.amazon.jobs/en/jobs/2004839/offensive-security-engineer-aws",\
         "https://www.amazon.jobs/en/jobs/1932828/mobile-security-engineer-offensive-security-penetration-testing"]
new_links = []
while True:
    if len(links) > 1500:
        links = links[len(links)//2:]
    failed_requests = 0
    for link in links:
        src = requests.get(link)
        attempts = 0
        for i in range(69):
            cache = requests.get(link)
            if not cache:
                attempts += 1
            if i - (attempts-1) > 10:
                vpn()
        for new_link in AmazonJobPostingScrapper.get_more_links(src):
            new_links.append(new_link)
    if not new_links:
        break
    links = new_links

