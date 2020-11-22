import argparse
import csv

from faker import Faker
from faker_rainbow_collection.providers import (BookkeepingProvider,
                                                BookProvider, FlowerProvider,
                                                ShipmentProvider,
                                                SoldierProvider,
                                                SportsmanProvider,
                                                StudentProvider,
                                                TeacherProvider,
                                                VehicleProvider)

providers = [
    BookkeepingProvider, BookProvider, FlowerProvider, ShipmentProvider,
    SoldierProvider, SportsmanProvider, StudentProvider, TeacherProvider, VehicleProvider
]


def main():
    try:
        parser = argparse.ArgumentParser()
        parser.add_argument("count", type=int, default=100,
                            help="Number of entries to generate.")
        parser.add_argument("-l", "--locale", type=str, choices=['en_US', 'ru_TL'],
                            help="Locale to use.")
        args = parser.parse_args()

        fake = Faker()
        for p in providers:
            fake.add_provider(p)

        generators = [
            "flower", "vehicle", "book", "record",
            "teacher", "student", "sportsman", "soldier", "shipment"
        ]

        for g in generators:
            data = []
            for _ in range(args.count):
                data.append(getattr(fake, g)(locale=args.locale))

            with open(f"{g}.csv", 'w') as f:
                dict_writer = csv.DictWriter(f, data[0].keys())
                dict_writer.writeheader()
                dict_writer.writerows(data)
    except KeyboardInterrupt:
        print('\nThe process was interrupted by the user')
        raise SystemExit


if __name__ == "__main__":
    main()
