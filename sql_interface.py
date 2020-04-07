# will create the user return "success" or "failure"
def create_user(email, password):
    # interface with SQL here
    print("created: ", email, password)
    return "failure"

# returns "success" or "failure"
def login(email, password):
    print("login attempt: ", email, password)
    # interface with SQL here
    return "failure"

# returns contact info in a list
def contact_info(email):
    print("contacts ", email)
    # interface with SQL here
    return ["a", "b"]

# returns "success" or "failure"
def add_contact_info(email, value):
    print("add contact: ", email, value)
    # interface with SQL here
    return "failure"

# returns "success" or "failure"
def delete_contact_info(email, value):
    print("delete ", email, value)
    # interface with SQL here
    return "failure"

# returns "success" or "failure"
def update_contact_info(email, oldval, newval):
    print("update attempt: ", email, oldval, newval)
    # interface with SQL here
    return "failure"
