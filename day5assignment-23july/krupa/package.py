from password_generator.password import password
p=password()
password=p.generate_password(8)
print(password)