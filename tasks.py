from robocorp.excel import open_workbook
from robocorp.tasks import task
from robocorp import workitems


@task
def producer():
    """Split Excel rows into multiple output Work Items for the next step."""
    for item in workitems.inputs:
        path = item.download_file("orders.xlsx")
        orders = open_workbook(path).worksheet(0).as_table(header=True)

        for row in orders:
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
