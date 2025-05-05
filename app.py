from flask import Flask, render_template, request
import random

app = Flask(__name__)

def generate_name_phone(name, phone, count=2000):
    passwords = set()
    name_variants = [name.lower(), name.capitalize(), name.upper()]
    phone_parts = [phone[:4], phone[-4:], phone[1:5]]

    patterns = [
        lambda n, p: f"{n}@{p}",
        lambda n, p: f"{p}@{n}",
        lambda n, p: f"{n}{p}@",
        lambda n, p: f"{p}{n}@",
        lambda n, p: f"{n[:3]}@{p}",
        lambda n, p: f"{n}@{random.randint(10,99)}{p[-2:]}"
    ]

    while len(passwords) < count:
        n = random.choice(name_variants)
        p = random.choice(phone_parts)
        pattern = random.choice(patterns)(n, p)
        passwords.add(pattern)

    return list(passwords)

def generate_name_birthyear(name, year, count=1000):
    passwords = set()
    name_variants = [name.lower(), name.capitalize(), name.upper()]
    year_parts = [year, year[-2:], f"@{year}", f"{year}@"]

    while len(passwords) < count:
        n = random.choice(name_variants)
        y = random.choice(year_parts)
        pattern = random.choice([
            f"{n}{y}",
            f"{y}{n}",
            f"{n}@{y}",
            f"{n[:3]}{y}",
            f"{n}@{random.randint(10,99)}{y[-2:]}"
        ])
        passwords.add(pattern)

    return list(passwords)

@app.route('/', methods=['GET', 'POST'])
def index():
    passwords = []
    if request.method == 'POST':
        name = request.form.get('name', '').strip()
        phone = request.form.get('phone', '').strip()
        birthyear = request.form.get('birthyear', '').strip()

        if name and phone:
            passwords += generate_name_phone(name, phone)
        if name and birthyear:
            passwords += generate_name_birthyear(name, birthyear)
        if not passwords and (name or phone or birthyear):
            passwords = [f"{name}@1234", f"user@{phone[:4] if phone else '0000'}"]

    return render_template('index.html', passwords=passwords)

if __name__ == '__main__':
    app.run(debug=True)



