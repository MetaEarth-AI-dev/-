# src/ai_agents/challenge_agent.py

"""
Challenge Agent Module
-----------------------
This module manages global and community challenges, tracks participation, and
calculates collective progress.
"""

import datetime

class ChallengeAgent:
    """
    A class to manage and track challenges for sustainability actions.
    """

    def __init__(self):
        self.challenges = {}
        self.participation = {}

    def create_challenge(self, challenge_id, name, goal, start_date, end_date):
        """
        Creates a new challenge.

        Args:
            challenge_id (str): Unique identifier for the challenge.
            name (str): The name of the challenge.
            goal (dict): The goal of the challenge (e.g., {"trees": 1000, "co2_reduction": 1000}).
            start_date (str): The start date of the challenge (ISO format).
            end_date (str): The end date of the challenge (ISO format).

        Returns:
            dict: A summary of the created challenge.
        """
        challenge = {
            "challenge_id": challenge_id,
            "name": name,
            "goal": goal,
            "start_date": start_date,
            "end_date": end_date,
            "progress": {key: 0 for key in goal.keys()}
        }
        self.challenges[challenge_id] = challenge
        print(f"[INFO] Created challenge: {challenge}")
        return challenge

    def participate_in_challenge(self, user_id, challenge_id, contribution):
        """
        Allows a user to participate in a challenge by contributing their actions.

        Args:
            user_id (str): Unique identifier for the user.
            challenge_id (str): Unique identifier for the challenge.
            contribution (dict): Contribution details (e.g., {"trees": 10}).

        Returns:
            dict: A summary of the updated challenge progress.
        """
        if challenge_id not in self.challenges:
            print(f"[ERROR] Challenge {challenge_id} does not exist.")
            return None

        if user_id not in self.participation:
            self.participation[user_id] = {}

        if challenge_id not in self.participation[user_id]:
            self.participation[user_id][challenge_id] = {}

        # Update user participation
        for key, value in contribution.items():
            self.participation[user_id][challenge_id][key] = (
                self.participation[user_id][challenge_id].get(key, 0) + value
            )

        # Update challenge progress
        for key, value in contribution.items():
            self.challenges[challenge_id]["progress"][key] += value

        print(f"[INFO] Updated challenge {challenge_id} with contribution {contribution} from user {user_id}")
        return self.challenges[challenge_id]

    def get_challenge_status(self, challenge_id):
        """
        Retrieves the current status of a challenge.

        Args:
            challenge_id (str): Unique identifier for the challenge.

        Returns:
            dict: The status of the challenge, including progress and remaining goal.
        """
        if challenge_id not in self.challenges:
            print(f"[ERROR] Challenge {challenge_id} does not exist.")
            return None

        challenge = self.challenges[challenge_id]
        remaining_goal = {
            key: max(0, challenge["goal"][key] - challenge["progress"][key])
            for key in challenge["goal"]
        }
        status = {
            "challenge_id": challenge_id,
            "name": challenge["name"],
            "progress": challenge["progress"],
            "remaining_goal": remaining_goal,
            "start_date": challenge["start_date"],
            "end_date": challenge["end_date"]
        }
        print(f"[INFO] Challenge status: {status}")
        return status

# Example usage
if __name__ == "__main__":
    agent = ChallengeAgent()

    # Create a challenge
    agent.create_challenge(
        "challenge1",
        "Plant 1 Million Trees",
        {"trees": 1000000},
        "2025-01-01",
        "2025-12-31"
    )

    # User participation
    agent.participate_in_challenge("user123", "challenge1", {"trees": 100})
    agent.participate_in_challenge("user456", "challenge1", {"trees": 50})

    # Get challenge status
    print(agent.get_challenge_status("challenge1"))
