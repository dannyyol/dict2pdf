from test_base import PDFGeneratorTestBase
from dict2pdf import PDFGenerator
from reportlab.platypus import Table, Paragraph

class TestGenerateTable(PDFGeneratorTestBase):
    def test_generate_table_horizontal(self):
        elements = PDFGenerator.generate_table(
            self.sample_data,
            "Test Report",
            layout="horizontal",
            styles=self.default_styles
        )
        self.assertTrue(any(isinstance(elem, Table) for elem in elements))
    
    def test_generate_table_vertical(self):
        elements = PDFGenerator.generate_table(
            self.sample_data,
            "Test Report",
            layout="vertical",
            styles=self.default_styles
        )
        self.assertTrue(any(isinstance(elem, Table) for elem in elements))
    
    def test_generate_table_with_title_key(self):
        elements = PDFGenerator.generate_table(
            self.sample_data,
            "Test Report",
            title_key="name",
            styles=self.default_styles
        )
        self.assertTrue(any(
            isinstance(elem, Paragraph) and "John Doe" in elem.text 
            for elem in elements
        ))