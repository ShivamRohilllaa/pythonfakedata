from faker import Faker
fake = Faker()
names = [fake.unique.first_name() for i in range(500)]
assert len(set(names)) == len(names)

print('Fake Names', names)