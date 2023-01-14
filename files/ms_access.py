import win32com.client as win

try:
    access = win.Dispatch('Access.Application')
    db = access.OpenCurrentDatabase(r'D:\center\database\Q-H.S.E_RB.accdb')
        

    access.DoCmd.OpenForms(formname)

    # RUN BUTTON CLICK EVENT (OPEN PARENTHESES REQUIRED)
    access.Forms(formname).myButton_Click()

    access.Visible = True

except Exception as e:
    print(e)
    access.DoCmd.CloseDatabase()
    access.Quit()

finally:
    db = None; access = None
    del db; del access