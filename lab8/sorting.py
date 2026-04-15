def main():
    data = {}
    sort_list = []

    with open("items.txt", "r") as file:
        for line in file:
            line = line.strip()

            if not line:
                continue

            parts = line.split("|")

            item_id = parts[0]
            title = parts[1]
            genre = parts[2]
            pages = parts[3]

            data[item_id] = {
                "title": title,
                "genre": genre,
                "pages": pages
            }

            sort_list.append((title, item_id))

    sort_list.sort()

    for item in sort_list:
        title = item[0]
        item_id = item[1]
        info = data[item_id]

        print(f"ID: {item_id}, Title: {info['title']}, Genre: {info['genre']}, Pages: {info['pages']}")


if __name__ == "__main__":
    main()


