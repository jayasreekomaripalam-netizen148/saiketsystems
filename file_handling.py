def read_file(filename):
    try:
        with open(filename, "r") as file:
            data = file.read()
            return data

    except FileNotFoundError:
        print("Error: File not found.")
        return None

    except Exception as e:
        print("Error reading file:", e)
        return None


def find_and_replace(filename, old_word, new_word):
    try:
        data = read_file(filename)

        if data is not None:
            if old_word in data:
                modified_data = data.replace(old_word, new_word)

                with open(filename, "w") as file:
                    file.write(modified_data)

                print("Word replaced successfully!")

            else:
                print("Word not found in the file.")

    except PermissionError:
        print("Error: Permission denied.")

    except Exception as e:
        print("Error updating file:", e)


def main():

    filename = "sample.txt"

    print("===== BASIC FILE HANDLING PROGRAM =====")

    data = read_file(filename)

    if data:
        print("\nOriginal File Content:")
        print(data)

    old_word = input("\nEnter word to replace: ")
    new_word = input("Enter new word: ")

    find_and_replace(filename, old_word, new_word)

    updated_data = read_file(filename)

    if updated_data:
        print("\nUpdated File Content:")
        print(updated_data)


if __name__ == "__main__":
    main()