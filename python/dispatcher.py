import json
import os
from python.handlers import gift_handler, sale_handler, ots_handler
from python.renderer import render_docx

# FIX: base directory
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

HANDLERS = {
    "gift_handler": gift_handler,
    "sale_handler": sale_handler,
    "ots_handler": ots_handler
}


def load_config(doc_type):
    # FIX: absolute config path
    with open(os.path.join(BASE_DIR, "configs", f"{doc_type}.json"), "r", encoding="utf-8") as f:
        return json.load(f)


def dispatch(doc_type, input_data, output_path):
    config = load_config(doc_type)

    # Validate required fields
    for field in config["required"]:
        if field not in input_data or input_data[field] == "":
            raise ValueError(f"Missing required field: {field}")

    handler = HANDLERS[config["handler"]]

    processed_data = handler(input_data, config["template"])

    # FIX: absolute template path
    template_path = os.path.join(BASE_DIR, "templates", config["template"])

    render_docx(
        template_path=template_path,
        output_path=output_path,
        values=processed_data
    )
