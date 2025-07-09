import unittest
from test_base import PDFGeneratorTestBase
from dict2pdf import PDFGenerator

class TestMergeStyles(PDFGeneratorTestBase):
    def test_merge_styles_basic(self):
        custom_styles = {
            'table_title': {'font_size': 16}
        }
        merged = PDFGenerator.merge_styles(self.default_styles, custom_styles)
        self.assertEqual(merged['table_title']['font_size'], 16)
    
    def test_merge_styles_new_category(self):
        custom_styles = {
            'new_style': {'color': 'red'}
        }
        merged = PDFGenerator.merge_styles(self.default_styles, custom_styles)
        self.assertIn('new_style', merged)
    
    def test_merge_styles_nested_update(self):
        custom_styles = {
            'border_cell': {'padding': (8, 12)}  # Changed from 'cell'
        }
        merged = PDFGenerator.merge_styles(self.default_styles, custom_styles)
        self.assertEqual(merged['border_cell']['padding'], (8, 12))  # Changed from 'cell'

if __name__ == '__main__':
    unittest.main()