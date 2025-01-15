# src/sdk/analytics.py

"""
Analytics Module
-----------------
This module provides functionality to analyze user behavior, challenge progress,
and overall platform performance for MetaEarth AI.
"""

class AnalyticsEngine:
    """
    A class to perform data analytics on user actions, challenges, and platform metrics.
    """

    def __init__(self):
        self.user_data = {}
        self.challenge_data = {}

    def log_user_action(self, user_id, action_type, points):
        """
        Logs user actions and updates their cumulative data.

        Args:
            user_id (str): The unique identifier of the user.
            action_type (str): The type of action (e.g., "recycling", "tree_planting").
            points (int): Points awarded for the action.

        Returns:
            dict: Updated user data.
        """
        if user_id not in self.user_data:
            self.user_data[user_id] = {"actions": {}, "total_points": 0}

        if action_type not in self.user_data[user_id]["actions"]:
            self.user_data[user_id]["actions"][action_type] = 0

        self.user_data[user_id]["actions"][action_type] += points
        self.user_data[user_id]["total_points"] += points

        print(f"[INFO] Logged action for user {user_id}: {action_type} (+{points} points)")
        return self.user_data[user_id]

    def log_challenge_progress(self, challenge_id, metric, value):
        """
        Logs progress for a specific challenge.

        Args:
            challenge_id (str): The unique identifier of the challenge.
            metric (str): The metric being tracked (e.g., "trees", "co2_reduction").
            value (int): The amount contributed to the metric.

        Returns:
            dict: Updated challenge data.
        """
        if challenge_id not in self.challenge_data:
            self.challenge_data[challenge_id] = {}

        if metric not in self.challenge_data[challenge_id]:
            self.challenge_data[challenge_id][metric] = 0

        self.challenge_data[challenge_id][metric] += value
        print(f"[INFO] Updated challenge {challenge_id}: {metric} (+{value})")
        return self.challenge_data[challenge_id]

    def generate_user_report(self, user_id):
        """
        Generates a report for a specific user.

        Args:
            user_id (str): The unique identifier of the user.

        Returns:
            dict: A report of the user's actions and achievements.
        """
        if user_id not in self.user_data:
            print(f"[ERROR] No data found for user {user_id}")
            return None

        user_report = self.user_data[user_id]
        print(f"[INFO] Generated user report for {user_id}: {user_report}")
        return user_report

    def generate_challenge_report(self, challenge_id):
        """
        Generates a progress report for a specific challenge.

        Args:
            challenge_id (str): The unique identifier of the challenge.

        Returns:
            dict: A report of the challenge's progress.
        """
        if challenge_id not in self.challenge_data:
            print(f"[ERROR] No data found for challenge {challenge_id}")
            return None

        challenge_report = self.challenge_data[challenge_id]
        print(f"[INFO] Generated challenge report for {challenge_id}: {challenge_report}")
        return challenge_report

# Example usage
if __name__ == "__main__":
    analytics = AnalyticsEngine()

    # Log user actions
    analytics.log_user_action("user123", "tree_planting", 50)
    analytics.log_user_action("user123", "recycling", 20)
    analytics.log_user_action("user456", "tree_planting", 30)

    # Log challenge progress
    analytics.log_challenge_progress("challenge1", "trees", 100)
    analytics.log_challenge_progress("challenge1", "co2_reduction", 50)

    # Generate reports
    print(analytics.generate_user_report("user123"))
    print(analytics.generate_challenge_report("challenge1"))
