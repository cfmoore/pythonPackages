from singleLL import SingleLL


def main():
    head = SingleLL(-1)
    temp = head
    for i in range(9):
        temp.add_node(i)
    head.print_nodes()
    print("This is an inline test: ")


if __name__ == "__main__":
    main()
