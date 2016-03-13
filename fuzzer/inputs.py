import requests


class FormInput:
    def __init__(self, url, tag):
        self.name = "FormInput"
        self.url = url
        self.tag = tag

    def submit(self, form_input):
        return requests.post(self.url, data=form_input, allow_redirects=True)

    def __str__(self):
        return self.name + ":\n\t" + str(self.url) + "\n\t" + str(self.tag)


class CookieInput:
    def __init__(self, url, cookie_key):
        pass

    def submit(self, vector):
        pass

    def __str__(self):
        return "CookieInput"


class URLParameterInput:
    def __init__(self, url, parameter_key):
        pass

    def submit(self, vector):
        pass

    def __str__(self):
        return "URLParameterInput"
