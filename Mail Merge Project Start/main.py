import os

PLACEHOLDER = "[name]"

with open("C:\\Users\\dell\\Desktop\\projects\\Mail Merge Project Start\\Input\\Names\\invited_names.txt") as names_file:
    names = [name.strip() for name in names_file.readlines()]

with open("C:\\Users\\dell\\Desktop\\projects\\Mail Merge Project Start\\Input\\Letters\\starting_letter.txt") as letter_file:
    letter_contents = letter_file.read()

# Ensure the output directory exists
os.makedirs("./Output/ReadyToSend", exist_ok=True)

for name in names:
    stripped_name = name.strip()
    new_letter = letter_contents.replace(PLACEHOLDER, stripped_name)
    print(new_letter)
    with open(f"./Output/ReadyToSend/letter_for_{stripped_name}.docx", "w") as completed_letter:
        completed_letter.write(new_letter)
