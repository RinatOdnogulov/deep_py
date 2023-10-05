from faker import Faker


def main():
    fake = Faker(locale="Ru_ru")
    for i in range(5):
        doc = {
            'name': fake.name(),
            'address': fake.address(),
            'company': fake.company(),
            'country': fake.country(),
            'text': fake.sentence()
        }
        print(doc)


if __name__ == "__main__":
    main()