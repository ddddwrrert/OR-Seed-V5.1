def find_reference(references, identifier):
    return next((item for item in references if item["reference"] == identifier), None)
