Github static pelican plugin
===

Since I needed it for my personal blog, I made this tiny wrapper around the Github API.

Everytime you rebuild your pelican site, it will retrieves public repositories from [Github](https://github.com) using the [PyGithub](https://github.com/jacquev6/PyGithub) python library.

Dependency
---

You will need to install the `pygithub` using pip: `pip install pygithub`

Installation
---

Clone this repository using:

`git clone git@github.com:YuukanOO/pelican_github_static.git github_static`

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

### Basic

Once configured, you will be able to use the `github_repos` context variable in template pages like this:

```
<ul>
    {% for repo in github_repos %}
    <li><a href="{{ repo.html_url }}">{{ repo.full_name }}</a>: {{ repo.description }}</li>
    {% endfor %}
</ul>
```

### Advanced

If you need to split your repos between your own project and project you contributed to, use the `github_user_repos` and `github_forked_repos` context variable.

```
{% if "projects.md" in page.source_path %}
    <h2>My projects</h2>
    <ul>
        {% for repo in github_user_repos %}
        <li><a href="{{ repo.html_url }}">{{ repo.full_name }}</a>: {{ repo.description }}</li>
        {% endfor %}
    </ul>

    <h2>Projects I contributed to</h2>
    <ul>
        {% for repo in github_forked_repos %}
        <li><a href="{{ repo.html_url }}">{{ repo.full_name }}</a>: {{ repo.description }}</li>
        {% endfor %}
    </ul>
{% endif %}
```

Basically, it's just an array of [github.Repository.Repository](http://jacquev6.github.io/PyGithub/v1/github_objects/Repository.html#github.Repository.Repository) as returned by the Github API.