from typing import TypeAlias, Any, Callable, TYPE_CHECKING
from .styles import Style

if TYPE_CHECKING:
    from .signals import Signal
    from .refs import Ref

WebElementChild: TypeAlias = "WebElement | str | int | tuple[WebElementChild, ...] | Signal[Any] | Ref[Any] | Callable[[], WebElementChild] | None"
WebElementAttributeValue: TypeAlias = "str | bool | Style | Callable[..., None]"
WebElementAttributes: TypeAlias = "dict[str, WebElementAttributeValue]"

# def children_equal(child: WebElementChild, child2: WebElementChild):
#     if (type(child) == str or type(child) == int) and (type(child2) != type(child) or child != child2):
#         return False

#     if isinstance(child, Signal) and (not isinstance(child2, Signal) or child.get() != child2.get()):
#         return False

#     if isinstance(child, Ref) and (not isinstance(child2, Ref) or child.get() != child2.get()):
#         return False

#     if callable(child) and id(child) != id(child2):
#         return False

#     if child is None and child2 is not None:
#         return False

#     if isinstance(child, WebElement) and (not isinstance(child2, WebElement) or not child.equals(child2)):
#         return False
    
#     if type(child) == tuple:
#         if type(child2) != tuple: return False
#         # pyright wont shut up
#         if callable(child) or callable(child2): return False
#         if len(child) != len(child2): return False

#         for i in range(len(child)):
#             if children_equal(child[i], child2[i]):
#                 return False
    
#     return True

class WebElement:
    def __init__(self, typeof: str, children: tuple[WebElementChild, ...], attributes: WebElementAttributes) -> None:
        self.type = typeof
        self.children = children
        self.attributes = attributes

    #
    # Replaced by dumber diffing method.
    #
    # def equals(self, other: "WebElement") -> bool:
    #     if self.type != other.type:
    #         return False
        
    #     if len(self.attributes) != len(other.attributes):
    #         return False
        
    #     for attr_name, attr_value in self.attributes.items():
    #         if attr_name not in other.attributes:
    #             return False
            
    #         other_value = other.attributes[attr_name]

    #         if (type(attr_value) == str or type(attr_value) == int) and (type(other_value) != type(attr_value) or other_value != attr_value):
    #             return False
            
    #         if isinstance(attr_value, Style) and (not isinstance(other_value, Style) or attr_value.style_text != other_value.style_text):
    #             return False
            
    #         if callable(attr_value) and (not callable(other_value) or id(attr_value) != id(other_value)):
    #             return False

    #     if len(self.children) != len(other.children):
    #         return False
        
    #     return children_equal(self.children, other.children)

