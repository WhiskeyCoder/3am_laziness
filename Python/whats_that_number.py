import itertools
import requests

all_combinations = list(itertools.product(range(10), repeat=4))
all_combinations_as_strings = [''.join(map(str, combination)) for combination in all_combinations]
all_combinations_as_strings_with_wild_card = ['7175' + combination + '1924' for combination in all_combinations_as_strings]
with open('phone_numbers.txt', 'w') as f:
    for item in all_combinations_as_strings_with_wild_card:
        f.write("%s \n" % item)
with open('phone_numbers.txt', 'r') as f:
    phone_numbers = f.readlines()
    access_key = 'API KEY FOR NUMBER VERIFICATION ITS FREE'
    for phone_number in phone_numbers:
        headers = {
            'apikey': access_key,
        }
        params = {
            'number': phone_number,
        }
        response = requests.get('https://api.apilayer.com/number_verification/validate', params=params, headers=headers)
        if response.status_code == 200:
            answer = response.json()
            if "valid" in answer and answer["valid"] == True:
                print(phone_number, 'is valid')
                # Write the valid phone number to a txt file
                with open('valid_phone_numbers.txt', 'a') as f:
                    f.write("%s \n" % phone_number)
            else:
                print(phone_number, 'is not valid')
        else:
            print('Failed to get a response from the server')
