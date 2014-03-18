Github static pelican plugin
===

Since I needed it for my personal blog, I made this tiny wrapper around the Github API.

Everytime you rebuild your pelican site, it will retrieves public repositories from [Github](https://github.com) using the [PyGithub](https://github.com/jacquev6/PyGithub) python library.

Dependency
---

You will need to install the `pygithub` using pip: `pip install pygithub`

Installation
---

Just enable the plugin in your pelican settings:

```
PLUGINS = ["related_posts", "github_static"]
```

And provide your credentials:

```
GITHUB_USERNAME = u"Username"
GITHUB_PASSWORD = u"Password"
```

Usage
---

Once configured, you will be able to use the `github_repos` context variable in template pages like this:

```
<ul>
    {% for repo in github_repos %}
    <li><a href="{{ repo.html_url }}">{{ repo.full_name }}</a>: {{ repo.description }}</li>
    {% endfor %}
</ul>
```

Basically, it's just an array of [github.Repository.Repository](http://jacquev6.github.io/PyGithub/v1/github_objects/Repository.html#github.Repository.Repository) as returned by the Github API.