def html(*children: WebElementChild, **attributes: WebElementAttributeValue): return WebElement("html", children, attributes)
def base(*children: WebElementChild, **attributes: WebElementAttributeValue): return WebElement("base", children, attributes)
def head(*children: WebElementChild, **attributes: WebElementAttributeValue): return WebElement("head", children, attributes)
def link(*children: WebElementChild, **attributes: WebElementAttributeValue): return WebElement("link", children, attributes)
def meta(*children: WebElementChild, **attributes: WebElementAttributeValue): return WebElement("meta", children, attributes)
def script(*children: WebElementChild, **attributes: WebElementAttributeValue): return WebElement("script", children, attributes)
def style(*children: WebElementChild, **attributes: WebElementAttributeValue): return WebElement("style", children, attributes)
def title(*children: WebElementChild, **attributes: WebElementAttributeValue): return WebElement("title", children, attributes)
def body(*children: WebElementChild, **attributes: WebElementAttributeValue): return WebElement("body", children, attributes)
def address(*children: WebElementChild, **attributes: WebElementAttributeValue): return WebElement("address", children, attributes)
def article(*children: WebElementChild, **attributes: WebElementAttributeValue): return WebElement("article", children, attributes)
def aside(*children: WebElementChild, **attributes: WebElementAttributeValue): return WebElement("aside", children, attributes)
def footer(*children: WebElementChild, **attributes: WebElementAttributeValue): return WebElement("footer", children, attributes)
def header(*children: WebElementChild, **attributes: WebElementAttributeValue): return WebElement("header", children, attributes)
def h1(*children: WebElementChild, **attributes: WebElementAttributeValue): return WebElement("h1", children, attributes)
def h2(*children: WebElementChild, **attributes: WebElementAttributeValue): return WebElement("h2", children, attributes)
def h3(*children: WebElementChild, **attributes: WebElementAttributeValue): return WebElement("h3", children, attributes)
def h4(*children: WebElementChild, **attributes: WebElementAttributeValue): return WebElement("h4", children, attributes)
def h5(*children: WebElementChild, **attributes: WebElementAttributeValue): return WebElement("h5", children, attributes)
def h6(*children: WebElementChild, **attributes: WebElementAttributeValue): return WebElement("h6", children, attributes)
def hgroup(*children: WebElementChild, **attributes: WebElementAttributeValue): return WebElement("hgroup", children, attributes)
def main(*children: WebElementChild, **attributes: WebElementAttributeValue): return WebElement("main", children, attributes)
def nav(*children: WebElementChild, **attributes: WebElementAttributeValue): return WebElement("nav", children, attributes)
def section(*children: WebElementChild, **attributes: WebElementAttributeValue): return WebElement("section", children, attributes)
def blockquote(*children: WebElementChild, **attributes: WebElementAttributeValue): return WebElement("blockquote", children, attributes)
def cite(*children: WebElementChild, **attributes: WebElementAttributeValue): return WebElement("cite", children, attributes)
def dd(*children: WebElementChild, **attributes: WebElementAttributeValue): return WebElement("dd", children, attributes)
def dt(*children: WebElementChild, **attributes: WebElementAttributeValue): return WebElement("dt", children, attributes)
def dl(*children: WebElementChild, **attributes: WebElementAttributeValue): return WebElement("dl", children, attributes)
def div(*children: WebElementChild, **attributes: WebElementAttributeValue): return WebElement("div", children, attributes)
def figcaption(*children: WebElementChild, **attributes: WebElementAttributeValue): return WebElement("figcaption", children, attributes)
def figure(*children: WebElementChild, **attributes: WebElementAttributeValue): return WebElement("figure", children, attributes)
def hr(*children: WebElementChild, **attributes: WebElementAttributeValue): return WebElement("hr", children, attributes)
def li(*children: WebElementChild, **attributes: WebElementAttributeValue): return WebElement("li", children, attributes)
def ol(*children: WebElementChild, **attributes: WebElementAttributeValue): return WebElement("ol", children, attributes)
def ul(*children: WebElementChild, **attributes: WebElementAttributeValue): return WebElement("ul", children, attributes)
def menu(*children: WebElementChild, **attributes: WebElementAttributeValue): return WebElement("menu", children, attributes)
def p(*children: WebElementChild, **attributes: WebElementAttributeValue): return WebElement("p", children, attributes)
def pre(*children: WebElementChild, **attributes: WebElementAttributeValue): return WebElement("pre", children, attributes)
def a(*children: WebElementChild, **attributes: WebElementAttributeValue): return WebElement("a", children, attributes)
def abbr(*children: WebElementChild, **attributes: WebElementAttributeValue): return WebElement("abbr", children, attributes)
def b(*children: WebElementChild, **attributes: WebElementAttributeValue): return WebElement("b", children, attributes)
def bdi(*children: WebElementChild, **attributes: WebElementAttributeValue): return WebElement("bdi", children, attributes)
def bdo(*children: WebElementChild, **attributes: WebElementAttributeValue): return WebElement("bdo", children, attributes)
def br(*children: WebElementChild, **attributes: WebElementAttributeValue): return WebElement("br", children, attributes)
def code(*children: WebElementChild, **attributes: WebElementAttributeValue): return WebElement("code", children, attributes)
def data(*children: WebElementChild, **attributes: WebElementAttributeValue): return WebElement("data", children, attributes)
def dfn(*children: WebElementChild, **attributes: WebElementAttributeValue): return WebElement("dfn", children, attributes)
def em(*children: WebElementChild, **attributes: WebElementAttributeValue): return WebElement("em", children, attributes)
def i(*children: WebElementChild, **attributes: WebElementAttributeValue): return WebElement("i", children, attributes)
def kbd(*children: WebElementChild, **attributes: WebElementAttributeValue): return WebElement("kbd", children, attributes)
def mark(*children: WebElementChild, **attributes: WebElementAttributeValue): return WebElement("mark", children, attributes)
def q(*children: WebElementChild, **attributes: WebElementAttributeValue): return WebElement("q", children, attributes)
def rp(*children: WebElementChild, **attributes: WebElementAttributeValue): return WebElement("rp", children, attributes)
def ruby(*children: WebElementChild, **attributes: WebElementAttributeValue): return WebElement("ruby", children, attributes)
def rt(*children: WebElementChild, **attributes: WebElementAttributeValue): return WebElement("rt", children, attributes)
def s(*children: WebElementChild, **attributes: WebElementAttributeValue): return WebElement("s", children, attributes)
def samp(*children: WebElementChild, **attributes: WebElementAttributeValue): return WebElement("samp", children, attributes)
def small(*children: WebElementChild, **attributes: WebElementAttributeValue): return WebElement("small", children, attributes)
def span(*children: WebElementChild, **attributes: WebElementAttributeValue): return WebElement("span", children, attributes)
def strong(*children: WebElementChild, **attributes: WebElementAttributeValue): return WebElement("strong", children, attributes)
def sub(*children: WebElementChild, **attributes: WebElementAttributeValue): return WebElement("sub", children, attributes)
def sup(*children: WebElementChild, **attributes: WebElementAttributeValue): return WebElement("sup", children, attributes)
def time(*children: WebElementChild, **attributes: WebElementAttributeValue): return WebElement("time", children, attributes)
def u(*children: WebElementChild, **attributes: WebElementAttributeValue): return WebElement("u", children, attributes)
def var(*children: WebElementChild, **attributes: WebElementAttributeValue): return WebElement("var", children, attributes)
def wbr(*children: WebElementChild, **attributes: WebElementAttributeValue): return WebElement("wbr", children, attributes)
def area(*children: WebElementChild, **attributes: WebElementAttributeValue): return WebElement("area", children, attributes)
def audio(*children: WebElementChild, **attributes: WebElementAttributeValue): return WebElement("audio", children, attributes)
def img(*children: WebElementChild, **attributes: WebElementAttributeValue): return WebElement("img", children, attributes)
def map(*children: WebElementChild, **attributes: WebElementAttributeValue): return WebElement("map", children, attributes)
def track(*children: WebElementChild, **attributes: WebElementAttributeValue): return WebElement("track", children, attributes)
def video(*children: WebElementChild, **attributes: WebElementAttributeValue): return WebElement("video", children, attributes)
def embed(*children: WebElementChild, **attributes: WebElementAttributeValue): return WebElement("embed", children, attributes)
def iframe(*children: WebElementChild, **attributes: WebElementAttributeValue): return WebElement("iframe", children, attributes)
def object(*children: WebElementChild, **attributes: WebElementAttributeValue): return WebElement("object", children, attributes)
def picture(*children: WebElementChild, **attributes: WebElementAttributeValue): return WebElement("picture", children, attributes)
def source(*children: WebElementChild, **attributes: WebElementAttributeValue): return WebElement("source", children, attributes)
def portal(*children: WebElementChild, **attributes: WebElementAttributeValue): return WebElement("portal", children, attributes)
def svg(*children: WebElementChild, **attributes: WebElementAttributeValue): return WebElement("svg", children, attributes)
def canvas(*children: WebElementChild, **attributes: WebElementAttributeValue): return WebElement("canvas", children, attributes)
def noscript(*children: WebElementChild, **attributes: WebElementAttributeValue): return WebElement("noscript", children, attributes)
def del_(*children: WebElementChild, **attributes: WebElementAttributeValue): return WebElement("del", children, attributes)
def ins(*children: WebElementChild, **attributes: WebElementAttributeValue): return WebElement("ins", children, attributes)
def caption(*children: WebElementChild, **attributes: WebElementAttributeValue): return WebElement("caption", children, attributes)
def col(*children: WebElementChild, **attributes: WebElementAttributeValue): return WebElement("col", children, attributes)
def colgroup(*children: WebElementChild, **attributes: WebElementAttributeValue): return WebElement("colgroup", children, attributes)
def table(*children: WebElementChild, **attributes: WebElementAttributeValue): return WebElement("table", children, attributes)
def tbody(*children: WebElementChild, **attributes: WebElementAttributeValue): return WebElement("tbody", children, attributes)
def tr(*children: WebElementChild, **attributes: WebElementAttributeValue): return WebElement("tr", children, attributes)
def td(*children: WebElementChild, **attributes: WebElementAttributeValue): return WebElement("td", children, attributes)
def tfoot(*children: WebElementChild, **attributes: WebElementAttributeValue): return WebElement("tfoot", children, attributes)
def th(*children: WebElementChild, **attributes: WebElementAttributeValue): return WebElement("th", children, attributes)
def thead(*children: WebElementChild, **attributes: WebElementAttributeValue): return WebElement("thead", children, attributes)
def button(*children: WebElementChild, **attributes: WebElementAttributeValue): return WebElement("button", children, attributes)
def datalist(*children: WebElementChild, **attributes: WebElementAttributeValue): return WebElement("datalist", children, attributes)
def option(*children: WebElementChild, **attributes: WebElementAttributeValue): return WebElement("option", children, attributes)
def fieldset(*children: WebElementChild, **attributes: WebElementAttributeValue): return WebElement("fieldset", children, attributes)
def label(*children: WebElementChild, **attributes: WebElementAttributeValue): return WebElement("label", children, attributes)
def form(*children: WebElementChild, **attributes: WebElementAttributeValue): return WebElement("form", children, attributes)
def input(*children: WebElementChild, **attributes: WebElementAttributeValue): return WebElement("input", children, attributes)
def legend(*children: WebElementChild, **attributes: WebElementAttributeValue): return WebElement("legend", children, attributes)
def meter(*children: WebElementChild, **attributes: WebElementAttributeValue): return WebElement("meter", children, attributes)
def optgroup(*children: WebElementChild, **attributes: WebElementAttributeValue): return WebElement("optgroup", children, attributes)
def select(*children: WebElementChild, **attributes: WebElementAttributeValue): return WebElement("select", children, attributes)
def output(*children: WebElementChild, **attributes: WebElementAttributeValue): return WebElement("output", children, attributes)
def progress(*children: WebElementChild, **attributes: WebElementAttributeValue): return WebElement("progress", children, attributes)
def textarea(*children: WebElementChild, **attributes: WebElementAttributeValue): return WebElement("textarea", children, attributes)
def details(*children: WebElementChild, **attributes: WebElementAttributeValue): return WebElement("details", children, attributes)
def summary(*children: WebElementChild, **attributes: WebElementAttributeValue): return WebElement("summary", children, attributes)
def dialog(*children: WebElementChild, **attributes: WebElementAttributeValue): return WebElement("dialog", children, attributes)
def slot(*children: WebElementChild, **attributes: WebElementAttributeValue): return WebElement("slot", children, attributes)
def template(*children: WebElementChild, **attributes: WebElementAttributeValue): return WebElement("template", children, attributes)
def acronym(*children: WebElementChild, **attributes: WebElementAttributeValue): return WebElement("acronym", children, attributes)
def applet(*children: WebElementChild, **attributes: WebElementAttributeValue): return WebElement("applet", children, attributes)
def bgsound(*children: WebElementChild, **attributes: WebElementAttributeValue): return WebElement("bgsound", children, attributes)
def big(*children: WebElementChild, **attributes: WebElementAttributeValue): return WebElement("big", children, attributes)
def blink(*children: WebElementChild, **attributes: WebElementAttributeValue): return WebElement("blink", children, attributes)
def center(*children: WebElementChild, **attributes: WebElementAttributeValue): return WebElement("center", children, attributes)
def dir(*children: WebElementChild, **attributes: WebElementAttributeValue): return WebElement("dir", children, attributes)
def font(*children: WebElementChild, **attributes: WebElementAttributeValue): return WebElement("font", children, attributes)
def frame(*children: WebElementChild, **attributes: WebElementAttributeValue): return WebElement("frame", children, attributes)
def frameset(*children: WebElementChild, **attributes: WebElementAttributeValue): return WebElement("frameset", children, attributes)
def image(*children: WebElementChild, **attributes: WebElementAttributeValue): return WebElement("image", children, attributes)
def keygen(*children: WebElementChild, **attributes: WebElementAttributeValue): return WebElement("keygen", children, attributes)
def marquee(*children: WebElementChild, **attributes: WebElementAttributeValue): return WebElement("marquee", children, attributes)
def menuitem(*children: WebElementChild, **attributes: WebElementAttributeValue): return WebElement("menuitem", children, attributes)
def nobr(*children: WebElementChild, **attributes: WebElementAttributeValue): return WebElement("nobr", children, attributes)
def noembed(*children: WebElementChild, **attributes: WebElementAttributeValue): return WebElement("noembed", children, attributes)
def noframes(*children: WebElementChild, **attributes: WebElementAttributeValue): return WebElement("noframes", children, attributes)
def param(*children: WebElementChild, **attributes: WebElementAttributeValue): return WebElement("param", children, attributes)
def plaintext(*children: WebElementChild, **attributes: WebElementAttributeValue): return WebElement("plaintext", children, attributes)
def rb(*children: WebElementChild, **attributes: WebElementAttributeValue): return WebElement("rb", children, attributes)
def rtc(*children: WebElementChild, **attributes: WebElementAttributeValue): return WebElement("rtc", children, attributes)
def spacer(*children: WebElementChild, **attributes: WebElementAttributeValue): return WebElement("spacer", children, attributes)
def strike(*children: WebElementChild, **attributes: WebElementAttributeValue): return WebElement("strike", children, attributes)
def tt(*children: WebElementChild, **attributes: WebElementAttributeValue): return WebElement("tt", children, attributes)
def xmp(*children: WebElementChild, **attributes: WebElementAttributeValue): return WebElement("xmp", children, attributes)