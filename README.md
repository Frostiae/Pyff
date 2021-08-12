# Pyff

Pyff is a very small python wrapper for the [Flyff Project M API](https://flyff-api.sniegu.fr/).
As time goes on and the API gets more populated, this library will hopefully follow. 

Contributions and pull requests are welcome!
### Quick Start

```python
from pyff.flyff import Flyff

flyff = Flyff()
item_ids = [1, 3, 5, 52, 55, 61, 81]
items = flyff.get_items_by_ids(item_ids)
for item in items:
    print(item['name']['en'])
```