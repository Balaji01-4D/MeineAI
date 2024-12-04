import inquirer

# Define the question
question = [
    inquirer.Confirm(
        'confirm',
        message="Do you want to continue?",
        default=True  # Default value is Yes
    )
]

# Prompt the user
answer = inquirer.prompt(question)

# Check the response
if answer['confirm']:
    print("You chose Yes.")
else:
    print("You chose No.")
