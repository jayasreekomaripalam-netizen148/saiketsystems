from collections import Counter
import re


def analyze_file(filename):

    try:
        with open(filename, "r") as file:
            text = file.read()

        # Count lines
        lines = text.splitlines()
        line_count = len(lines)

        # Count characters
        character_count = len(text)

        # Extract words
        words = re.findall(r'\b\w+\b', text.lower())

        # Count words
        word_count = len(words)

        # Word frequency
        frequency = Counter(words)

        print("\n===== TEXT ANALYSIS REPORT =====")

        print(f"Total Words      : {word_count}")
        print(f"Total Lines      : {line_count}")
        print(f"Total Characters : {character_count}")

        print("\nMost Common Words:")

        for word, count in frequency.most_common(10):
            print(f"{word} : {count} times")


    except FileNotFoundError:
        print("Error: File not found.")

    except PermissionError:
        print("Error: Permission denied.")

    except Exception as e:
        print("Error occurred:", e)



def main():

    print("===== WORD COUNT TOOL =====")

    filename = input("Enter text file name: ")

    analyze_file(filename)


if __name__ == "__main__":
    main()