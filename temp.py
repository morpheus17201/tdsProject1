response = {
    "id": "chatcmpl-AxM44YumZEEg1VxS2bGdjby2FgCRy",
    "object": "chat.completion",
    "created": 1738709532,
    "model": "gpt-4o-mini-2024-07-18",
    "choices": [
        {
            "index": 0,
            "message": {
                "role": "assistant",
                "content": None,
                "tool_calls": [
                    {
                        "id": "call_jLagMEGtKx6Q3VSMCDYyCWte",
                        "type": "function",
                        "function": {
                            "name": "extract_numbers_from_image",
                            "arguments": '{"input_file_path":"/data/credit-card.png","output_file_path":"/data/credit-card.txt"}',
                        },
                    }
                ],
                "refusal": None,
            },
            "logprobs": None,
            "finish_reason": "tool_calls",
        }
    ],
    "usage": {
        "prompt_tokens": 794,
        "completion_tokens": 35,
        "total_tokens": 829,
        "prompt_tokens_details": {"cached_tokens": 0, "audio_tokens": 0},
        "completion_tokens_details": {
            "reasoning_tokens": 0,
            "audio_tokens": 0,
            "accepted_prediction_tokens": 0,
            "rejected_prediction_tokens": 0,
        },
    },
    "service_tier": "default",
    "system_fingerprint": "fp_bd83329f63",
    "monthlyCost": 0.044854379999999874,
    "cost": 0.002592,
    "monthlyRequests": 233,
    "costError": "crypto.createHash is not a function",
}

# print(response["tool_calls"][0]["function"])
fname = response["choices"][0]["message"]["tool_calls"][0]["function"]["name"]
print(f"Function name: {fname}")
arguments = response["choices"][0]["message"]["tool_calls"][0]["function"]["arguments"]
print(f"Arguments: {arguments}")


def extract_numbers_from_image(input_file_path, output_file_path):
    print(f"Inside dummy function")
    print(f"Argumnets received: {input_file_path=}, {output_file_path=}")


import json

arg_dict = json.loads(arguments)


fun = globals()[fname]
fun(**arg_dict)


m = {
    "id": "chatcmpl-Axe7XfZS1OHgBjQPNJF2mNXSsWZbn",
    "object": "chat.completion",
    "created": 1738778939,
    "model": "gpt-4o-mini-2024-07-18",
    "choices": [
        {
            "index": 0,
            "message": {
                "role": "assistant",
                "content": 'I\'m not sure what you mean by "random xyz task." Could you please provide more details or specify a task you would like me to perform?',
                "refusal": None,
            },
            "logprobs": None,
            "finish_reason": "stop",
        }
    ],
    "usage": {
        "prompt_tokens": 770,
        "completion_tokens": 31,
        "total_tokens": 801,
        "prompt_tokens_details": {"cached_tokens": 0, "audio_tokens": 0},
        "completion_tokens_details": {
            "reasoning_tokens": 0,
            "audio_tokens": 0,
            "accepted_prediction_tokens": 0,
            "rejected_prediction_tokens": 0,
        },
    },
    "service_tier": "default",
    "system_fingerprint": "fp_bd83329f63",
    "monthlyCost": 0.08107337999999986,
    "cost": 0.002496,
    "monthlyRequests": 247,
    "costError": "crypto.createHash is not a function",
}
