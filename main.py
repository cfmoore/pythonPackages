from singleLL import SingleLL


def main():
    head = SingleLL(-1)
    temp = head
    for i in range(9):
        temp.add_node(i)
    head.print_nodes()
    head.remove_node(3)
    head.remove_node(-1)
    head.print_nodes()
    head = head.pop()
    head = head.pop()
    head = head.pop()
    head.print_nodes()


if __name__ == "__main__":
    main()
