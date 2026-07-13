def format_market_value(value):

    if value is None:
        return "-"

    if value >= 1_000_000_000:
        return f"{value / 1_000_000_000:.2f} B€"

    if value >= 1_000_000:
        return f"{value / 1_000_000:.1f} M€"

    if value >= 1_000:
        return f"{value / 1_000:.0f} K€"

    return f"{value:.0f} €"