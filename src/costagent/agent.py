TOOLS = ["profile_bill", "recommend"]
WRITES = ("apply", "resize", "delete",)


class InputError(ValueError):
    pass


def run(goal, payload):
    if not isinstance(goal, str) or not goal.strip():
        raise InputError("goal is empty")
    if any(word in goal.lower() for word in WRITES):
        return {"refused": True, "reason": "This agent only reads or plans. It does not write.", "tools": [], "wrote": False, "applied": False}
    result = [row["service"] for row in payload.get("lines") or [] if float(row.get("cost", 0)) >= 50]
    return {"refused": False, "tools": TOOLS, "flags": result, "wrote": False, "applied": False}
