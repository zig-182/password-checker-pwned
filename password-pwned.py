import requests
import hashlib


#This collects data from the Have I Been Pwned API 
def collect_api_data(query_char):
   
  #Construct the API URL with the first 5 characters of the SHA-1 hash
  url = 'https://api.pwnedpasswords.com/range/' + query_char
  
  # Send a GET request to the HIBP API
  res = requests.get(url)
  
  # Check if the request was successful (HTTP status code 200)
  if res.status_code != 200:
    raise RuntimeError(f'Error fetching: {res.status_code}, check the api and try again')
  return res

def times_password_leaked(hashes, hash_to_check):
  
  # Parse the API response and check if the full SHA-1 hash exists
  # Return the count of occurrences if found, otherwise, return 0
  hashes = (line.split(':') for line in hashes.text.splitlines())
  for h, count in hashes:
    if h == hash_to_check:
      return count
  return 0

def pwned_check(password):
  
  # Generate the SHA-1 hash of the password
  sha1password = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
  
  # Extract the first 5 characters and the tail of the SHA-1 hash 
  first5_char, tail = sha1password[:5], sha1password[5:]
  
  # Query the HIBP API with the first 5 characters of the hash
  response = collect_api_data(first5_char)
  
  # Check if the full hash exists in the response and return the count
  return times_password_leaked(response, tail)

def main():
    while True:
        password = input("Enter the password you want to check: ").strip()
        
        #If the user leaves it blank, this acts as a prompt
        if not password:
            print("Please enter a valid password.")
            continue
        
        count = pwned_check(password)

        if count:
            print(f'Your password, "{password}", was found {count} time(s). Change your password as soon as possible to enhance your cybersecurity! If you would like advice on how to choose a suitable password, check out this article: https://support.microsoft.com/en-gb/windows/create-and-use-strong-passwords-c5cebb49-8c53-4f5e-2bc4-fe357ca048eb!')
        else:
            print(f'Good news! Your password, "{password}", was not found. To ensure that your password adheres to strong cybersecurity guidelines, check out this article here: https://support.microsoft.com/en-gb/windows/create-and-use-strong-passwords-c5cebb49-8c53-4f5e-2bc4-fe357ca048eb!')

        #Create a loop so that the user can decide when to leave the application or continue checking passwords
        while True:
            another_password = input("Do you want to check another password? (yes/no): ").lower()

            if another_password in {'yes', 'no'}:
                break
            else:
                print("Please enter 'yes' or 'no'.")

        if another_password != 'yes':
            print('Finished!')
            break


if __name__ == "__main__":
    main()
