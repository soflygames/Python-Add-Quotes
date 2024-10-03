# Step 1: Read the text file line by line
with open('output.txt', 'r') as file:
    lines = file.readlines()

# Step 2: Add single quotes around each line (strip to remove extra newlines if necessary)
quoted_lines = ["'" + line.strip() + "'" for line in lines]

# Step 3: Write the quoted lines back to a new file
with open('output.txt', 'w') as file:
    for quoted_line in quoted_lines:
        file.write(quoted_line + '\n')

print("Single quotes added to each line and saved in 'output.txt'.")
