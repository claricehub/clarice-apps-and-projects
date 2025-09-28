import csv
from appli.utils.generator import generate_name
from appli.utils.generator import generate_age
from appli.business import nameexists
from appli.business.backend import addname

def main():
    while True:
        name = generate_name()
        age = generate_age()

        if not nameexists(name):
            addname(name, age)
            print(f"Added name: {name, age}")

            # Save to CSV
            with open("pessoas.csv", mode="a", newline="") as file:
                writer = csv.writer(file)
                writer.writerow([name, age])
            break  # Exit the loop after saving
        else:
            print(f"Name {name} already exists. Generating a new name...")

# Call the function outside the definition
main()
