import scrapy
from scrapy.crawler import CrawlerProcess


class DocPythonSpider(scrapy.Spider):
    name = "docpython"
    start_urls = ["https://docs.python.org/3/library/index.html"]

    def parse(self, response):
        base_url = "https://docs.python.org/3/library/"
        for code in response.css("code.xref.py-mod"):
            module_name = code.css("span.pre::text").get()
            href = code.xpath("..").attrib.get("href", "")
            if module_name and href:
                yield {
                    "module": module_name,
                    "url": base_url + href if not href.startswith("http") else href,
                }


if __name__ == "__main__":
    process = CrawlerProcess(settings={
        "FEEDS": {"modules.json": {"format": "json", "overwrite": True}},
        "LOG_LEVEL": "WARNING",
    })
    process.crawl(DocPythonSpider)
    process.start()
    print("Résultats enregistrés dans modules.json")
