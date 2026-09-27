#Project - Contact book

contacts = [{'name': 'James Omondi', 'phone': '0700000001', 'skill': 'welding', 'city': 'Nairobi'},
           {'name': 'Sandra Waweru', 'phone': '0700000002', 'skill': 'tilling', 'city': 'Mombasa'},
           {'name': 'Patrick Njiru', 'phone': '07000000003', 'skill': 'phone repair', 'city': 'Kisumu'},
           {'name': 'Grace Achieng', 'phone': '07000000004', 'skill': 'copywriting', 'city': 'Mombasa'},
           {'name': 'Brian Kamau', 'phone': '0700000005', 'skill': 'upholstery', 'city': 'Nairobi'}]
print('Contact book:', contacts)

#Count number of contacts.
print()
print('Contacts stored:', len(contacts))

#Print each contact separetly.
print()
print('First contact:', contacts[0])
print('Second contact:', contacts[1])
print('Third contact:', contacts[2])
print('Fourth contact:', contacts[3])
print('Fifth contact:', contacts[4])


#loop the contacts through the list.
print()
print('======= CONTACT BOOK =======')
for i, contact in enumerate(contacts):
    print(f'\n{i+1}. {contact['name']}')
    print(f'phone: {contact['phone']}')
    print(f'skill: {contact['skill']}')
    print(f'city: {contact['city']}')


#Search for a contact
print()
search_name = 'Brian Kamau'
found = False

for search in contacts:
    if contact['name'] == search_name:
        print(f'Contact found:')
        print(f'Name: {contact['name']}')
        print(f'phone: {contact['phone']}')
        print(f'skill: {contact['skill']}')
        print(f'city: {contact['city']}')
        found = True
        break

if not found:
    print('No contact found with name:', search_name)

#Search by City.
print()
search_city = 'Nairobi'
print(f'Contacts in {search_city}:')
for contact in contacts:
    if contact['city'] == search_city:
        print(f'{contact['name']} | {contact['skill']} | {contact['phone']}')


search_city = 'Mombasa'
print()
print(f'Contacts in {search_city}') 
for contact in contacts:
    if contact['city'] == search_city:
        print(f'{contact['name']} | {contact['skill']} | {contact['phone']}')

#Adding new contact.
print()
print('Before:', len(contacts), 'contacts')

new_contact = {'name:' 'Kevin Mwangi', 'phone:' '0700000006', 'skill:' 'beekeeping', 'city:' 'Nakuru'}

contacts.append(new_contact)
print('After:', len(contacts), 'contacts')
print()
print('Updated contact:', contacts)
print()
print('Last contact:', contacts[-1])


#SUMMARY
print(f'\nTotal contacts: {len(contacts)}')