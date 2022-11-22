def maketableof(table: list) -> None:
    """Print  as a table.
    
    Params
        table(list) : The data for the table to be printed
    >>> print_table([[1, 2, 3], [41, 0, 1]])
     1  2  3
    41  0  1
    """
    table = [[str(cell) for cell in row] for row in table]
    column_widths = [len(cell) for cell in table[0]]
    for row in table:
        for x, cell in enumerate(row):
            column_widths[x] = max(column_widths[x], len(cell))

    formatters = []
    for width in column_widths:
        formatters.append("{:>" + str(width) + "}")
    formatter = "  ".join(formatters)
    for row in table:
        print(formatter.format(*row))
