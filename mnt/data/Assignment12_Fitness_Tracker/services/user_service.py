from repositories.inmemory.in_memory_user_repository import InMemoryUserRepository
from src.user import User

class UserService:
    def _init_(self):
        self.repo = InMemoryUserRepository()

    def create_user(self, user_id, name, email, password, goal):
        if self.repo.find_by_id(user_id):
            raise ValueError("User already exists")
        user = User(user_id, name, email, password, goal)
        self.repo.save(user)
        return user

    def get_user(self, user_id):
        return self.repo.find_by_id(user_id)

    def get_all_users(self):
        return self.repo.find_all()

    def update_user(self, user_id, name=None, email=None, goal=None):
        user = self.repo.find_by_id(user_id)
        if not user:
            raise ValueError("User not found")
        if name: user.name = name
        if email: user.email = email
        if goal: user.goal = goal
        self.repo.save(user)
        return user

    def delete_user(self, user_id):
        self.repo.delete(user_id)

