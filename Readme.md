[![Python Versions](https://img.shields.io/pypi/pyversions/yt2mp3.svg)](https://pypi.python.org/pypi/yt2mp3/)
[![MIT License](https://img.shields.io/apm/l/atomic-design-ui.svg?)](https://github.com/tterb/atomic-design-ui/blob/master/LICENSEs)

# faker-rainbow-collection

## Description

Here you can find a number of providers for the [Faker](https://faker.readthedocs.io/en/stable/index.html) data generator.

## Installation

`python setup.py install`

or

`pip install -e .`

or

`pip install promethor`

## How to use

```
from faker import Faker
from faker_rainbow_collection.providers import FlowerProvider

fake = Faker()
fake.add_provider(FlowerProvider)
print(fake.flower())
```

More examples in the [examples](https://github.com/FromZeus/faker-rainbow-collection/tree/main/faker_rainbow_collection/examples) directory.
