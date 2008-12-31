""" @package MarkdownMacro
    @file macro.py
    @brief The markdownMacro class

    Implements Markdown syntax WikiProcessor as a Trac macro.
    
    From Markdown.py by Alex Mizrahi aka killer_storm
    See: http://trac-hacks.org/attachment/ticket/353/Markdown.py
    Get Python Markdown from: http://www.freewisdom.org/projects/python-markdown/

    @author Douglas Clifton <dwclifton@gmail.com>
    @date December, 2008
    @version 0.11.0
"""

from trac.core import *
from trac.wiki.macros import WikiMacroBase
from trac.wiki.formatter import Formatter

from re import sub, compile, search, I
from StringIO import StringIO

from markdown import markdown

# links, autolinks, and reference-style links

LINK = compile(
    r'(\]\()([^) ]+)([^)]*\))|(<)([^>]+)(>)|(\n\[[^]]+\]: *)([^ \n]+)(.*\n)'
)
HREF = compile(r'href=[\'"]?([^\'" ]*)')

__all__ = ['MarkdownMacro']

class MarkdownMacro(WikiMacroBase):
    """Implements Markdown syntax [WikiProcessors WikiProcessor] as a Trac macro."""

    def expand_macro(self, formatter, name, content):

        env = formatter.env
        abs = env.abs_href.base
        abs = abs[:len(abs) - len(env.href.base)]
        f = Formatter(formatter.env, formatter.context)
        
        def convert(m):
            pre, target, suf = filter(None, m.groups())
            out = StringIO()
            f.format(target, out)
            url = search(
                    HREF,
                    out.getvalue(),
                    I).groups()[0]
            # Trac creates relative links, which Markdown won't touch inside
            # <autolinks> because they look like HTML
            if pre == '<' and url != target:
               pre += abs
            return pre + str(url) + suf
            
        return markdown(sub(LINK, convert, content))
