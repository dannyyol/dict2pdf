from test_base import PDFGeneratorTestBase
from dict2pdf import PDFGenerator
import os

class TestGeneratePDF(PDFGeneratorTestBase):
    def setUp(self):
        super().setUp()
        self.test_output = "test_output.pdf"
    
    def tearDown(self):
        if os.path.exists(self.test_output):
            os.remove(self.test_output)
    
    def test_generate_pdf_basic(self):
        result = PDFGenerator.generate_pdf_from_dict(
            self.sample_data,
            self.test_output,
            "Test Report"
        )
        self.assertTrue(os.path.exists(result))
    
    def test_generate_pdf_buffer(self):
        result = PDFGenerator.generate_pdf_from_dict(
            self.sample_data,
            "buffer",
            "Test Report"
        )
        self.assertTrue(hasattr(result, 'read'))
    
    def test_generate_pdf_invalid_data(self):
        with self.assertRaises(ValueError):
            PDFGenerator.generate_pdf_from_dict(
                {"invalid": "data"},  # Not a list
                self.test_output,
                "Test Report"
            )