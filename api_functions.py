from telegraphapi import Telegraph


def make_telegraf_page(images):
    telegraph = Telegraph()

    telegraph.createAccount("PythonTelegraphAPI")
    # page = telegraph.createPage("Hello world!", html_content="<b>Welcome, TelegraphAPI!</b>")

    tags_list = []
    for i in images:
        tags_list.append("<img src='{}'/>".format(i))

    content = '\n'.join(tags_list)
    page = telegraph.createPage("Недвижимость Харьков", html_content=content)

    return 'http://telegra.ph/{}'.format(page['path'])
