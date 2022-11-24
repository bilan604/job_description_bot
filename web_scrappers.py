import re
import requests
from bs4 import BeautifulSoup


class AmazonJobPostingScrapper(object):

    def __init__(self, log):
        self.log = log
        if not self.log:
            raise "No Documentation!"

        self.dd_links = None
        self.json = {"jobs": []}

    def view(self, obj):
        if type(obj) == str:
            print(obj)
        elif type(obj) == list:
            for i in range(len(obj)):
                print("i: ", obj[i])
        return None

    def check(self, s):
        if "job" in s and "summary" in s:
            if "%" not in s:
                return True

    def get_description(self, lst):
        js_idx = 0
        js = None
        for i in range(len(lst)):
            s_checking = lst[i].lower()
            if self.check(s_checking):
                js_idx = i
                js = lst[i]
                break
        return js

    def filter_dds(self, dds):
        dds = [dd for dd in dds if dd[1] == "\""]
        dd_types = {}
        for dd in dds:
            s = dd.split(":")[0][1:]
            if s not in dd_types:
                dd_types[s] = dd
        return list(dd_types.values())

    def get_dds(self, ss):
        dds = []
        prev = ""
        s = ""
        for letter in ss:
            if letter == "{":
                if prev != "{":
                    prev = "{"
                    s = "{"
                else:
                    s = ""
                    prev = ""
            elif letter == "}":
                if prev == "{":
                    dds.append(s+"}")
                    s = ""
                    prev = ""
            else:
                if prev:
                    s += letter
        # filter non-json dictionaries
        dds = self.filter_dds(dds)
        return dds

    # TODO: Complete get_more_links(), which would allow this to become a botnet.
    # TODO: Not make this a botnet because doing so would be morally ambiguous.
    def get_more_links(self):
        pass

    def make_request(self, link):
        """
        This is the main function.
        :param link: string
        :return: job pls
        """
        response = requests.get(link)
        s = response.text
        self.log.log(s)

        soup = BeautifulSoup(response.content, 'html.parser')
        soup.prettify()

        ss = re.sub("br\/", "\(\n)", str(soup))
        dds = self.get_dds(ss)

        lst = s.split("=")
        js = self.get_description(lst)

        job = {"link": link, "summary": js, "args": dds}
        self.json["jobs"].append(job)

        self.get_more_links(s)
        return None

    def view(self):
        print("__________________\n", "FINAL OBJ:")
        for job in self.json["jobs"]:
            for arg in job:
                print(f"arg: {arg}\n    {job[arg]}")
        return

    def do(self, dd_links):
        self.dd_links = dd_links
        links = self.dd_links["links"]
        for link in links:
            self.make_request(link)
            self.dd_links.pop(link)
        return self.json

