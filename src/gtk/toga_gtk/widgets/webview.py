from toga_gtk.libs import Gtk, WebKit2

from .base import Widget
from ..keys import gtk_to_key


class WebView(Widget):
    """ GTK WebView implementation.

    TODO: WebView is not displaying anything when setting a url.
    """

    def create(self):
        if WebKit2 is None:
            raise RuntimeError(
                "Import 'from gi.repository import WebKit' failed;" +
                " may need to install gir1.2-webkit2-4.0 or gir1.2-webkit2-3.0.")

        self.native = Gtk.ScrolledWindow()
        self.native.set_policy(Gtk.PolicyType.AUTOMATIC, Gtk.PolicyType.AUTOMATIC)
        self.native.interface = self.interface

        self.webview = WebKit2.WebView()

        self.native.add(self.webview)
        self.native.set_min_content_width(200)
        self.native.set_min_content_height(200)

        def on_key(widget, event, *args):
            keyval = gtk_to_key(event.keyval)
            if keyval:
                self.interface.on_key_down(keyval, event.state)
        self.webview.connect('key-press-event', on_key)

        # self.native.connect('show', lambda event: self.rehint())

    def set_url(self, value):
        if value:
            self.webview.load_uri(self.interface.url)

    def set_user_agent(self, value):
        self.interface.factory.not_implemented('Window.info_dialog()')
        # self.native.user_agent = value if value else "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.101 Safari/537.36"

    def set_content(self, root_url, content):
        self.webview.load_html(content, root_url)

    def get_dom(self):
        self.interface.factory.not_implemented('WebView.get_dom()')

    def evaluate(self, javascript):
        return self.webview.run_javascript(javascript, None, None, None)
