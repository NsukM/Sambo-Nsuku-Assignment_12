from services.user_service import UserService
from services.fitness_profile_service import FitnessProfileService

class AnalyticsReportService:
    def _init_(self):
        self.user_service = UserService()
        self.profile_service = FitnessProfileService()

    def generate_summary(self):
        users = self.user_service.get_all_users()
        profiles = self.profile_service.get_all_profiles()
        return {
            "total_users": len(users),
            "average_weight": sum(p.weight for p in profiles) / len(profiles) if profiles else 0,
            "user_goals": [u.goal for u in users]
        }

