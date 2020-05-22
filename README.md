# python-gunbroker
A Python library for scraping https://www.gunbroker.com

---

## Usage
> Note: This has not been posted to pypi, you will need to install it with 
>
>`pip install git+https://github.com/DACRepair/python-gunbroker.git`

After installing, it can be simply used with:
```python
from gunbroker import GunBroker

gbroker = GunBroker()
print(gbroker.search("K98", limit=2)) # if limit is unset, all results will be returned

# Result (List of Dicts):
# [{'bids': 0,
#   'buy_now': 800.00,
#   'desc': "",
#   'id': <ID>,
#   'image': '<Image URL>',
#   'name': 'K98 Mauser',
#   'qty': 1,
#   'seller': '<Seller>',
#   'seller_rating': 'A+(999)',
#   'starting_bid': 600.00,
#   'time_left': 316800,
#   'url': '<Item URL>'},
#  {'bids': 0,
#   'buy_now': 700.0,
#   'desc': None,
#   'id': <ID>,
#   'image': '<Image URL>',
#   'name': 'K98',
#   'qty': 1,
#   'seller': '<Seller>',
#   'seller_rating': 'A+(1)',
#   'starting_bid': 600.01,
#   'time_left': 759600,
#   'url': '<Item URL>'}]
```

### Response Breakdown:
| Key           | Value Type | Description                                                                    |
| ------------- | ---------- | -----------------------------------------------------------------------------  |
| bids          | `int`      | The number of bids currently on the item (Only if an auction, else its `None`) |
| buy_now       | `float`    | Buy now price                                                                  |
| desc          | `str`      | Auction Description                                                            |
| id            | `int`      | Auction ID                                                                     |
| image         | `str`      | Image thumbnail URL                                                            |
| name          | `str`      | The name of the auction listing                                                |
| qty           | `int`      | The quantity of the item being sold                                            |
| seller        | `str`      | The sellers name                                                               |
| seller_rating | `str`      | The rating of the seller (Shown as `<Rating>(# of ratings)` IE: `A+(100)`)     |
| starting_bid  | `float`    | Auction starting bid (Only if an auction, else its `None`)                     |
| time_left     | `int`      | Time left on auction in seconds (Only if an auction, else its `None`)          |
| url           | `str`      | URL to the individual item                                                     |

## Legal
I made this for personal use, any use of this library is done so at the users own risk. I am not licensing this as it
is not something I care to support. This is also not to be used for malicious purposes. If you use this,
please specify a user-agent like:
```python
from gunbroker import GunBroker
test = GunBroker(user_agent="My Bot (my email address)")
```
so that GunBroker can contact you for being an idiot.