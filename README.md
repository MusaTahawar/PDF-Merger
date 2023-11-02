# Advanced PDF Merging Script

This is a Python script that uses the `PyPDF2` library to merge multiple PDF files into a single PDF document. The script allows you to specify the order in which the PDFs are merged and provides robust error handling.

## Getting Started

To run this script, you need to have Python and the `PyPDF2` library installed on your system.

1. **Clone the repository** to your local machine:

    ```shell
    git clone https://github.com/yourusername/advanced-pdf-merger.git
    cd advanced-pdf-merger
    ```

2. **Run the script**:

    ```shell
    python merge_pdfs.py
    ```

The script will merge the PDF files as specified and save the merged PDF as "merged.pdf" by default.

## Features

- **PDF Merging:** Merge multiple PDF files into a single PDF document.
- **Custom Merge Order:** Specify the order in which the PDFs are merged by providing a custom merge order.
- **Robust Error Handling:** The script includes error handling to gracefully handle any issues that may arise during the merging process.

## Usage

### Basic Usage

To merge PDFs in the order they appear in the `pdf_files` list:

```python
# List of PDF files to merge
pdf_files = ["file1.pdf", "file2.pdf", "file3.pdf"]

# Output filename for the merged PDF
output_pdf = "merged.pdf"

merge_pdfs(pdf_files, output_pdf)


Custom Merge Order
To specify a custom order for merging the PDFs, provide a list of indices in the merge_order parameter:

python
Copy code
# Specify the order of merging (e.g., merge in the order [1, 2, 0])
merge_order = [1, 2, 0]

merge_pdfs(pdf_files, output_pdf, merge_order)
