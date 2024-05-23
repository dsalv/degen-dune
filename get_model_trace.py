def get_model_trace(trace: dict) -> dict:
    type = trace.get("type", None)
    type = type.upper() if type else None

    if type in ["CALL", "DELEGATECALL", "STATICCALL", "CALLCODE"]:
        return {
            "type": "call",
            "call_type": type.lower(),
            "address": None,
            "to": trace.get("to", None),
            "input": trace.get("input", None),
            "code": None,
            "output": trace.get("output", None),
            "refund_address": None
        }
    elif type in ["CREATE", "CREATE2"]:
        return {
            "type": "create",
            "call_type": None,
            "address": trace.get("to", None),
            "to": None,
            "input": None,
            "code": trace.get("input", None),
            "output": None,
            "refund_address": None
        }
    elif type == "SELFDESTRUCT":
        return {
            "type": "suicide",
            "call_type": None,
            "address": trace.get("from", None),
            "to": trace.get("from", None),
            "input": None,
            "code": trace.get("input", None),
            "output": None,
            "refund_address": trace.get("to", None),
        }
    elif type == "INVALID":
        return {
            "type": "invalid",
            "call_type": None,
            "address": trace.get("to", None),
            "to": None,
            "input": None,
            "code": trace.get("input", None),
            "output": None,
            "refund_address": None
        }
    elif type == "STOP":
        return {
            "type": "stop",
            "call_type": None,
            "address": None,
            "to": None,
            "input": None,
            "code": None,
            "output": None,
            "refund_address": None
        }
    else:
        return {
            "type": type.lower(),
            "call_type": None,
            "address": None,
            "to": None,
            "input": None,
            "code": None,
            "output": None,
            "refund_address": None
        }

