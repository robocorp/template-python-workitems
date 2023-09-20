from robocorp.tasks import task
from robocorp import workitems
import os

from RPA.Excel.Files import Files as Excel


@task
def producer():
    """Split Excel rows into multiple output Work Items for the next step."""
    for item in workitems.inputs:
        output_directory = os.environ.get("ROBOT_ARTIFACTS")
        name = "orders.xlsx"
        path = item.get_file(name, os.path.join(output_directory, name))

        excel = Excel()
        excel.open_workbook(path)
        rows = excel.read_worksheet_as_table(header=True)

        for row in rows:
            payload = {
                "Name": row["Name"],
                "Zip": row["Zip"],
                "Product": row["Item"],
            }
            workitems.outputs.create(payload)


@task
def consumer():
    """Process all the produced input Work Items from the previous step."""
    for item in workitems.inputs:
        try:
            name = item.payload["Name"]
            address = item.payload["Zip"]
            product = item.payload["Product"]
            print(f"Processing order: {name}, {address}, {product}")
            item.done()
        except KeyError as err:
            item.fail(code="MISSING_VALUE", message=str(err))
