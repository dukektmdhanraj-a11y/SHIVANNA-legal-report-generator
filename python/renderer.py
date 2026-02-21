from docxtpl import DocxTemplate
import os

def render_docx(template_path, filename, values):
    doc = DocxTemplate(template_path)
    doc.render(values)

    output_path = os.path.join("/tmp", filename)  # save only in /tmp on Render
    doc.save(output_path)

    return output_path
