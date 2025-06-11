#Ask user for a file name
#if file exist
#   open it
#   Write its content to the terminal
#else
#   Create a new file
#If file cannot be opened
#   print error
#Loop
#   Get user input
#   if input == 'SAVE'
#   break
#Write all the user input into the file

import os


def main():
    filename = input('Enter the file name to open or create: ').strip()
    try:
        if os.path.exists(filename):
            with open(filename, 'r', encoding='utf-8') as file:
                content = file.read()
                print(content)
        else:
            with open(filename, 'w', encoding='utf-8') as file:
                pass

    except OSError:
        print('File not found')
        return

    print('\nEnter your text and type (SAVE) on a new line to save and exit the file.')

    content = []
    while True:
        input_text = input()
        if input_text == "SAVE":
            break
        content.append(input_text)

    try:
        with open(filename, 'w', encoding='utf-8') as file:
            file.write("\n".join(content))
            print(f"{filename} saved")
    except OSError:
        print(f"{filename} could not be saved")




if __name__ == "__main__":
    main()
