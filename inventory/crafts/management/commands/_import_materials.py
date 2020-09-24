import csv


field_mapping = {
    'Code': 'sku',
    'Article': 'name',
    'Size': 'size',
    'N of pcs': 'units_per_package',
    'Price (€)': 'price_per_package',
    'Source': 'source',
    'Notes': 'memo',
}


def sanitize(model_field, orig_value):
    if model_field == 'price_per_package':
        return float(orig_value[1:].replace(',', '.'))

    return orig_value


class AdaptedRow:
    def __init__(self, row):
        self.orig = row.copy()
        self.row = {}
        for csv_field, model_field in field_mapping.items():
            if csv_field in row:
                orig_value = row[csv_field]
                self.row[model_field] = {
                    'sanitized_value': sanitize(model_field, orig_value),
                    'orig_value': orig_value,
                    'csv_field': csv_field,
                }

    def print_debug(self):
        print(self.orig)
        for k, v in self.row.items():
            print(f"{k} = {v}")
        print()


def is_valid_row(row):
    return row['Code'] != ''


def rows_from_csv(path):
    with open(path) as fh:
        reader = csv.DictReader(fh, delimiter=';')
        for row in reader:
            if is_valid_row(row):
                yield AdaptedRow(row)
