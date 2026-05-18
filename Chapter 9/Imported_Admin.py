from admin import *

my_admin = Admin('osborne', 'risaiah', 'osborne@example.com', 'password123')
# show privileges using the privileges_instance attribute
print(my_admin.privileges_instance.show_privileges())


 

