import os

import apt_pkg
import time
import gi

gi.require_version('Vte', '2.91')
gi.require_version('Gtk', '3.0')
from apt.progress.base import InstallProgress, AcquireProgress, OpProgress

from gi.repository import Vte, Gtk

TERMINAL_TIMEOUT = 4 * 60.0


class InstallProgressAdapter(InstallProgress):
    def __init__(self, progress, term, label, term_expander):
        InstallProgress.__init__(self)
        self.progress = progress
        self.term = term
        self.term_expander = term_expander
        self.finished = False
        self.action = label
        self.time_last_update = time.time()
        self.term.connect("child-exited", self.child_exited)
        self.env = ["VTE_PTY_KEEP_FD=%s" % self.writefd,
                    "DEBIAN_FRONTEND=gnome",
                    "APT_LISTCHANGES_FRONTEND=gtk"]

    def child_exited(self, term, status):
        # status = term.get_child_exit_status()
        # print "apt finished %s" % status
        # print "exit status: %s" % posix.WEXITSTATUS(status)
        # print "was signaled %s" % posix.WIFSIGNALED(status)
        self.apt_status = status
        self.finished = True

    def error(self, pkg, errormsg):
        # FIXME: display a msg
        self.term_expander.set_expanded(True)

    def conffile(self, current, new):
        # FIXME: display a msg or expand term
        self.term_expander.set_expanded(True)

    def start_update(self):
        # print "startUpdate"
        # apt_pkg.pkgsystem_unlock()
        # self.action.set_markup("<i>Installing dependencies...</i>")
        self.progress.set_fraction(0.0)
        self.progress.set_text("")

    def status_change(self, pkg, percent, status):
        # print "status change", pkg, percent, status
        self.progress.set_fraction(percent / 100.0)
        self.progress.set_text(status)
        self.time_last_update = time.time()

    def update_interface(self):
        InstallProgress.update_interface(self)
        # while Gtk.events_pending():
        #     Gtk.main_iteration()
        if (not self.term_expander.get_expanded() and
                    (self.time_last_update + TERMINAL_TIMEOUT) < time.time()):
            self.term_expander.set_expanded(True)
        # sleep just long enough to not create a busy loop
        time.sleep(0.01)

    def finish_update(self):
        self.progress.set_fraction(1)
        self.action.set_markup("Selesai")
        self.progress.set_text("")

    def fork(self):
        pty = Vte.Pty.new_sync(Vte.PtyFlags.DEFAULT,None)
        pid = os.fork()
        if pid == 0:
            # *grumpf* workaround bug in vte here (gnome bug #588871)
            for env in self.env:
                (key, value) = env.split("=")
                os.environ[key] = value
            # MUST be called
            pty.child_setup()
            # FIXME: close all fds expect for self.writefd
        else:
            self.term.set_pty(pty)
            self.term.watch_child(pid)
        return pid

    def wait_child(self):
        while not self.finished:
            self.update_interface()
        return self.apt_status


class FetchProgressAdapter(AcquireProgress):
    def __init__(self, progress, action, main):
        super(FetchProgressAdapter, self).__init__()
        self.progress = progress
        self.action = action
        self.main = main

    def start(self):
        super(FetchProgressAdapter, self).start()
        # self.action.set_markup("<i>Updating software list...</i>")
        self.progress.set_fraction(0)

    def stop(self):
        # print "stop()"
        pass

    def pulse(self, owner):
        super(FetchProgressAdapter, self).pulse(owner)
        at_item = min(self.current_items + 1, self.total_items)
        if self.current_cps > 0:
            self.progress.set_text(
                "File %s of %s at %sB/s" % (at_item, self.total_items, apt_pkg.size_to_str(self.current_cps)))
        else:
            self.progress.set_text("File %s of %s" % (at_item, self.total_items))
        self.progress.set_fraction(float(self.current_bytes) / self.total_bytes)
        print(float(self.current_bytes) / self.total_bytes)
        # while Gtk.events_pending():
        #     Gtk.main_iteration()
        return True

    def media_change(self, medium, drive):
        # print "mediaChange %s %s" % (medium, drive)
        msg = "Please insert '%s' into the drive '%s'" % (medium, drive)
        dialog = Gtk.MessageDialog(parent=self.main,
                                   flags=Gtk.DialogFlags.MODAL,
                                   type=Gtk.MessageType.QUESTION,
                                   buttons=Gtk.ButtonsType.OK_CANCEL)
        dialog.set_markup(msg)
        res = dialog.run()
        # print res
        dialog.destroy()
        if res == Gtk.ResponseType.OK:
            return True

        return False

class CacheProgressAdapter(OpProgress):
    def __init__(self, progressbar):
        self.progressbar = progressbar
    def update(self, percent=None):
        self.progressbar.show()
        if percent:
            self.progressbar.set_fraction(percent/100.0)
        #self.progressbar.set_text(self.op)
        while Gtk.events_pending():
            Gtk.main_iteration()
    def done(self):
        self.progressbar.hide()


if __name__ == "__main__":
    from gi.repository import Gtk, Vte, Gio, GObject, GLib

    def update_cache(job, cancellable, data):
        import apt
        cache = apt.Cache()
        cache["firefox"].mark_install()
        cache.commit(data[0], data[1])

    GObject.threads_init()

    window = Gtk.Window(title="Test adapter")
    box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
    window.add(box)

    label = Gtk.Label(label="Empty label")
    box.pack_start(label, 1, 1, 10)

    progressbar = Gtk.ProgressBar()
    progressbar.set_show_text(True)
    box.pack_start(progressbar, 1, 1, 10)

    vte = Vte.Terminal()
    vte.set_size_request(800, 250)

    expander = Gtk.Expander(label="tampilkan")
    expander.add(vte)
    box.pack_start(expander, 1, 1, 10)


    window.connect("delete-event", Gtk.main_quit)
    window.show_all()

    fprogress = FetchProgressAdapter(progressbar,label, window)
    iprogress = InstallProgressAdapter(progressbar, vte, label,expander)

    Gio.io_scheduler_push_job(update_cache,
                              (fprogress, iprogress),
                              GLib.PRIORITY_DEFAULT,
                              None)
    Gtk.main()