SCHEMA = {
    "$schema": "http://json-schema.org/draft-04/schema#",
    "description": "Telephone call detail records",
    "type": "object",
    "properties": {
        "id": {
            "description": "Record unique identificator",
            "type": ["string", "integer"]
        },
        "type": {
            "description": "Indicate if it's a call 'start' or 'end' record",
            "enum": ["start", "end"]
        },
        "timestamp": {
            "description": "The timestamp of when the event occured",
            "type": "string",
            "format": "data-time"
        },
        "call_id": {
            "description": "Unique for each call record pair",
            "type": ["string", "integer"]
        },
        "source": {
            "description": "The subscriber phone number that originated the call",
            "type": ["string", "integer"],
            "maxLength": 11,
            "minLength": 10,
            "minimum": 1000000000,
            "maximum": 100000000000,
            "exclusiveMaximum": True

        },
        "destination": {
            "description": "The phone number receiving the call",
            "type": ["string", "integer"],
            "maxLength": 11,
            "minLength": 10,
            "minimum": 1000000000,
            "maximum": 100000000000,
            "exclusiveMaximum": True
        }
    },
    "oneOf": [
        {
            "properties": {
                "type": {"enum": ["start"]}
            },
            "required": ["id", "timestamp", "call_id", "source", "destination"]
        },
        {
            "properties": {
                "type": {"enum": ["end"]}
            },
            "required": ["id", "timestamp", "call_id"]
        }
    ],
    "required": ["type"],
    "additionalProperties": False
}
