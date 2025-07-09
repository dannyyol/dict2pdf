# dict2pdf/styles.py
from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER, TA_LEFT

DEFAULT_STYLES = {
    'body': {
        'font_name': 'Helvetica',
        'font_size': 8,
        'leading': 10,
        'text_color': colors.HexColor('#333'),
        'back_color': colors.HexColor('#ffffff'),
        'left_padding': 20,
        'right_padding': 20,
        'top_padding': 20,
        'bottom_padding': 20
    },
    'table_title': {
        'font_name': 'Helvetica-Bold',
        'font_size': 12,
        'text_color': colors.HexColor('#2c3e50'),
        'space_after': 10,
        'alignment': TA_CENTER,
        'underline_color': colors.HexColor('#3498db'),
        'underline_width': 2,
        'underline_offset': -4,
        'text_transform': 'uppercase',
        'letter_spacing': 0.5
    },
    'horizontal_table_title': {
        'font_name': 'Helvetica-Bold',
        'font_size': 12, # Reduced from 16
        'text_color': colors.HexColor('#3498db'),
        'space_after': 12,
        'alignment': TA_LEFT,
        'text_transform': 'capitalize',
    },
    'horizontal_table': {
        'space_after': 12,
        'col_widths': ['15%', '85%'],
    },
    'data_table': {
        'space_after': 10,
        'col_widths': ['20%', '20%', '15%', '20%', '25%'],
        'border_width': 20.5,
        'border_color': colors.HexColor('#cccccc')
    },
    'border_cell': {
        'border_width': 0.5,
        'border_color': colors.HexColor('#cccccc'),
    },
    'header_cell': {
        'back_color': colors.HexColor('#ffffff'),
        'font_size': 10,
        'text_color': colors.HexColor('#333'),
        'padding': (8, 6),
        'leading': 14
    }
}