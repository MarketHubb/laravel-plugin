import sublime
import sublime_plugin



class LaravelPlugin(sublime_plugin.EventListener):
    def __init__(self):
        self._controller_list = []
        self._view_list = []   
    def on_query_completions(self, view, prefix, locations):
        if prefix == '':
            return [], sublime.INHIBIT_COMPLETION

        completions = []
        for word in ['controller', 'model', 'view']:
            if word.startswith(prefix.lower()):
                completions.append((word, word))

        return completions, sublime.INHIBIT_COMPLETION

	def on_text_command(self, view, command_name, args):
	        if command_name == 'laravel_jump_to_controller':
	            self.jump_to_controller(view)
	            return sublime.INHIBIT_DEFAULT

	        elif command_name == 'laravel_jump_to_view':
	            self.jump_to_view(view)
	            return sublime.INHIBIT_DEFAULT
    
    def jump_to_controller(self, view):
        current_file = view.file_name()
        controller_path = os.path.join(os.path.dirname(current_file), 'app/Http/Controllers')
        controller_name = os.path.basename(current_file).replace('.php', '')
        controller_file = os.path.join(controller_path, f'{controller_name}Controller.php')
        self.jump_to_file(view, controller_file)

    def jump_to_view(self, view):
        current_file = view.file_name()
        view_path = os.path.join(os.path.dirname(current_file), 'resources/views')
        view_name = os.path.basename(current_file).replace('.php', '')
        view_file = os.path.join(view_path, f'{view_name}.blade.php')
        self.jump_to_file(view, view_file)

    def jump_to_file(self, view, file_path):
        sublime.active_window().open_file(file_path)