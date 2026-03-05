def risk_profiler(accidents):

    if accidents > 2:
        return "High"
    elif accidents > 0:
        return "Medium"
    else:
        return "Low"


def conversion_predictor():

    import random
    return random.randint(10,95)


def premium_advisor(premium):

    if premium > 1200:
        return "Premium too high - recommend discount"
    else:
        return "Premium acceptable"


def decision_router(risk,conversion):

    if risk == "High":
        return "Escalate to Underwriter"
    elif conversion < 40:
        return "Agent Follow Up"
    else:
        return "Auto Approve"