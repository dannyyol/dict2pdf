from test_base import PDFGeneratorTestBase
from dict2pdf import PDFGenerator
from reportlab.lib import colors

class TestCreateParagraph(PDFGeneratorTestBase):
    def test_create_paragraph_basic(self):
        paragraph = PDFGenerator.create_paragraph("Test", 'table_title', self.default_styles)
        self.assertEqual(paragraph.text, "TEST")
    
    def test_create_paragraph_custom_style(self):
        custom_styles = {
            'table_title': {
                'font_size': 20,
                'text_transform': 'uppercase'
            }
        }
        paragraph = PDFGenerator.create_paragraph("test", 'table_title', custom_styles)
        self.assertEqual(paragraph.text, "TEST")
    
    def test_create_paragraph_default_style(self):
        paragraph = PDFGenerator.create_paragraph("Test", 'nonexistent_style', self.default_styles)
        self.assertEqual(paragraph.style.fontSize, 8)