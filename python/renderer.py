from docxtpl import DocxTemplate


def render_docx(template_path, output_path, values):
    doc = DocxTemplate(template_path)
    doc.render(values)
    doc.save(output_path)
