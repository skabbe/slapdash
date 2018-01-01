import dash_core_components as dcc
import dash_html_components as html

from .utils import component, get_url


@component
def Row(children=None, **kwargs):
    """A convenience component that makes a Bootstrap row"""
    return html.Div(children=children, className='row', **kwargs)


@component  
def Col(children=None, bp=None, size=None, **kwargs):
    """A convenience component that makes a Bootstrap column"""
    if size is None and bp is None:
        col_class = 'col'
    elif bp is None:
        col_class = f'col-{size}'
    else:        
        col_class = f'col-{bp}-{size}'

    return html.Div(children=children, className=col_class, **kwargs)


@component
def Navbar(items, home=None, orientation='top', active_path=None):
    li_className = 'nav-item'
    nav_items = []
    
    for path, text in items:
        href = get_url(path)
        is_active = href == active_path
        className = '{li_className} active' if is_active else li_className
        li = html.Li(
            className=className,
            children=dcc.Link(text, href=href, className='nav-link')
        )
        nav_items.append(li)
    return html.Nav(
        className=f'navbar {orientation}',
        children=[
            dcc.Link(home, className='home') if home else html.Div(),
            html.Ul(
                className='navigation',
                children=nav_items
            ),
        ]
    )


def Fa(name):
    """A convenience component for adding Font Awesome icons"""
    return html.I(className=f"fa {name}")
