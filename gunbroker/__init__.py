from bs4 import BeautifulSoup
from requests import Session


class GunBroker:
    def __init__(self):
        self.session = Session()
        self.session.headers.update({"User-Agent": "python-gunbroker (https://github.com/DACRepair/python-gunbroker)"})
        self.url = "https://www.gunbroker.com"

    def _params(self, search: str, page: int = 1) -> dict:
        params = {'Keywords': search, "PageSize": 96, "Sort": 13, "PageIndex": page}
        return params

    def _html(self, params) -> str:
        data = self.session.get(self.url + "/All/search", params=params)
        return data.text

    def _beautiful(self, html) -> BeautifulSoup:
        return BeautifulSoup(html, features="html.parser")

    def _get_page_count(self, search: str) -> int:
        try:
            soup = self._beautiful(self._html(self._params(search)))
            return int(soup.find_all("span", class_="page-count-display")[0].text)
        except:
            return 0

    def _parse_listing(self, listing) -> dict:
        seller = listing.find("div", class_="listing-seller").find_all("a")
        name = " ".join(str(listing.find("div", class_="listing-text").find("h4").find("a").text).split())
        desc = listing.find("div", class_="listing-text").find("p")
        if desc is not None:
            desc = " ".join(str(desc.find("a").text).split())
        else:
            desc = ""

        prices = listing.find("div", class_="listing-figures")
        starting_bid = prices.find("a", class_="current")
        if starting_bid is not None:
            starting_bid = float(str(starting_bid.text).replace(",", "").replace("$", ""))
        buy_now = prices.find("a", class_="buy-now")
        if buy_now is not None:
            buy_now = float(str(buy_now.text).replace(",", "").replace("$", ""))

        time_qty = listing.find("span", class_="time-left").text
        if "Qty:" in time_qty:
            qty = int(''.join(filter(lambda x: x.isdigit(), time_qty)))
            time_left = None
            bids = None
        else:
            qty = 1
            time_left, bids = str(time_qty).split("|")
            time_left = time_left.split()
            _time_left = 0
            for entry in time_left:
                val = ''.join(filter(lambda x: x.isdigit(), entry))
                if val.isdigit():
                    val = int(val)
                else:
                    val = 0
                if "s" in entry.lower():
                    _time_left += val
                if "m" in entry.lower():
                    _time_left += (val * 60)
                if "h" in entry.lower():
                    _time_left += (val * 3600)
                if "d" in entry.lower():
                    _time_left += (val * 86400)
            time_left = _time_left
            bids = int("".join(bids.strip("Bids").split()))

        data = {
            "id": int(listing.find("a", class_="was-visited").get("href").strip("/item/")),
            "name": name,
            "desc": desc,
            "image": listing.find("div", class_="listing-image").find("img").get('src'),
            "url": self.url + listing.find("a", class_="was-visited").get("href"),
            "seller": seller[0].text,
            "seller_rating": seller[1].text,
            "qty": qty,
            "buy_now": buy_now,
            "starting_bid": starting_bid,
            "bids": bids,
            "time_left": time_left
        }

        return data

    def search(self, search: str, limit: int = 0) -> list:
        results = []
        for page in range(1, self._get_page_count(search) + 1, 1):
            for listing in self._beautiful(self._html(self._params(search, page))).find_all("div", class_="listing"):
                results.append(self._parse_listing(listing))
                if len(results) >= limit != 0:
                    break
            if len(results) >= limit != 0:
                break
        return results
