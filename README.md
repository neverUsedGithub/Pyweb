# Python web framework

This is a basic web framework created in python, that allows you to
create web apps without ever touching javascript.

# Examples

Take a look at `examples/app.py`.

# Installation

`pip install git+https://github.com/neverUsedGithub/Pyweb`

# Getting started

### Creating a page

To create a page you need to use the `app.page()` decorator.

```py
@app.page("/")
def index_page(request: Request):
    return (
        html.h1("Hello, World!")
    )
```

### Using event listeners

> Note: for now only the event listeners `onchecked` and `oninput`
> have any event information associated with them.

We are going to begin by adding a button.

```py
@app.page("/")
def index_page(request: Request):
    return (
        html.h1("Hello, World!"),
        html.button("Click me!")
    )
```

If you restart the server now you should see a button on your screen.
To add a click listener to our button we need to add a function to the
`onclick` attribute of the button.

```py
@app.page("/")
def index_page(request: Request):
    def clicked():
        print("Somebody clicked the button!")

    return (
        html.h1("Hello, World!"),
        html.button("Click me!")
    )
```

If you restart the server and click the button now, you should see a
message saying `Somebody clicked the button!` in your terminal.

> **But why in the terminal?**  
> The framework doesn't transpile your python code to javascript, but
> instead when an action happens on the client, it sends a WebSocket
> message to the server where the event listener is trigger and then
> the changed html is returned to the client.

### Using signals

Signals are one of the main ways to store state in the framework. All
signals must have an initial value.

```py
@app.page("/")
def index_page(request: Request):
    count = signal(0)

    return (
        html.h1("The count is ", count)
    )
```

If you run your app now you should see `The count is 0` on your screen.
You can modify a signal's value like this `my_signal(lambda current: ...)`.
Let's add a button to our site which we will increase the counter with.

```py
@app.page("/")
def index_page(request: Request):
    count = signal(0)

    def add_one():
        count(lambda current: current + 1)

    return (
        html.h1("The count is ", count),
        html.button(
            "Increase",
            onclick=add_one
        )
    )
```

If you now click the button, the counter should increase!

### Using the each and whether helpers

The framework provides two functions to help you write cleaner html,
these are `each` and `whether`.

#### each

`each` acts like a for loop but for your html content. Its parameters
are a signal or a function returning a list, and a mapper function
which maps all items inside of the list to a html element.

```py
@app.page("/")
def index_page(request: Request):
    tasks = signal([
        "do homework",
        "learn about python"
    ])

    return (
        html.h1("Your tasks are: "),
        each(tasks, lambda task, i: h3(task))
    )
```

#### whether

`whether` is for rendering things conditionally. It takes in a boolean
signal or a function returning a boolean, a function which renders when
the condition is truthy, and optionally a function which renders when
its not.

```py
@app.page("/")
def index_page(request: Request):
    count = signal(0)

    def add_one():
        count(lambda current: current + 1)

    return (
        html.h1("The count is ", count),
        html.button(
            "Increase",
            onclick=add_one
        ),

        whether(
            lambda: count.get() > 5,
            lambda: html.h1("The count is higher than 5!"),
            lambda: html.h1("Keep on clicking")
        )
    )
```

### Styling your webpage

You can style your pages using the `style` function. First, you will
have to declare your styles. This should be done in global scope or even
in a separate file.

```py
my_button_styles = style({
    "font-size": 20,
    "color": "red",

    ":hover": {
        "color": "blue"
    }
})
```

After declaring your styles navigate to your `app.page` decorater and
add the style in the page's `uses` parameter.

```py
@app.page("/", uses=[my_button_styles])
def index_page(request: Request):
    return (
        html.button("graphic design is my passion")
    )
```

But you are still not done. You will have to add a reference to your
style in your button element's `class_name`.

```py
@app.page("/", uses=[my_button_styles])
def index_page(request: Request):
    return (
        html.button(
            "graphic design is my passion",
            class_name=my_button_styles
        )
    )
```

After adding the `class_name`, restart your application and try out
your cool looking button!

> Note: you can combine your styles using the static method
> `Style.combine` or the method `style.add`.
>
> ```py
> first_style = style({ "color": "red" })
> second_style = style({ "font-size": 20 })
>
> combined_styles = first_style.add(second_style)
> # OR
> combined_styles = Style.combine(first_style, second_style)
> ```
