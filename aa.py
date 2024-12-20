import asyncio

# Dummy User class for demonstration purposes
class User:
    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password

    async def save_to_db(self):
        # Simulate an asynchronous save operation
        await asyncio.sleep(0.1)  # Simulates database save time

async def create_and_save_user(name, email):
    # This function creates a user and saves it to the database
    user = User(name, email, 'default_password')
    await user.save_to_db()
    return user

async def user_count(loop, names, emails):
    # This will store all the user creation tasks
    tasks = []
    
    # Iterate over names and emails, creating tasks to handle each user
    for name, email in zip(names, emails):
        task = loop.create_task(create_and_save_user(name, email))
        tasks.append(task)
    
    # Await on all tasks to complete
    await asyncio.gather(*tasks)

    # Return the number of users, which is the length of the names list
    return len(names)

# Example usage:
if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    names = ["Alice", "Bob", "Charlie"]
    emails = ["alice@example.com", "bob@example.com", "charlie@example.com"]
    user_count_result = loop.run_until_complete(user_count(loop, names, emails))
    print(f"Total users created: {user_count_result}")