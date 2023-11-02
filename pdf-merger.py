import PyPDF2

def merge_pdfs(pdf_list, output_filename, merge_order=None):
    pdf_merger = PyPDF2.PdfFileMerger()

    try:
        if merge_order:
            for index in merge_order:
                pdf_merger.append(pdf_list[index])
        else:
            for pdf in pdf_list:
                pdf_merger.append(pdf)

        pdf_merger.write(output_filename)
        pdf_merger.close()
        print(f"Merged {len(pdf_list)} PDFs into {output_filename}")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

# List of PDF files to merge
pdf_files = ["file1.pdf", "file2.pdf", "file3.pdf"]

# Output filename for the merged PDF
output_pdf = "merged.pdf"

# Specify the order of merging (e.g., merge in the order [1, 2, 0])
merge_order = [1, 2, 0]

merge_pdfs(pdf_files, output_pdf, merge_order)
