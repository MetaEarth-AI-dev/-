# src/ai_agents/tracking_agent.py

"""
Tracking Agent Module
---------------------
This module tracks user environmental actions in real-time and records the data
for analysis and reward calculations.
"""

import datetime

class TrackingAgent:
    """
    A class to track and log user actions related to sustainability.
    """

    def __init__(self):
        self.action_log = []

    def track_action(self, user_id, action_type, details):
        """
        Tracks a user's environmental action and logs it.

        Args:
            user_id (str): The unique identifier of the user.
            action_type (str): The type of action (e.g., "recycling", "tree_planting").
            details (dict): Additional details about the action (e.g., quantity, location).

        Returns:
            dict: A summary of the tracked action.
        """
        action = {
            "user_id": user_id,
            "action_type": action_type,
            "details": details,
            "timestamp": datetime.datetime.utcnow().isoformat()
        }
        self.action_log.append(action)
        print(f"[INFO] Action tracked: {action}")
        return action

    def get_user_actions(self, user_id):
        """
        Retrieves all tracked actions for a specific user.

        Args:
            user_id (str): The unique identifier of the user.

        Returns:
            list: A list of actions performed by the user.
        """
        user_actions = [action for action in self.action_log if action["user_id"] == user_id]
        print(f"[INFO] Retrieved {len(user_actions)} actions for user {user_id}")
        return user_actions

    def get_all_actions(self):
        """
        Retrieves all tracked actions.

        Returns:
            list: A list of all logged actions.
        """
        print(f"[INFO] Retrieved total {len(self.action_log)} actions.")
        return self.action_log

# Example usage
if __name__ == "__main__":
    agent = TrackingAgent()

    # Simulate tracking actions
    agent.track_action("user123", "tree_planting", {"quantity": 5, "location": "Park A"})
    agent.track_action("user456", "recycling", {"material": "plastic", "weight_kg": 2.5})

    # Retrieve actions for a specific user
    print(agent.get_user_actions("user123"))

    # Retrieve all actions
    print(agent.get_all_actions())
