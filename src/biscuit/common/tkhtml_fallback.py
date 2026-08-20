"""HtmlFrame compatibility shim.

tkinterweb's HtmlFrame requires the Tkhtml C extension, which has no
prebuilt binary for Tcl/Tk 9 (and is awkward to compile on some
platforms, e.g. Apple Silicon). To keep the editor runnable everywhere,
we expose a single `HtmlFrame` symbol:

- If tkinterweb + a working Tkhtml are available, we re-export the real one.
- Otherwise we provide a minimal stand-in backed by a plain tk.Text
  that degrades HTML to readable text, so every call site
  (.load_html / .add_css / .on_link_click / .yview / .html.* / .grid /
  .pack) keeps working without crashing the app.

The import alone is not enough to detect breakage: the tkinterweb
module imports fine even when Tkhtml is missing; the failure only
surfaces when an HtmlFrame is *instantiated* (it tries to load the
Tkhtml package into Tcl). So we probe instantiation before deciding.
"""

import re
import tkinter as tk

try:
    import tkinterweb  # noqa: F401  (must import for the probe below)
    from tkinterweb import HtmlFrame as _RealHtmlFrame

    # Probe: does constructing an HtmlFrame actually work here? On Tcl/Tk 9
    # without a compiled Tkhtml, the constructor raises a TclError.
    _probe = tk.Tk()
    try:
        _t = _RealHtmlFrame(_probe)
        HtmlFrame = _RealHtmlFrame
    finally:
        _probe.destroy()
        try:
            _t.destroy()
        except Exception:
            pass
except Exception:  # pragma: no cover - platform/Tk dependent
    HtmlFrame = None


if HtmlFrame is None:

    class HtmlFrame(tk.Frame):  # type: ignore[no-redef]
        """Minimal HtmlFrame replacement using a tk.Text widget."""

        def __init__(
            self, master=None, messages_enabled=True, vertical_scrollbar=True, **kwargs
        ):
            super().__init__(master, **kwargs)
            self._text = tk.Text(self, wrap=tk.WORD, state=tk.DISABLED)
            self._text.pack(fill=tk.BOTH, expand=True)
            # Call sites use self.html.config(...) and self.html.shrink(...).
            # Alias to ourselves so those calls hit the Frame/our shims.
            self.html = self
            self._link_cb = None

        def load_html(self, html, **kwargs):
            text = re.sub(r"<[^>]+>", "", html or "")
            self._text.config(state=tk.NORMAL)
            self._text.delete("1.0", tk.END)
            self._text.insert("1.0", text)
            self._text.config(state=tk.DISABLED)

        def add_css(self, css):
            # Styling is unsupported in the fallback; nothing to do.
            pass

        def on_link_click(self, callback):
            self._link_cb = callback

        def shrink(self, *args, **kwargs):
            pass

        def yview(self, *args, **kwargs):
            return self._text.yview(*args, **kwargs)
