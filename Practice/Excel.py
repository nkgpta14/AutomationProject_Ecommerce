import xlrd

wk = xlrd.open_workbook("C:/Users/nikhilg/Desktop/Results/TestData.xlsx")

print(wk.nsheets)

ws = wk.sheet_by_index(0)

n = ws.nrows
c = ws.ncols
print(n)
print(c)

for i in range (0,n):
    for j in range (0,c):
        wc = ws.cell(i,j)
        print(wc.value)