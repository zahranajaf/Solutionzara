def cloud_function(json_input):
    text = json_input["text"]
    w = json_input["w"]

    words = text.split()
    
    # Processing
    result = [words[i:i + w] for i in range(0, len(words), w)]

    # return the result
    res = {
        "wordArray": result
    }
    return res
