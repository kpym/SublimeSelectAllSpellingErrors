import sublime, sublime_plugin

class SelectAllSpellingErrorsCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        regions = []
        while True:
            self.view.run_command('next_misspelling')
            if self.view.sel()[0] not in regions:
                regions.append(self.view.sel()[0])
            else:
                break
        self.view.sel().clear()
        self.view.sel().add_all(regions)
