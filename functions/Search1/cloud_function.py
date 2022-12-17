def cloud_function(json_input):
    S = json_input["batch"]
    p = json_input["p"]
    
    # Processing
    count=0
    for i in S:
        if i==p:
            count+=1

    # return the result
    res = {
        "repetition": count
    }
    return res
