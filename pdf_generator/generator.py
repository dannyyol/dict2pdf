import io
from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle,
    KeepInFrame
)
from reportlab.lib.units import inch
from reportlab.lib.enums import TA_CENTER, TA_LEFT

from .styles import DEFAULT_STYLES

class PDFGenerator:
    @staticmethod
    def merge_styles(default_styles, custom_styles):
        """Merge custom styles with defaults"""
        merged = default_styles.copy()
        for category, styles in custom_styles.items():
            if category in merged:
                merged[category].update(styles)
            else:
                merged[category] = styles
        return merged

    @staticmethod
    def flatten_dict(d, parent_key='', sep='_'):
        """Flatten nested dictionary"""
        items = []
        for k, v in d.items():
            new_key = f"{parent_key}{sep}{k}" if parent_key else k
            if isinstance(v, dict):
                items.extend(PDFGenerator.flatten_dict(v, new_key, sep=sep).items())
            else:
                items.append((new_key, v))
        return dict(items)

    @staticmethod
    def create_paragraph(text, style, styles_config):
        """Create a styled paragraph with full body style integration"""
        style_config = styles_config.get(style, {})
        body_style = styles_config.get('body', {})
        
        para_style = ParagraphStyle(
            name=style,
            fontName=style_config.get('font_name', body_style.get('font_name', 'Helvetica')),
            fontSize=style_config.get('font_size', body_style.get('font_size', 12)),
            textColor=style_config.get('text_color', body_style.get('text_color', colors.black)),
            spaceAfter=style_config.get('space_after', 0),
            leading=style_config.get('leading', body_style.get('leading', 14)),
            alignment=style_config.get('alignment', TA_LEFT),
            backColor=body_style.get('back_color', None),
            leftIndent=body_style.get('left_padding', 0),
            rightIndent=body_style.get('right_padding', 0),
            spaceBefore=body_style.get('top_padding', 0),
            wordWrap='CJK',
            splitLongWords=True
        )
        # Apply text transformation if specified
        text_transform = style_config.get('text_transform')
        if text_transform == 'uppercase':
            text = text.upper()
        elif text_transform == 'lowercase':
            text = text.lower()
        elif text_transform == 'capitalize':
            text = text.title()

        return Paragraph(text, para_style)

    @staticmethod
    def create_table(data, col_widths=None, style=None, styles_config=None, is_horizontal=False):
        """Create a styled table with full body style integration"""
        # Get style configurations from the style dictionary
        body_style = styles_config.get('body', {})
        border_cell_style = styles_config.get('border_cell', {})  # Changed from cell_style
        header_style = styles_config.get('header_cell', {})
        
        # Define base table styling
        table_style = [
            # Basic table grid and borders
            ('GRID', (0, 0), (-1, -1), 
             border_cell_style.get('border_width', 0.5),  # Changed from cell_style
             border_cell_style.get('border_color', colors.HexColor('#cccccc'))),  # Changed from cell_style
            
            # Cell alignment and spacing
            ('ALIGN', (0, 0), (-1, -1), border_cell_style.get('alignment', 'LEFT')),
            ('VALIGN', (0, 0), (-1, -1), 'TOP'),
            ('PADDING', (0, 0), (-1, -1), 
             body_style.get('left_padding', 6), 
             body_style.get('top_padding', 4)),
            
            # Font configuration for all cells
            ('FONTNAME', (0, 0), (-1, -1), body_style.get('font_name', 'Helvetica')),
            ('FONTSIZE', (0, 0), (-1, -1), body_style.get('font_size', 8)),
            ('LEADING', (0, 0), (-1, -1), body_style.get('leading', 10)),
            ('TEXTCOLOR', (0, 0), (-1, -1), body_style.get('text_color', colors.HexColor('#333'))),
        ]
        
        # Add background color if specified
        if body_style.get('back_color'):
            table_style.append(
                ('BACKGROUND', (0, 0), (-1, -1), body_style['back_color'])
            )
        
        # Special styling for header row in vertical layout
        if not is_horizontal and header_style:
            table_style.extend([
                # Header background
                ('BACKGROUND', (0, 0), (-1, 0), 
                header_style.get('back_color', colors.HexColor('#ffffff'))),
                
                # Header font styling
                ('FONTSIZE', (0, 0), (-1, 0), 
                header_style.get('font_size', body_style.get('font_size', 10) + 2)),
                ('TEXTCOLOR', (0, 0), (-1, 0), 
                header_style.get('text_color', colors.HexColor('#000000'))),
                
                # Header padding and spacing
                ('PADDING', (0, 0), (-1, 0), 
                header_style.get('padding_left', 8),
                header_style.get('padding_top', 6)),
                ('LEADING', (0, 0), (-1, 0), 
                header_style.get('leading', body_style.get('leading', 12) + 2)),
            ])
            
        # Apply any additional custom styles
        if style:
            table_style.extend(style)
            
        # Add WORDWRAP command if word_wrap is True
        if border_cell_style.get('word_wrap', False):  # Changed from cell_style
            table_style.append(('WORDWRAP', (0, 0), (-1, -1), True))
            
        # Create and return the final table
        table = Table(data, colWidths=col_widths)
        table.setStyle(TableStyle(table_style))
        table._style_commands = table_style  # Expose for testing
        return table

    @staticmethod
    def format_value(value, styles_config, nested_table=False, max_length=300, max_height=200):
        """Format values with strict size constraints"""
        # Get base style configuration
        body_style = styles_config.get('body', {})
        
        # Create base paragraph style for all content
        normal_style = ParagraphStyle(
            name='Normal',
            fontName=body_style.get('font_name', 'Helvetica'),
            fontSize=body_style.get('font_size', 8),
            leading=body_style.get('leading', 10),
            textColor=body_style.get('text_color', colors.HexColor('#333')),
            spaceBefore=0,
            spaceAfter=0,
            leftIndent=0,
            rightIndent=0,
            wordWrap='CJK',
            splitLongWords=True,
            back_color=body_style.get('back_color', colors.HexColor('#f9f9f9')),
        )
        
        # Handle different value types
        if value is None:
            return Paragraph("None", normal_style)
        
        # Handle string values with truncation and splitting
        if isinstance(value, str):
            if len(value) > max_length:
                value = value[:max_length] + "... [truncated]"
            if len(value) > 100:
                chunks = simpleSplit(value, normal_style.fontName, normal_style.fontSize, max_height)
                if chunks:
                    return [Paragraph(chunk, normal_style) for chunk in chunks]
            return Paragraph(value, normal_style)
        
        # Handle numeric values
        if isinstance(value, (int, float)):
            return Paragraph(str(value), normal_style)
        
        # Handle dictionary values with nested formatting
        if isinstance(value, dict):
            formatted_items = []
            for k, v in value.items():
                key_para = Paragraph(f"<b>{k}:</b>", normal_style)
                value_para = PDFGenerator.format_value(v, styles_config, nested_table, max_length, max_height)
                
                # Handle both single and multiple paragraph responses
                if isinstance(value_para, list):
                    formatted_items.extend([key_para] + value_para)
                else:
                    formatted_items.extend([key_para, value_para])
                formatted_items.append(Spacer(1, 4))
            
            if formatted_items:
                formatted_items.pop()  # Remove last spacer
            return KeepInFrame(maxWidth=400, maxHeight=max_height, content=formatted_items)
        
        # Handle list values
        if isinstance(value, list):
            # Handle list of strings
            if all(isinstance(item, str) for item in value):
                formatted_items = []
                for item in value:
                    formatted_items.append(PDFGenerator.format_value(item, styles_config, nested_table, max_length, max_height))
                    formatted_items.append(Spacer(1, 4))
                if formatted_items:
                    formatted_items.pop()  # Remove last spacer
                return KeepInFrame(maxWidth=400, maxHeight=max_height, content=formatted_items)
            
            # Handle list of dictionaries
            elif all(isinstance(item, dict) for item in value):
                formatted_items = []
                for idx, item in enumerate(value, 1):
                    if idx > 1:
                        formatted_items.append(Spacer(1, 8))
                    formatted_items.append(Paragraph(f"<b>Item {idx}:</b>", normal_style))
                    nested_items = PDFGenerator.format_value(item, styles_config, nested_table, max_length, max_height)
                    if isinstance(nested_items, list):
                        formatted_items.extend(nested_items)
                    else:
                        formatted_items.append(nested_items)
                return KeepInFrame(maxWidth=400, maxHeight=max_height, content=formatted_items)
        
        # Fallback for any other type
        return Paragraph(str(value), normal_style)

    @staticmethod
    def generate_table(data, title, layout="horizontal", styles=None, title_key=None, nested_table=False):
        """Generate table structure that handles any dictionary dynamically"""
        effective_styles = PDFGenerator.merge_styles(DEFAULT_STYLES, styles) if styles else DEFAULT_STYLES
        elements = []
        elements.append(PDFGenerator.create_paragraph(title, 'table_title', effective_styles))
        
        horizontal_tables = [data] if isinstance(data, dict) else data
        
        if layout == "horizontal":
            for i, entry in enumerate(horizontal_tables, 1):
                if title_key is None:
                    horizontal_table_title = f"Entry {i}"
                elif title_key == "":
                    horizontal_table_title = None
                else:
                    horizontal_table_title = entry.get(title_key, title_key)
                
                if horizontal_table_title:
                    elements.append(PDFGenerator.create_paragraph(str(horizontal_table_title), 'horizontal_table_title', effective_styles))
                
                table_data = []

                for key, value in entry.items():
                    if title_key is not None and key == title_key:
                        continue
                    formatted_value = PDFGenerator.format_value(value, effective_styles, nested_table)
                    table_data.append([
                        Paragraph(str(key), getSampleStyleSheet()['Normal']),
                        formatted_value if isinstance(formatted_value, list) else [formatted_value]
                    ])
                
                horizontal_table = PDFGenerator.create_table(
                    table_data,
                    col_widths=effective_styles['horizontal_table']['col_widths'],
                    styles_config=effective_styles,
                    is_horizontal=True
                )
                elements.append(horizontal_table)
                elements.append(Spacer(1, effective_styles['horizontal_table']['space_after']))
        else:
            if not horizontal_tables:
                return elements
                
            # Get all unique keys while maintaining order from first entry
            all_keys = []
            seen_keys = set()
            for entry in horizontal_tables:
                for key in entry.keys():
                    if key not in seen_keys:
                        seen_keys.add(key)
                        all_keys.append(key)
            
            table_data = [[Paragraph(str(h).upper(), getSampleStyleSheet()['Normal']) for h in all_keys]]
            for entry in horizontal_tables:
                row = []
                for key in all_keys:
                    value = entry.get(key, '')
                    formatted_value = PDFGenerator.format_value(value, effective_styles, nested_table)
                    row.append(formatted_value if isinstance(formatted_value, list) else [formatted_value])
                table_data.append(row)
            
            col_count = len(all_keys)
            col_width = f"{100//col_count}%"
            col_widths = [col_width] * col_count
            
            data_table = PDFGenerator.create_table(
                table_data,
                col_widths=col_widths,
                styles_config=effective_styles,
                is_horizontal=False
            )
            elements.append(data_table)
            elements.append(Spacer(1, effective_styles['data_table']['space_after']))
        
        return elements

    @staticmethod
    def generate_pdf_from_dict(data, output_file="output.pdf", title="Report", 
                            layout="horizontal", styles=None, title_key=None, 
                            nested_table=False, output_dir=None):
        """Generate PDF with comprehensive error handling"""
        # Validate input data structure
        if not isinstance(data, (list)):
            raise ValueError("Input data must be a list of dictionaries")
            
        if isinstance(data, list) and not all(isinstance(item, dict) for item in data):
            raise ValueError("All items in the list must be dictionaries")

        buffer = io.BytesIO()
        effective_styles = PDFGenerator.merge_styles(DEFAULT_STYLES, styles) if styles else DEFAULT_STYLES
        page_size = letter
        
        # Handle output directory
        if output_dir:
            import os
            os.makedirs(output_dir, exist_ok=True)
            output_path = os.path.join(output_dir, output_file)
        else:
            output_path = output_file
            
        try:
            doc = SimpleDocTemplate(
                buffer if output_file == "buffer" else output_path,
                pagesize=page_size,
                leftMargin=effective_styles['body']['left_padding'],
                rightMargin=effective_styles['body']['right_padding'],
                topMargin=effective_styles['body']['top_padding'],
                bottomMargin=effective_styles['body']['bottom_padding'],
                allowSplitting=1
            )
            
            elements = PDFGenerator.generate_table(
                data, title, layout, effective_styles, title_key, nested_table
            )
            
            doc.build(elements)
            
            if output_file == "buffer":
                buffer.seek(0)
                return buffer
            return output_path
            
        except Exception as e:
            error_msg = f"PDF generation failed: {str(e)}"
            if output_file == "buffer":
                buffer = io.BytesIO()
                doc = SimpleDocTemplate(buffer, pagesize=letter)
                doc.build([Paragraph(error_msg, getSampleStyleSheet()['Normal'])])
                buffer.seek(0)
                return buffer
            else:
                doc = SimpleDocTemplate(output_path, pagesize=letter)  # Use output_path for error document too
                doc.build([Paragraph(error_msg, getSampleStyleSheet()['Normal'])])
                return output_path  # Return the full path