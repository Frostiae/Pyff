from flyff import Flyff

flyff = Flyff()


def main():
    item_ids = [1, 3, 5, 52, 55, 61, 81]
    items = flyff.get_items_by_ids(item_ids)
    for item in items:
        print(item['name']['en'])


if __name__ == '__main__':
    main()
