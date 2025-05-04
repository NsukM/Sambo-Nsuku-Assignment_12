from services.fitness_profile_service import FitnessProfileService

def test_add_profile():
    service = FitnessProfileService()
    profile = service.add_profile(25, 70, 175, "High")
    assert profile.age == 25
    assert service.get_profile(25).height == 175



