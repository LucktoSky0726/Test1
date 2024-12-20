import asyncio
import uuid

# models.py
class User:
    def __init__(self, name, email, password):
        self.id = uuid.uuid4()
        self.name = name
        self.email = email
        self.password = password # In a real app, hash the password

    async def create_blog(self, title, content, db):
        blog = Blog(self.id, title, content)
        db['blogs'][blog.id] = blog
        return blog

    async def delete_blog(self, blog_id, db):
        if blog_id in db['blogs'] and db['blogs'][blog_id].author_id == self.id:
            del db['blogs'][blog_id]
            return True
        return False


class Blog:
    def __init__(self, author_id, title, content):
        self.id = uuid.uuid4()
        self.author_id = author_id
        self.title = title
        self.content = content

class Comment:
    def __init__(self, user_id, blog_id, content):
        self.id = uuid.uuid4()
        self.user_id = user_id
        self.blog_id = blog_id
        self.content = content



async def main():
    db = {'users': {}, 'blogs': {}, 'comments': {}}  # Simulated database

    async def create_user(name, email, password):
        user = User(name, email, password)
        db['users'][user.id] = user
        return user

    async def search_blogs(keyword):
        results = []
        for blog in db['blogs'].values():
            if keyword.lower() in blog.title.lower() or keyword.lower() in blog.content.lower():
                results.append(blog)
        return results

    # Example usage
    user = await create_user("Alice", "alice@example.com", "password123")
    blog = await user.create_blog("First Blog", "This is my first blog post.", db)
    search_results = await search_blogs("first")
    print(f"Search results: {len(search_results)}") # Output: Search results: 1


if __name__ == "__main__":
    asyncio.run(main())