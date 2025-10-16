new_invitations = []

with open("Input/Names/invited_names.txt") as names:
    invitations = names.readlines()

for names in invitations:
    new_names = names.replace("\n", "")
    new_invitations.append(new_names)

with open("Input/Letters/starting_letter.txt") as data:
    content = data.read()

for invites in new_invitations:
    with open(f"Output/ReadyToSend/letter_for_{invites}.txt", mode="w") as letter:
        new_content = content.replace("[name]", invites)
        letter.write(new_content)