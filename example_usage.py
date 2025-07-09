from pdf_generator import PDFGenerator, DEFAULT_STYLES
import pandas as pd
import numpy as np

custom_styles = {
    'table_title': {
        'font_size': 18,
        'space_after': 20,
        'text_transform': 'capitalize'
    },
    'cell': {
        'word_wrap': False,
        'leading': 17
    }
}
# Example usage with different dictionary structures
data = [
    {
        "id": "P1001",
        "title": "Urban Air Quality Study",
        "status": "active",
        "timeframe": {
            "start": "2023-01-15",
            "end": "2023-12-31"
        },
        "budget": "$120,000",
        "lead_researcher": {
            "name": "Dr. Sarah Chen",
            "department": "Environmental Science"
        }
    },
    {
        "id": "P1002",
        "title": "Renewable Energy Optimization",
        "status": "planning",
        "timeframe": {
            "start": "2023-03-01",
            "end": "2024-02-28"
        },
        "budget": "$85,000",
        "lead_researcher": {
            "name": "Prof. James Wilson",
            "department": "Engineering"
        }
    },
    {
        "id": "P1003",
        "title": "Coastal Erosion Analysis",
        "status": "completed",
        "timeframe": {
            "start": "2022-06-01",
            "end": "2023-01-30"
        },
        "budget": "$65,000",
        "lead_researcher": {
            "name": "Dr. Maria Garcia",
            "department": "Geology"
        }
    },
    {
        "id": "P1004",
        "title": "AI for Medical Diagnostics",
        "status": "active",
        "timeframe": {
            "start": "2023-02-10",
            "end": "2024-06-15"
        },
        "budget": "$210,000",
        "lead_researcher": {
            "name": "Dr. Alan Turing",
            "department": "Computer Science"
        }
    },
    {
        "id": "P1005",
        "title": "Nanomaterials for Solar Cells",
        "status": "active",
        "timeframe": {
            "start": "2022-11-01",
            "end": "2023-10-31"
        },
        "budget": "$175,000",
        "lead_researcher": {
            "name": "Dr. Lisa Zhang",
            "department": "Materials Science"
        }
    },
    {
        "id": "P1006",
        "title": "Behavioral Economics Study",
        "status": "completed",
        "timeframe": {
            "start": "2021-09-01",
            "end": "2022-08-31"
        },
        "budget": "$92,000",
        "lead_researcher": {
            "name": "Dr. Robert Kahn",
            "department": "Economics"
        }
    },
    {
        "id": "P1007",
        "title": "Antibiotic Resistance Research",
        "status": "active",
        "timeframe": {
            "start": "2023-04-01",
            "end": "2025-03-31"
        },
        "budget": "$340,000",
        "lead_researcher": {
            "name": "Dr. Emma Watson",
            "department": "Microbiology"
        }
    },
    {
        "id": "P1008",
        "title": "Smart City Infrastructure",
        "status": "planning",
        "timeframe": {
            "start": "2024-01-01",
            "end": "2026-12-31"
        },
        "budget": "$500,000",
        "lead_researcher": {
            "name": "Dr. Mark Lee",
            "department": "Urban Planning"
        }
    },
    {
        "id": "P1009",
        "title": "Quantum Computing Algorithms",
        "status": "active",
        "timeframe": {
            "start": "2022-07-01",
            "end": "2024-06-30"
        },
        "budget": "$275,000",
        "lead_researcher": {
            "name": "Dr. Priya Patel",
            "department": "Physics"
        }
    },
    {
        "id": "P1010",
        "title": "Marine Biodiversity Catalog",
        "status": "completed",
        "timeframe": {
            "start": "2020-05-01",
            "end": "2022-04-30"
        },
        "budget": "$150,000",
        "lead_researcher": {
            "name": "Dr. Carlos Mendez",
            "department": "Marine Biology"
        }
    }
]

# Generate PDF (horizontal layout)
PDFGenerator.generate_pdf_from_dict(
    data,
    output_file="dataframe_horizontal1.pdf",
    title="Research Projects",
    layout="horizontal",
    output_dir="output_pdfs",  # Specify output directory
    title_key="title",  # Use Name column as entry titles
    styles=custom_styles
)

# Generate PDF (vertical layout)
PDFGenerator.generate_pdf_from_dict(
    data,
    output_file="dataframe_vertical_recursive.pdf",
    title="Research Projects",
    layout="vertical",
    output_dir="output_pdfs",  # Specify output directory
    styles=custom_styles
)
