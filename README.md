# 📘 PDF Generator

**PDF Generator** is a Python package that converts structured list of dictionaries data into clean, styled PDF documents. It supports horizontal and vertical layouts, nested data structures, and extensive customization options.

---

## 🚀 Features

- ✅ Convert dictionaries into formatted PDFs
- 🧱 Support for horizontal and vertical layouts
- 🎨 Customizable styles (titles, headers, cells)
- 🪆 Handles complex nested structures
- 📝 Word wrapping, text truncation, and alignment support
- 🧩 Optional section titles using keys from your data

---

## 📦 Installation

```bash
pip install pdf-generator
```

---

## 📄 Basic Usage

```python
from dict2pdf import PDFGenerator

data = [
    {
        "id": "P1001",
        "title": "Project Alpha",
        "status": "active",
        "lead_researcher": {
            "name": "Dr. Smith",
            "department": "Research"
        }
    }
]

PDFGenerator.generate_pdf_from_dict(
    data,
    output_file="output.pdf",
    title="Project Report"
)
```

---

## 🎨 Custom Styling

```python
from dict2pdf import PDFGenerator

custom_styles = {
    'table_title': {
        'font_size': 24,
        'space_after': 30,
        'text_transform': 'uppercase'
    },
    'border_cell': {
        'border_width': 0.5,
        'border_color': colors.HexColor('#cccccc'),
    },
    'header_cell': {
        'back_color': '#f2f2f2',
        'font_size': 12,
        'font_name': 'Helvetica-Bold'
    },
    'horizontal_table_title': {
        'font_name': 'Helvetica-Bold',
        'font_size': 12,
        'text_color': colors.HexColor('#3498db'),
        'space_after': 12,
        'alignment': TA_LEFT,
        'text_transform': 'capitalize',
    },
}

PDFGenerator.generate_pdf_from_dict(
    data,
    output_file="styled_report.pdf",
    title="Styled Project Report",
    styles=custom_styles
)
```

---

## 📐 Layout Options

### Horizontal Layout (default)

```python
PDFGenerator.generate_pdf_from_dict(
    data,
    output_file="horizontal.pdf",
    title="Horizontal Layout",
    layout="horizontal"
)
```

### Vertical Layout

```python
PDFGenerator.generate_pdf_from_dict(
    data,
    output_file="vertical.pdf",
    title="Vertical Layout",
    layout="vertical"
)
```

---

## 📁 Custom Output Directory

```python
PDFGenerator.generate_pdf_from_dict(
    data,
    output_file="report.pdf",
    title="Project Report",
    output_dir="output_pdfs"
)
```

---

## 🏷️ Use Title Key as Section Header

```python
PDFGenerator.generate_pdf_from_dict(
    data,
    output_file="titled_report.pdf",
    title="Project Report",
    title_key="title"
)
```

---

## 🧩 Handling Complex Nested Data

```python
complex_data = [
    {
        "course_details": {
            "code": "CS101",
            "name": "Intro to AI"
        },
        "instructors": {
            "main_instructor": "Prof. Alice",
            "assistants": ["Mark", "Linda", "Tom"]
        },
        "schedule": {
            "begin": "2025-09-01",
            "finish": "2026-06-30",
            "modules": [
                {"topic": "Foundations", "period": "2025-Q3"},
                {"topic": "Machine Learning", "period": "2025-Q4"},
                {"topic": "Final Project", "period": "2026-Q2"}
            ]
        }
    }
]

PDFGenerator.generate_pdf_from_dict(
    complex_data,
    output_file="complex_report.pdf",
    title="Detailed Project Report",
    nested_table=True
)
```

---

## 📚 License

This project is licensed under the MIT License.

---

## 🤝 Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.