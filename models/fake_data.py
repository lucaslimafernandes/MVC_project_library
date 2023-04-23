from faker import Faker

faker = Faker()

#a = dir(faker)
#for i in a:
#    print(i)

#print(f'name: {faker.name()}')
#print(f'iana_id: {faker.iana_id()}')
#print(f'address: {faker.address()}')
#print(f'street_address: {faker.street_address()}')
#print(f'state: {faker.state()}')
#print(f'country: {faker.country()}')
#print(f'simple_profile: {faker.simple_profile()}')
#print(f'phone: {faker.phone_number()}')
#print(f'email: {faker.email()}')
#print(f'user_name: {faker.user_name()}')
#print(f'password: {faker.password()}')
#print(f'job: {faker.job()}')
#print(f'CC: {faker.credit_card_full()}')
#print(f'date: {faker.date()}')

def gerar_user():

    return {
        'name'  : faker.name(),
        'iana_id'   : faker.iana_id(),
        'address'   : faker.address(),
        'phone_number'  : faker.phone_number(),
        'email'     : faker.email(),
        'job'       : faker.job(),
        'date'      : faker.date()
    }


if __name__ == '__main__':

    data = gerar_user()
    print(data)