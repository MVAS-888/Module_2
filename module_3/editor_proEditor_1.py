class Editor:
    def view_document(self):
        print("Document is viewed.")

    def edit_document(self):
        print("Editing is unavailable in the free version.")


class ProEditor(Editor):
    def edit_document(self):
        print("Document is being edited.")


license_key = input("Enter license key: ")
if license_key == "PRO123":
    editor = ProEditor()
else:
    editor = Editor()

editor.view_document()
editor.edit_document()