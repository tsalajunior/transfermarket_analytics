class PlayerMetricsService:

    @staticmethod
    def compute_metrics(stat):

        if stat.minutes_played == 0:
            return

        stat.goals_per_90 = (
            stat.goals * 90
        ) / stat.minutes_played

        stat.assists_per_90 = (
            stat.assists * 90
        ) / stat.minutes_played

        stat.goal_contribution_per_90 = (
            (stat.goals + stat.assists) * 90
        ) / stat.minutes_played

        if stat.goals > 0:
            stat.minutes_per_goal = (
                stat.minutes_played
                / stat.goals
            )

        stat.yellow_per_90 = (
            stat.yellow_cards * 90
        ) / stat.minutes_played

        stat.performance_score = (
            stat.goals * 4
            + stat.assists * 3
            - stat.yellow_cards
            - stat.red_cards * 3
        )