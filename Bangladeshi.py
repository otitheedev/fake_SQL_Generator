# Install this PIP module: pip install faker

from faker import Faker
import random

fake = Faker()

# Generate 100 random user records
user_records = []
for _ in range(100):
    
    # Generate a username that starts with '018', '017', or '015'
    username_prefix = random.choice(['018', '017', '015'])
    username = f"{username_prefix}{fake.random_number(digits=8)}"
   
    # Generate a names in Bangladeshi
    first_name_prefix = random.choice(['Md Shohan', 'Md Raihan', 'Sujon', 'Imran'])
    last_name_prefix = random.choice(['Hossain', 'Kabir', 'Hossain', 'Khan'])
    
   
   
    # Generate a fake email address
    email = fake.email()
    
    

    user_record = (
        'NULL',  # Assuming 'id' is an auto-incremented field
        '5',  # Assuming 'group_id' is optional
        f"'{username}'",  # Generate a username
        "'$2a$12$8WEJqIe/yOgbmn0EKTljmOnP54ZCaru0ftPiYmG8KOEE0lNUxwHSe'",  # Set all passwords to '123456'
        f"'{email}'",  # Assuming 'email' is optional
        f"'{first_name_prefix}'",  # Generate a random first name
        f"'{last_name_prefix}'",  # Generate a random last name
        'NULL',  # Assuming 'nid' is optional
        'NULL',  # Assuming 'nid_front_image' is optional
        'NULL',  # Assuming 'nid_back_image' is optional
        "'01878578504'",  # Assuming 'referer' is optional
        f"'{fake.date_of_birth()}'",  # Generate a random date of birth
        'NULL',  # Assuming 'address_1' is optional
        'NULL',  # Assuming 'state' is optional
        'NULL',  # Assuming 'city' is optional
        #f'{random.randint(0, 1)}',  # Generate a random value for 'is_ref' (0 or 1)
        '0',
        'NULL',  # Assuming 'gender' is optional
        'NULL',  # Assuming 'country' is optional
        'NULL',  # Assuming 'avatar' is optional
        '1',  # Set 'active' to 1
        'NULL',  # Assuming 'login_attempt' is set to 0 by default
        'NULL',  # Assuming 'last_login' is optional
        'CURRENT_TIMESTAMP',  # Set 'created_at' to the current timestamp
        'NULL',  # Assuming 'updated_at' is optional
        'NULL',  # Assuming 'reminder' is optional
        'NULL',  # Assuming 'activation' is optional
        'NULL',  # Assuming 'temp_pass' is optional
        'NULL',  # Assuming 'remember_token' is optional
        '0',  # Assuming 'device_token' is optional
        'NULL',  # Assuming 'last_activity' is optional
        'NULL'  # Assuming 'config' is optional
    )
    user_records.append(', '.join(map(str, user_record)))

# Create the SQL query
query = f"INSERT INTO `tb_users` (`id`, `group_id`, `username`, `password`, `email`, `first_name`, `last_name`, `nid`, `nid_front_image`, `nid_back_image`, `referer`, `birth_of_day`, `address_1`, `state`, `city`, `is_ref`, `gender`, `country`, `avatar`, `active`, `login_attempt`, `last_login`, `created_at`, `updated_at`, `reminder`, `activation`, `temp_pass`, `remember_token`, `device_token`, `last_activity`, `config`) VALUES ({'), ('.join(user_records)});"

print(query)

