def main() -> None:
    name_of_the_file = input("Enter name of the file: ")
    with open(f"{name_of_the_file}.txt", "a") as saving_file:
        while True:
            new_line_of_file = input("Enter new line of content: ")
            if new_line_of_file != "stop":
                saving_file.write(f"{new_line_of_file}\n")
            else:
                break


if __name__ == "__main__":
    main()
