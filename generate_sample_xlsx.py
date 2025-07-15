from openpyxl import Workbook

wb = Workbook()
ws = wb.active
ws.title = "Sheet1"

ws.append(["Name", "Value", "Date"])
ws.append(["Temperature", 34.5, "2025-07-15"])
ws.append(["Humidity", 78, "2025-07-15"])

wb.save("data_ingestion/docs/sample.xlsx")
