# src/sdk/gamification.py

"""
Gamification Module
--------------------
This module implements the core gamification logic for MetaEarth AI,
including scoring, leveling, and achievement systems.
"""

class GamificationEngine:
    """
    A class to manage gamification elements such as scoring, leveling, and achievements.
    """

    def __init__(self):
        self.user_data = {}

    def add_user(self, user_id):
        """
        Initializes gamification data for a new user.

        Args:
            user_id (str): The unique identifier of the user.
        """
        if user_id not in self.user_data:
            self.user_data[user_id] = {
                "score": 0,
                "level": 1,
                "achievements": []
            }
            print(f"[INFO] User {user_id} added to gamification system.")

    def update_score(self, user_id, points):
        """
        Updates the user's score and checks for level-up.

        Args:
            user_id (str): The unique identifier of the user.
            points (int): The number of points to add to the user's score.

        Returns:
            dict: Updated user data including score and level.
        """
        if user_id not in self.user_data:
            print(f"[WARNING] User {user_id} not found. Adding user to system.")
            self.add_user(user_id)

        self.user_data[user_id]["score"] += points
        print(f"[INFO] User {user_id} score updated to {self.user_data[user_id]['score']}.")

        # Check for level-up
        self.check_level_up(user_id)
        return self.user_data[user_id]

    def check_level_up(self, user_id):
        """
        Checks if a user qualifies for a level-up based on their score.

        Args:
            user_id (str): The unique identifier of the user.
        """
        score = self.user_data[user_id]["score"]
        level = self.user_data[user_id]["level"]

        # Define a simple level-up logic (e.g., 100 points per level)
        required_score = level * 100
        while score >= required_score:
            self.user_data[user_id]["level"] += 1
            level = self.user_data[user_id]["level"]
            required_score = level * 100
            print(f"[INFO] User {user_id} leveled up to {level}.")

    def add_achievement(self, user_id, achievement_name):
        """
        Adds an achievement to the user's profile.

        Args:
            user_id (str): The unique identifier of the user.
            achievement_name (str): The name of the achievement.

        Returns:
            list: Updated list of achievements for the user.
        """
        if user_id not in self.user_data:
            print(f"[WARNING] User {user_id} not found. Adding user to system.")
            self.add_user(user_id)

        self.user_data[user_id]["achievements"].append(achievement_name)
        print(f"[INFO] User {user_id} earned achievement: {achievement_name}.")
        return self.user_data[user_id]["achievements"]

    def get_user_data(self, user_id):
        """
        Retrieves gamification data for a specific user.

        Args:
            user_id (str): The unique identifier of the user.

        Returns:
            dict: Gamification data for the user, including score, level, and achievements.
        """
        return self.user_data.get(user_id, f"[ERROR] User {user_id} not found.")

# Example usage
if __name__ == "__main__":
    engine = GamificationEngine()

    # Add users
    engine.add_user("user123")
    engine.add_user("user456")

    # Update scores and check level-ups
    engine.update_score("user123", 120)
    engine.update_score("user456", 80)
    engine.update_score("user123", 100)

    # Add achievements
    engine.add_achievement("user123", "First 100 Points")
    engine.add_achievement("user456", "Starter Badge")

    # Retrieve user data
    print(engine.get_user_data("user123"))
    print(engine.get_user_data("user456"))
