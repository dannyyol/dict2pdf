from test_base import PDFGeneratorTestBase
from dict2pdf import PDFGenerator
from reportlab.platypus import Paragraph, KeepInFrame

class TestFormatValue(PDFGeneratorTestBase):
    def test_format_value_string(self):
        result = PDFGenerator.format_value("Test", self.default_styles)
        self.assertIsInstance(result, Paragraph)
    
    def test_format_value_number(self):
        result = PDFGenerator.format_value(42, self.default_styles)
        self.assertIsInstance(result, Paragraph)
    
    def test_format_value_dict(self):
        test_dict = {"key": "value"}
        result = PDFGenerator.format_value(test_dict, self.default_styles)
        self.assertIsInstance(result, KeepInFrame)
    
    def test_format_value_list(self):
        test_list = ["item1", "item2"]
        result = PDFGenerator.format_value(test_list, self.default_styles)
        self.assertIsInstance(result, KeepInFrame)