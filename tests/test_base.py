import unittest
from dict2pdf import PDFGenerator, DEFAULT_STYLES
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import Paragraph, Table

class PDFGeneratorTestBase(unittest.TestCase):
    def setUp(self):
        self.default_styles = DEFAULT_STYLES
        self.sample_data = [
            {
                "id": 101,
                "name": "John Doe",
                "department": {"name": "Engineering"}
            }
        ]