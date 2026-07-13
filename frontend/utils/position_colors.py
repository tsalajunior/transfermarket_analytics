POSITION_COLORS = {
    "Goalkeeper": "#f1c40f",

    "Centre-Back": "#3498db",
    "Left-Back": "#5dade2",
    "Right-Back": "#5dade2",

    "Defensive Midfield": "#9b59b6",
    "Central Midfield": "#2ecc71",
    "Attacking Midfield": "#27ae60",

    "Left Winger": "#e67e22",
    "Right Winger": "#e67e22",

    "Centre-Forward": "#e74c3c",
    "Second Striker": "#ff6b6b",
}

def color_position(position: str):

    color = POSITION_COLORS.get(position, "#95a5a6")

    return (
        f"background-color:{color};"
        "color:white;"
        "font-weight:bold;"
        "text-align:center;"
        "border-radius:4px;"
    )