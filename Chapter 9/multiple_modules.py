from privileges_and_admin import Admin

my_admin = Admin('osborne', 'risaiah', 'osborne@example.com', 'password123')

print(my_admin.privileges_instance.show_privileges())