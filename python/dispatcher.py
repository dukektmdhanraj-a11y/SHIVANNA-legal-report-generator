def dispatch(doc_type, input_data):
    config = load_config(doc_type)

    for field in config["required"]:
        if field not in input_data or input_data[field] == "":
            raise ValueError(f"Missing required field: {field}")

    handler = HANDLERS[config["handler"]]

    processed_data = handler(input_data, config["template"])

    template_path = f"templates/{config['template']}"
    filename = f"{doc_type}_report.docx"

    output_path = render_docx(template_path, filename, processed_data)

    return output_path
