def cloud_function(json_input):
    finaltext = json_input["text"]
    rep = json_input["repArray"]

    # Processing
    repetition = sum(i for i in rep)

    # return the result
    res = {
        "finaltext": finaltext,
        "repetition": repetition
    }
    return res
