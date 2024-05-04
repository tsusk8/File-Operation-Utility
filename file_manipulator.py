import shutil
import sys
import os

def validate_args(args):
    valid_commands = ["reverse", "copy", "duplicate-contents", "replace-string"]
    if len(args) < 2 or args[1] not in valid_commands:
        print("Invalid command. Valid commands are: reverse, copy, duplicate-contents, replace-string")
        return False

    if args[1] == "reverse" and len(args) != 4:
        print("Usage: reverse <input_path> <output_path>")
        return False

    if args[1] == "copy" and len(args) != 4:
        print("Usage: copy <input_path> <output_path>")
        return False

    if args[1] == "duplicate-contents" and len(args) != 4:
        print("Usage: duplicate-contents <input_path> <count>")
        return False
    elif args[1] == "duplicate-contents":
        try:
            int(args[3])
        except ValueError:
            print("Count should be an integer.")
            return False

    if args[1] == "replace-string" and len(args) != 5:
        print("Usage: replace-string <input_path> <needle> <new_string>")
        return False

    return True

def reverse_file(input_path, output_path):
    try:
        with open(input_path, 'r') as input_file, open(output_path, 'w') as output_file:
            lines = input_file.readlines()
            for line in reversed(lines):
                output_file.write(line)
        print(f"File reversed successfully. Output written to {output_path}")
    except FileNotFoundError:
        print(f"Error: {input_path} not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

def copy_file(input_path, output_path):
    try:
        shutil.copy(input_path, output_path)
        print(f"File copied successfully to {output_path}")
    except FileNotFoundError:
        print(f"Error: {input_path} not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

def duplicate_contents(input_path, count):
    try:
        with open(input_path, 'r+') as file:
            contents = file.read()
            file.seek(0)
            file.write(contents * count)
        print(f"File contents duplicated {count} times successfully.")
    except FileNotFoundError:
        print(f"Error: {input_path} not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

def replace_string(input_path, needle, new_string):
    try:
        with open(input_path, 'r') as input_file, open(f"{input_path}.tmp", 'w') as output_file:
            contents = input_file.read()
            output_file.write(contents.replace(needle, new_string))

        os.remove(input_path)
        os.rename(f"{input_path}.tmp", input_path)
        print(f"String '{needle}' replaced with '{new_string}' successfully.")
    except FileNotFoundError:
        print(f"Error: {input_path} not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

def main():
    if validate_args(sys.argv):
        command = sys.argv[1]
        if command == "reverse":
            reverse_file(sys.argv[2], sys.argv[3])
        elif command == "copy":
            copy_file(sys.argv[2], sys.argv[3])
        elif command == "duplicate-contents":
            duplicate_contents(sys.argv[2], int(sys.argv[3]))
        elif command == "replace-string":
            replace_string(sys.argv[2], sys.argv[3], sys.argv[4])

if __name__ == "__main__":
    main()