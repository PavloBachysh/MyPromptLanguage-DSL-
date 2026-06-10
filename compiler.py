from textx import metamodel_from_file
import json

def Limitation(value, min_val, max_val = None):
    if max_val is not None:
        if value < min_val or value > max_val:
            raise ValueError(f"Error, your value {value} but it must be higher than {min_val} and lower that {max_val}")
        else:
            return value
    else:
        if value <= min_val:
            raise ValueError(f"Error, your value {value} but it must be higher than {min_val}")
        else:
            return value
    


meta = metamodel_from_file('grammar.tx')
try:
    model = meta.model_from_file('prompt.conf')
    print("File is founded")

    resault = {}
    for rule in model.rules:
        rule_type = rule.__class__.__name__
        match rule_type:
            case "ModelRule":
                resault["model"] = rule.model
            case "MessagesRule":
                messages = rule.messages
                messages_array = []
                for message in messages:
                    mes = {}
                    mes["role"] = message.role
                    mes["content"] = message.content
                    messages_array.append(mes)
                resault["messages"] = messages_array
            case "TemperatureRule":
                resault["temperature"] = Limitation(rule.temperature, 0, 2)
            case "TopPRule":
                resault["top_p"] = Limitation(rule.top_p, 0, 1)
            case "MaxTokenRule":
                resault["max_completion_tokens"] = Limitation(rule.max_completion_tokens, 0)
            case "PresencePenaltyRule":
                resault["presence_penalty"] = Limitation(rule.presence_penalty, -2, 2)
            case "FrequencyPenaltyRule":
                resault["frequency_penalty"] = Limitation(rule.frequency_penalty, -2, 2)
            case "ReasoningEffortRule":
                resault["reasoning_effort"] = rule.reasoning_effort

    if "top_p" in resault and "temperature" in resault:
        print("It is not recomended to use both top_p and temperature. It may cause some troubles.")

    output_filename = 'output.json'

    with open(output_filename, 'w', encoding='utf-8') as json_file:
        json.dump(resault, json_file, indent=4, ensure_ascii=False)

except Exception as e:
    print(f"Error: {e}")
