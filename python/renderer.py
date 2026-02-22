from docxtpl import DocxTemplate
from io import BytesIO

def render_docx(template_path, values):
    doc = DocxTemplate(template_path)
    doc.render(values)

    buffer = BytesIO()
    doc.save(buffer)
    buffer.seek(0)

    return buffer
