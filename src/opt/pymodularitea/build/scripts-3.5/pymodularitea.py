#!/usr/bin/python3

from modularitea.progress_adapter import FetchProgressAdapter
from modularitea.module import Module
from optparse import OptionParser

import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, Gio, GObject, GLib, Vte

parser = OptionParser()
parser.add_option("-m", "--module", dest="module")

(option, args) = parser.parse_args()

class Modularitea:
    def __init__(self):
        GObject.threads_init()

        self.ui = Gtk.Builder.new_from_file('/usr/share/modularitea/modularitea.ui')
        self.window = self.ui.get_object('main_window')
        self.action_label = self.ui.get_object('current_action')
        self.progressbar = self.ui.get_object('progressbar')
        self.expander = self.ui.get_object('expander')
        self.cancel_button = self.ui.get_object('cancel_button')
        self.terminal = Vte.Terminal()
        self.cancellable = Gio.Cancellable()

        self.terminal.set_visible(True)
        self.terminal.set_size(60, 20)
        self.expander.add(self.terminal)
        self.expander.hide()
        self.terminal.set_size_request(300,200)

        #connecting signals
        self.cancel_button.connect("clicked", Gtk.main_quit)
        self.window.connect("delete-event", Gtk.main_quit)


        Gio.io_scheduler_push_job(
            self.download,
            None,
            GLib.PRIORITY_DEFAULT,
            None
        )



    def download(self, job, cancellable, user_data):
        self.module_name = option.module
        self.module_object = Module(
            self.module_name,
            self.progressbar,
            self.action_label,
            self.terminal,
            self.expander
        )
        self.module_object.download_apt(self.window)
        self.module_object.download_archive()
        self.expander.show_all()
        self.module_object.install_apt(self.window)
        self.module_object.install_archives()


modularitea = Modularitea()
modularitea.window.show()
Gtk.main()