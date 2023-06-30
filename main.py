from prettytable import PrettyTable

x = PrettyTable()

x.field_names = ["Names", "Reg Number", "Department", "Faculty"]
x.add_rows(
  [
    ["Damian", "20201208492", "Computer Science", "School of information and communication technology"],
    ["Okpala", "20202636264", "Computer Science", "School of information and communication technology"]
  ]
)
print(x)