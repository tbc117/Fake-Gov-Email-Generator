import random
import string

def generate_email():
    # List of common government domains
    government_domains = ['usa.gov', 'gov.uk', 'gov.au', 'gov.ca', 'gov.in']

    # Generate a random username
    username = ''.join(random.choices(string.ascii_lowercase, k=random.randint(5, 10)))

    # Choose a random government domain
    domain = random.choice(government_domains)

    # Construct the email address
    email = f"{username}@{domain}"

    return email

if __name__ == "__main__":
    # Generate and print a random fake government email address
    fake_email = generate_email()
    print("Fake Government Email:", fake_email)
    
    # Wait for user input to prevent the script from closing immediately
    input("Press Enter to exit...")
