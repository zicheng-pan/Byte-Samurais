# 设置环境变量里面
import json
import os
from openai import OpenAI
from flask import Flask, request

# 查找最近的4s店位置
# 选择第二个位置，查看这个4s店的可使用时间
# 那么选择刚刚第一个位置来查看4s店的可用时间
# 帮我预定周六上午的时间

static_messages = [
    {"role": "system",
     "content": "Assume you are a professional car repair diagnostic expert. Users will send in car-related questions, and you can provide professional answers."}
]
app = Flask(__name__)

client = OpenAI(
    # This is the default and can be omitted
    api_key=os.environ.get("OPENAI_API_KEY"),
)


def get_current_4s_avaiable(location):
    if location == '{"location":"No. 1373-1, Jiangyang South Road, Baoshan District, Shanghai."}':
        return ["Saturday morning from 9:00 to 10:00", "Sunday afternoon from 3:00 to 4:00."]
    else:
        return "The current 4S dealership is too busy and has no available time slots."


def get_current_4s_location():
    # TODO 获取4s店地址
    return [
        "No. 1373-1, Jiangyang South Road, Baoshan District, Shanghai.",
        "Songjiang area, No. 6282 Beisong Highway, Songjiang."
    ]


def boot4s(function_args):
    location = json.loads(function_args).get("location")
    time_start = json.loads(function_args).get("timestart")
    time_end = json.loads(function_args).get("timeend")
    return location + " booked from " + time_start + " to " + time_end + " successfully."


# 第一个字典定义了一个名为"get_current_weather"的功能
functions = [
    {
        "name": "get_current_4s_location",
        "description": "Obtain the current location of the 4S store"
    }, {
        "name": "get_current_4s_avaiable",
        "description": "Obtain the current available appointment times for the 4S dealership.",
        "parameters": {
            "type": "object",
            "properties": {
                "location": {
                    "type": "string",
                    "description": "The location to get the 4s dealership."
                }
            },
            "required": ["location"],
        },
    }, {
        "name": "boot4s",
        "description": "Book the available time slots for this 4S dealership.",
        "parameters": {
            "type": "object",
            "properties": {
                "location": {
                    "type": "string",
                    "description": "The location to get the 4s dealership"
                },
                "timestart": {
                    "type": "string",
                    "description": "The time slot start"
                },
                "timeend": {
                    "type": "string",
                    "description": "The time slot end"
                }
            },
            "required": ["location"],
        },
    }
]


#
# from openai import OpenAI
#
def chatAPI(role, message):
    current_message = {"role": role, "content": message}
    static_messages.append(current_message)
    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=static_messages,
        functions=functions
        # max_tokens=100
    )
    # if function_call is not None:
    #     json_data.update({"function_call": function_call})
    message_content = completion.choices[0].message

    if message_content.function_call:
        function_name = message_content.function_call.name
        if message_content.function_call.arguments:
            function_args = message_content.function_call.arguments

        if function_name == "get_current_4s_location":
            # location = json.loads(function_args).get("location")
            # mock 获取当前GPS
            vehicle4s_info = get_current_4s_location()
            static_messages.append({"role": "system", "content": str(vehicle4s_info)})
            return vehicle4s_info
        elif function_name == "get_current_4s_avaiable":
            vehicle4s_info = get_current_4s_avaiable(function_args)
            static_messages.append({"role": "system", "content": str(vehicle4s_info)})
            return vehicle4s_info
        elif function_name == "boot4s":
            vehicle4s_info = boot4s(function_args)
            static_messages.append({"role": "system", "content": str(vehicle4s_info)})
            return vehicle4s_info
    else:
        return static_messages.append({"role": "system", "content": str(message_content)})


@app.route("/userchat", methods=['POST'])
def userchat():
    if request.method == 'POST':
        data = request.form.get("message")
        return chatAPI("user", data)


def getStatus(engine_rpm, lub_oil_pressure, fuel_pressure, coolant_pressure, lub_oil_temp, coolant_temp):
    return "success"


@app.route("/vehiclechat", methods=['POST'])
def vehiclechat():
    if request.method == 'POST':
        engine_rpm = request.form.get("engine_rpm")
        lub_oil_pressure = request.form.get("lub_oil_pressure")
        fuel_pressure = request.form.get("fuel_pressure")
        coolant_pressure = request.form.get("coolant_pressure")
        lub_oil_temp = request.form.get("lub_oil_temp")
        coolant_temp = request.form.get("coolant_temp")
    result = getStatus(engine_rpm, lub_oil_pressure, fuel_pressure, coolant_pressure, lub_oil_temp,
                       coolant_temp)
    return result


if __name__ == "__main__":
    app.run(debug=False)
