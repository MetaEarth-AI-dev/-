# src/ai_agents/reward_agent.py

"""
Reward Agent Module
---------------------
This module calculates and distributes $METAERTH token rewards based on
user actions and their environmental impact.
"""

class RewardAgent:
    """
    A class to calculate and distribute token rewards for sustainability actions.
    """

    def __init__(self, token_rate=1.0):
        """
        Initializes the Reward Agent with a default token rate.

        Args:
            token_rate (float): The base rate of tokens awarded per unit of impact.
        """
        self.token_rate = token_rate

    def calculate_rewards(self, action_type, details):
        """
        Calculates the token rewards for a given action.

        Args:
            action_type (str): The type of action (e.g., "recycling", "tree_planting").
            details (dict): Additional details about the action (e.g., quantity, weight).

        Returns:
            float: The calculated reward in $METAERTH tokens.
        """
        base_reward = 0

        if action_type == "tree_planting":
            base_reward = details.get("quantity", 0) * self.token_rate
        elif action_type == "recycling":
            base_reward = details.get("weight_kg", 0) * self.token_rate
        elif action_type == "energy_saving":
            base_reward = details.get("energy_kwh", 0) * self.token_rate
        else:
            print(f"[WARNING] Unknown action type: {action_type}")

        print(f"[INFO] Calculated reward: {base_reward} tokens for action: {action_type}")
        return base_reward

    def distribute_rewards(self, user_id, reward_amount):
        """
        Simulates the distribution of tokens to a user.

        Args:
            user_id (str): The unique identifier of the user.
            reward_amount (float): The amount of $METAERTH tokens to distribute.

        Returns:
            dict: A summary of the distribution.
        """
        # In a real implementation, this would interact with a blockchain to transfer tokens.
        distribution = {
            "user_id": user_id,
            "reward_amount": reward_amount,
            "status": "success"
        }
        print(f"[INFO] Distributed {reward_amount} tokens to user {user_id}")
        return distribution

# Example usage
if __name__ == "__main__":
    agent = RewardAgent(token_rate=1.5)

    # Simulate calculating rewards
    action = {"quantity": 10}  # Planting 10 trees
    reward = agent.calculate_rewards("tree_planting", action)

    # Simulate distributing rewards
    agent.distribute_rewards("user123", reward)
