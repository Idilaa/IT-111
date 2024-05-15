
def create_html_table(num_rows, num_cols, include_header=False):

    html = "<table>\n"
    
    # Add header row
    if include_header:
        html += "<thead>\n<tr>\n"
        for col in range(1, num_cols + 1):
            html += f"<th>Header {col}</th>\n"
        html += "</tr>\n</thead>\n"
    
    # Add table body
    html += "<tbody>\n"
    for row in range(1, num_rows + 1):
        html += "<tr>\n"
        for col in range(1, num_cols + 1):
            html += f"<td>Row {row}, Col {col}</td>\n"
        html += "</tr>\n"
    html += "</tbody>\n"
    
    html += "</table>"
    
    return html

# Example usage:
rows = 3
cols = 4
header = True
table_html = create_html_table(rows, cols, header)
print(table_html)