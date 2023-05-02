import sys

def count_lines(file_path):
    try:
        if not file_path.endswith(".py"):
            raise ValueError("Not a Python file")

        with open(file_path, "r") as f:
            lines = f.readlines()

        count = 0
        for line in lines:
            line = line.strip()
            if line == "" or line.startswith("#"):
                continue
            count += 1

        return count

    except FileNotFoundError:
        print("File does not exist")
        sys.exit(1)

    except ValueError as e:
        print(str(e))
        sys.exit(1)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Too few/many command-line arguments")
        sys.exit(1)

    file_path = sys.argv[1]
    print(count_lines(file_path))
