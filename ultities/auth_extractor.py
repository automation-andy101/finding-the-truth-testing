import base64

# The Base64 encoded string from the Authorization header
encoded_str = "NTc0MTk3OTg5NGFkMDpiM013YkhwTFNEVndRMUY0WkVJNVFtOUlNVWhVVDBScVFYUXJhMG94VkVodVYxRlJhWHBxYlVKc1pqaHdUalJyY0dsa1dubHhObFZ1TW1VelVubDRLM1ZhZWpONE9XTmplVEYyZFdRclMwaGhkR3RwWkhCMGQwaGxSVkZZTlVKT1pETjFWbGQ0ZW1kWlF6UTk"

# Decode the Base64 string
decoded_bytes = base64.b64decode(encoded_str)
decoded_str = decoded_bytes.decode('utf-8')

# Split the decoded string to get username and password
username, password = decoded_str.split(":", 1)

print(f"Username: {username}")
print(f"Password: {password}")
