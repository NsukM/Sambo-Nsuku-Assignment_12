from repositories.inmemory.in_memory_fitness_profile_repository import InMemoryFitnessProfileRepository
from src.fitness_profile import FitnessProfile

class FitnessProfileService:
    def _init_(self):
        self.repo = InMemoryFitnessProfileRepository()

    def add_profile(self, age, weight, height, activity_level):
        profile = FitnessProfile(age, weight, height, activity_level)
        self.repo.save(profile)
        return profile

    def get_profile(self, age):
        return self.repo.find_by_id(age)

    def get_all_profiles(self):
        return self.repo.find_all()

    def delete_profile(self, age):
        self.repo.delete(age)

