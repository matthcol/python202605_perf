import requests
from bs4 import BeautifulSoup


URL_BASE = "https://docs.python.org/3/library/"



class ScrappingError(Exception):
    pass

def scrap_types_from_module(module_name: str) -> list[str]:
    url = f"{URL_BASE}{module_name}.html"
    response = requests.get(url)
    if response.status_code != 200:
        raise ScrappingError(f"Error while accessing Python documentation of module: {module_name}")
    
    soup = BeautifulSoup(response.text, 'html.parser')

    section_type = soup.select_one("section#available-types")
    types = [t.text for t in section_type.select("span.descname span")]
    return types


if __name__ == '__main__':
    modules = [
        'datetime',
        # 'zoneinfo'
    ]
    for module in modules:
        types = scrap_types_from_module(module)
        print(module, types, sep=': ')
    