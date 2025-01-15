# src/sdk/leaderboard.py

"""
Leaderboard Module
-------------------
This module manages leaderboards for individual and community challenges,
tracking and displaying rankings based on user contributions.
"""

class Leaderboard:
    """
    A class to manage and display leaderboards for challenges.
    """

    def __init__(self):
        self.user_scores = {}
        self.challenge_scores = {}

    def update_user_score(self, user_id, challenge_id, points):
        """
        Updates the user's score for a specific challenge.

        Args:
            user_id (str): The unique identifier of the user.
            challenge_id (str): The unique identifier of the challenge.
            points (int): The number of points to add to the user's score.

        Returns:
            dict: Updated user score for the challenge.
        """
        if challenge_id not in self.user_scores:
            self.user_scores[challenge_id] = {}

        if user_id not in self.user_scores[challenge_id]:
            self.user_scores[challenge_id][user_id] = 0

        self.user_scores[challenge_id][user_id] += points
        print(f"[INFO] Updated user {user_id} score for challenge {challenge_id}: {self.user_scores[challenge_id][user_id]}")
        return {"user_id": user_id, "score": self.user_scores[challenge_id][user_id]}

    def get_leaderboard(self, challenge_id, top_n=10):
        """
        Retrieves the leaderboard for a specific challenge.

        Args:
            challenge_id (str): The unique identifier of the challenge.
            top_n (int): Number of top users to retrieve (default: 10).

        Returns:
            list: A sorted list of top users and their scores.
        """
        if challenge_id not in self.user_scores:
            print(f"[WARNING] No scores found for challenge {challenge_id}")
            return []

        sorted_scores = sorted(
            self.user_scores[challenge_id].items(),
            key=lambda item: item[1],
            reverse=True
        )
        leaderboard = [{"user_id": user, "score": score} for user, score in sorted_scores[:top_n]]
        print(f"[INFO] Leaderboard for challenge {challenge_id}: {leaderboard}")
        return leaderboard

    def reset_scores(self, challenge_id):
        """
        Resets the scores for a specific challenge.

        Args:
            challenge_id (str): The unique identifier of the challenge.

        Returns:
            bool: True if scores were reset, False otherwise.
        """
        if challenge_id in self.user_scores:
            self.user_scores[challenge_id] = {}
            print(f"[INFO] Scores reset for challenge {challenge_id}")
            return True
        print(f"[WARNING] No scores to reset for challenge {challenge_id}")
        return False

# Example usage
if __name__ == "__main__":
    leaderboard = Leaderboard()

    # Update scores
    leaderboard.update_user_score("user123", "challenge1", 150)
    leaderboard.update_user_score("user456", "challenge1", 200)
    leaderboard.update_user_score("user789", "challenge1", 100)

    # Retrieve leaderboard
    print(leaderboard.get_leaderboard("challenge1"))

    # Reset scores
    leaderboard.reset_scores("challenge1")
    print(leaderboard.get_leaderboard("challenge1"))
