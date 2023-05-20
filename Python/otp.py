import random

def generate_otp(phone_number):
    # Convert phone number to string and remove non-numeric characters
    phone_number = ''.join(filter(str.isdigit, str(phone_number)))
    
    # Generate random 6-digit OTP
    otp = ''.join(random.choices('0123456789', k=6))
    
    # Return OTP as string
    return otp

# Example usage
phone_number = input("Enter your phone number: ")
otp = generate_otp(phone_number)
print(f"Your OTP is: {otp}")
