class MenuItem:
    def __init__(self, name, action=None):
        self.name = name
        self.action = action
        self.submenu = None

    def set_submenu(self, submenu):
        self.submenu = submenu

    def execute(self):
        if self.action:
            self.action()
        elif self.submenu:
            self.submenu.show_menu()

