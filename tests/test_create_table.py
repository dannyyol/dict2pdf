from test_base import PDFGeneratorTestBase
from dict2pdf import PDFGenerator
from reportlab.lib import colors
from reportlab.platypus import Table, TableStyle

class TestCreateTable(PDFGeneratorTestBase):
    def test_create_table_basic(self):
        data = [["Header", "Value"], ["Key", "Data"]]
        table = PDFGenerator.create_table(data, styles_config=self.default_styles)
        self.assertIsInstance(table, Table)
        self.assertEqual(table._cellvalues, data)
    
    def test_create_table_word_wrap(self):
        styles = self.default_styles.copy()
        styles['border_cell'] = {'word_wrap': True, 'leading': 12}  # Changed from 'cell'
        data = [["Long text that should wrap", "Value"]]
        table = PDFGenerator.create_table(data, styles_config=styles)
        
        # Verify word wrap is enabled
        self.assertTrue(hasattr(table, '_style_commands'))
        if hasattr(table, '_style_commands'):
            # Check for either 'WORDWRAP' command or wordWrap=True in style
            has_wordwrap = any(
                cmd[0] == 'WORDWRAP' or 
                (cmd[0] == 'STYLE' and cmd[3].wordWrap)
                for cmd in table._style_commands
            )
            self.assertTrue(has_wordwrap)
    
    def test_create_table_header_style(self):
        data = [["Header", "Value"], ["Key", "Data"]]
        table = PDFGenerator.create_table(
            data, 
            styles_config=self.default_styles,
            is_horizontal=False
        )
        self.assertTrue(any(cmd[0] == 'BACKGROUND' for cmd in table._style_commands))