# -*- coding: utf8 -*-
from github import Github
from pelican import signals

def github_fetch_repos(generator):
    """
    Fetch user repositories and returns a list of repository object as returned
    by the underlying github bridge.
    """
    all_repos = [repo for repo in generator.github_instance.get_user().get_repos(type = "public")]

    generator.context["github_repos"] = all_repos
    generator.context["github_user_repos"] = [repo for repo in all_repos if repo.fork == False]
    generator.context["github_forked_repos"] = [repo for repo in all_repos if repo.fork == True]

def github_initialization(generator):
    """
    Connect to github and creates the github main object.
    """
    username = generator.settings.get(u"GITHUB_USERNAME")
    password = generator.settings.get(u"GITHUB_PASSWORD")

    generator.github_instance = Github(username, password)

def register():
    """
    Plugin registration
    """
    try:
        signals.page_generator_init.connect(github_initialization)
        signals.page_generator_finalized.connect(github_fetch_repos)
    except ImportError:
        logger.warning('`github_static` failed to load dependency `pygithub`.'
                       '`github_static` plugin not loaded.')