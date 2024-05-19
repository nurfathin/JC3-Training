import pdfplumber
import pandas as pd

def extract_tables_from_pdf(pdf_path, start_page, end_page):
    tables = []
    with pdfplumber.open(pdf_path) as pdf:
        for page_number in range(start_page, end_page + 1):
            page = pdf.pages[page_number - 1]  # Pages are 0-indexed
            extracted_tables = page.extract_tables()
            tables.extend(extracted_tables)
    return tables

def remove_table_headers(tables, header_rows=3):
    tables_without_headers = []
    for table in tables:
        if len(table) > header_rows:
            tables_without_headers.append(table[header_rows:])  # Exclude the first three rows (header)
    return tables_without_headers

def compile_tables_into_dataframe(tables):
    compiled_table = []
    for table in tables:
        compiled_table.extend(table)
    return pd.DataFrame(compiled_table)

def save_tables_to_excel(tables, excel_path):
    with pd.ExcelWriter(excel_path) as writer:
        df = compile_tables_into_dataframe(tables)
        df.to_excel(writer, sheet_name='Data 2020', index=False, header=False)

pdf_path = (r"C:\Users\Desktop\LBT2020.pdf")
start_page = 173
end_page = 239 #you need to add one more page the end page

tables = extract_tables_from_pdf(pdf_path, start_page, end_page)
tables_without_headers = remove_table_headers(tables)
save_tables_to_excel(tables_without_headers, r"C:\Users\Dekstop\LBT2020.xlsx")

print("Data has been saved.")
