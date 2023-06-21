contacts = []

def add_contact(name, email, phone):
    contact = {'name' : name, 'email' : email, 'phone' : phone}
    contacts.append(contact)

def search_contact(keyword):
    results = []
    for contact in contacts:
        if keyword.lower() in contact['name'].lower():
            results.append(contact)
    return results

# Example usage
add_contact("Kemp Milan", "kemp@example.com", "1234567890")
add_contact("Brian Smith", "brian@example.com", "9876543210")

search_results = search_contact("kemp")
for contact in search_results:
    print(contact)
