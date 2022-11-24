from Logging import Logger
from web_scrappers import AmazonJobPostingScrapper


links = ["https://www.amazon.jobs/en/jobs/2155085/penetration-testing-engineer",\
         "https://www.amazon.jobs/en/jobs/1164273/penetration-testing-engineer",\
         "https://www.amazon.jobs/en/jobs/2155085/penetration-testing-engineer",\
         "https://www.amazon.jobs/en/jobs/2004839/offensive-security-engineer-aws",\
         "https://www.amazon.jobs/en/jobs/2004839/offensive-security-engineer-aws",\
         "https://www.amazon.jobs/en/jobs/1932828/mobile-security-engineer-offensive-security-penetration-testing"]


# TODO: Complete get_more_links(), which would allow this to become a botnet.
# TODO: Not make this a botnet because doing so would be morally ambiguous.


dd = {"links": links}


if __name__ == "__main__":
    log = Logger()
    log.log("\n----Beginning Process----\n")
    oi = AmazonJobPostingScrapper(log)
    json = oi.do(dd)

