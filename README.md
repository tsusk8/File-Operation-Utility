# File Operation Utility

This Python script provides a command-line utility for performing various operations on files. It supports the following commands:

## Commands

1. **reverse**
   - Usage: `reverse <input_path> <output_path>`
   - Description: Reverses the contents of the input file and writes the reversed contents to the output file.

2. **copy**
   - Usage: `copy <input_path> <output_path>`
   - Description: Creates a copy of the input file at the specified output path.

3. **duplicate-contents**
   - Usage: `duplicate-contents <input_path> <count>`
   - Description: Duplicates the contents of the input file the specified number of times and writes the duplicated contents back to the input file.

4. **replace-string**
   - Usage: `replace-string <input_path> <needle> <new_string>`
   - Description: Replaces all occurrences of the `needle` string in the input file with the `new_string` and writes the modified contents back to the input file.

## Usage

To use the utility, run the script with the desired command and arguments:

```
python script.py <command> <arguments>
```

Replace `<command>` with one of the supported commands (`reverse`, `copy`, `duplicate-contents`, or `replace-string`), and provide the required arguments as specified for each command.

## Example

To reverse the contents of a file `input.txt` and write the reversed contents to `output.txt`, run:

```
python script.py reverse input.txt output.txt
```

This will create a new file `output.txt` with the reversed contents of `input.txt`.