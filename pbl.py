import random

def generate_passwords(name, birth_year, fav_person, mobile_no):
    base_patterns = [
        name + birth_year, name + "@" + birth_year, name + fav_person, name + "@" + fav_person,
        name + mobile_no, name + "@" + mobile_no, birth_year + fav_person, fav_person + "@" + birth_year,
        mobile_no + "@" + birth_year, fav_person + mobile_no, fav_person + "@" + mobile_no,
        name + "123", name + "!", name + "#"
    ]

    # Adding simple substitutions
    variations = set(base_patterns + [
        pattern.replace("a", "@").replace("o", "0").replace("e", "3") for pattern in base_patterns
    ])

    # Generate more random combinations
    all_passwords = list(variations)
    while len(all_passwords) < 1000:
        rand_pass = random.choice(base_patterns) + random.choice(["!", "@", "#", "123", "456"])
        all_passwords.append(rand_pass)

    return list(set(all_passwords))[:1000]  # Limit to 1000 unique passwords

# Get user inputs
name = input("Enter victim's first name: ").strip()
birth_year = input("Enter victim's birth year: ").strip()
fav_person = input("Enter victim's favorite person's name: ").strip()
mobile_no = input("Enter victim's mobile number: ").strip()

# Generate passwords
password_list = generate_passwords(name, birth_year, fav_person, mobile_no)

# Display first 20 passwords
print("\n🔹 Generated Passwords (Showing first 20):")
for password in password_list[:20]:
    print(password)

# Ask user if they want to save
save_choice = input("\nDo you want to save all 1000 passwords? (yes/no): ").strip().lower()

if save_choice == "yes":
    with open("password_list.txt", "w") as file:
        file.write("\n".join(password_list))
    print("✅ Password list saved to 'password_list.txt'")
else:
    print("❌ Passwords not saved.")
