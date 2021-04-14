---
title: Setup
---


## Requirements

* A GitHub account
* A working [Python 3.4+](https://www.python.org) environment to run the lesson initialization
  script
* (Optional) A local install of [bundler](https://bundler.io/) which will require the Ruby
  language to be installed.

## Setup for local rendering of the lessons (optional)

Though not essential, it is desirable to be able to preview changes on your own machine
before pushing them to GitHub.

In order to preview changes locally, you must install the software described below.

If you don't install bundler as indicated in this section, you will not be able to preview the
lessons locally (in other words, you won't be able to run `make serve` or `make site`).
However, you can still edit the files that make up the lessons. You will only be able to see the
changes once your edits have been merged in the main repository.

### Windows

For Windows, there are two main ways to setup your system to be able to render the lessons.

- Option 1 relies on the Windows Subsystem for Linux (WSL). WSL allows you to run a Linux
  environment directly from Windows.
- Option 2 relies on using Windows built-in applications.

## Option 1 - Using the Windows Subsystem for Linux (WSL)

If your version of Windows supports it, using the WSL will make the installation of the tools
needed easier. Instructions to install Linux distributions from Windows 10/Windows Server are
available from the [Microsoft website](https://docs.microsoft.com/en-us/windows/wsl/about).

Once you have installed a Linux distribution, you can follow the installation instructions for
[Linux](#linux-ubuntu) listed below. If you install a distribution other than Ubuntu, you will
need to adjust the commands that install the packages.


## Option 2 - Using Windows built-in applications

With the instructions below, you'll be able to preview websites for non-R based lessons. You'll be
able to do so from the Git Bash terminal or from the "Command Prompt with Ruby" that comes with
the Ruby installation. You won't be able to use the `make` commands as Make isn't available from
the Git Bash terminal (see the optional section below for more info).

1. **Ruby**, go to <https://rubyinstaller.org/> choose Ruby+DevKit for your
  system (typically x64), and the most recent version available. During the
  installation process, choose to install the MSYS2 toolchain. On the last step
  of the installation screen, make sure that "Run 'ridk install'" is checked.
  This will bring a terminal window with 3 options, press "Enter" (for the
  default installation). After this step completes, you'll be prompted again,
  and press "Enter" again (for the default option). Once the installation is
  complete, restart your system.

2. Navigate to the folder that contains the lesson, and you can now use `bundle
  exec jekyll serve` from your Git Bash terminal to preview the lessons.

### Optional (but recommended)

With these instructions, you'll be able to use the `make` commands and render all lessons
including those that use R. However, you won't be able to do so from the Git Bash terminal, but
from the other terminals (Windows Powershell, cmd.exe, or the Command Prompt with Ruby).

1. In the File Explorer, right-click on "This PC" icon, and click on
  "Properties". Click on "Advanced System Settings", and click on the button
  "Environment Variables". Click on the variable "Path", and then the "Edit"
  button. Click on the "New" button and add `C:\Ruby26-x64\msys64\usr\bin` (use
  the File Explorer to make sure this is the correct path for your Ruby and
  MSYS2 installation). If you're working on R-based lessons and R isn't already
  listed there, you need to add it by adding `C:\Program Files\R\R-3.x.x\bin`
  (using the correct path and R version number for your installation).

2. Open the "Command Prompt with Ruby" (if it was open before you edited the
  Path, close it and re-open it).


Regardless of the option you chose, go to the section [For Everyone](#for-everyone).

### macOS

1. First make sure you have Homebrew installed

To install Homebrew, open the [Homebrew website](https://brew.sh/) and copy/paste the first command
on that page into your Terminal. You may also want to check the requirements first. The command for
installing Homebrew will look something like:

```bash
  /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

 If you're not sure whether you have brew installed, type

```bash
  brew help
```

  If you have Homebrew installed, you should see something like:

```bash
  # Example usage:
  brew search [TEXT|/REGEX/]
  brew info [FORMULA...]
  brew install FORMULA...
  brew update
  brew upgrade [FORMULA...]
  brew uninstall FORMULA...
  brew list [FORMULA...]

# Troubleshooting:
  brew config
  brew doctor
  brew install --verbose --debug FORMULA

# Contributing:
  brew create [URL [--no-fetch]]
  brew edit [FORMULA...]

# Further help:
  brew commands
  brew help [COMMAND]
  man brew
  https://docs.brew.sh
```


2. **Ruby** -- `brew install ruby`

3. **bundler** -- `gem install bundler --user-install`

4. Go to the section [For Everyone](#for-everyone)

### Linux (Ubuntu)

1.  **[Ruby](https://www.ruby-lang.org/en/downloads/)** and other dependencies.

    You will need to have the following packages installed (some might already
    be on your system):

    ```bash
    sudo apt-get install ruby ruby-dev build-essential libxml2-dev
    ```

2. **[bundler](https://bundler.io/)**

    ```bash
    gem install bundler --user-install
    ```

    `gem` is the package management framework for Ruby. It was installed as part
    of Ruby in the step above. `bundler` is also a package manager but at the
    scale of a project instead of being system-wide. It makes it easier to
    manage dependencies.


### For Everyone

1. **The GitHub Pages Ruby Gem**

    Make sure there is a `Gemfile` at the root of your lesson repository. This
    file should only contain:

    ```bash
    source 'https://rubygems.org'
    gem 'github-pages', group: :jekyll_plugins
    ```

    If you don't have it, create it and the two lines above to it.

    At the root of your repository type

    ```bash
    bundle update
    ```

    If you haven't used `bundler` yet for your project, this command will
    install all the needed dependencies. Otherwise, it will update them to match
    the current versions used by GitHub Pages.

4. **Generate the lesson**

    Now you are ready to run jekyll to build your website and run a local server. To do this run:

    ```bash
    make serve
    ```

    There will be several lines of output after this. If there were errors or warnings you can use
    them to fix your lesson and run again if it failed. If it was successful the last few lines
    will include `Server address: http://127.0.0.1:4000` and `Server running... press ctrl-c to
    stop`. You can see your rendered site by pointing your browser to the address shown.

### For R-based lessons

You will need a recent version of R (>= 3.5.0). Installation instructions are available from the
[CRAN website](https://cran.r-project.org).

We use the [knitr][cran-knitr], and [remotes](https://cran.r-project.org/package=remotes) to format
lessons written in R Markdown and figure out needed packages to execute the code in the lesson. You
will need to install the `remotes` package to build R lessons (and this example lesson), the other
packages will be installed automatically during the rendering of the lesson. You can install this
package by opening an R terminal and typing:

```r
install.packages('remotes', repos = 'https://cran.rstudio.com')
```

### Troubleshooting

1. Check your version of Ruby:

   ```bash
   ruby -v
   ```

   You need Ruby 2.1.0 or later (currently GitHub pages uses Ruby 2.7.1). If you
   have an older version of Ruby, if possible upgrade your operating system to a
   more recent version. If it's not possible, consider using
   [rbenv](https://github.com/rbenv/rbenv).

    ```bash
    rbenv install 2.7.1
    ```

    And then instructing `rbenv` to use it in your lesson development process by
    executing the following command from your lesson directory:

    ```bash
    rbenv local 2.7.1
    ```

2.  **[RubyGems](https://rubygems.org/pages/download/)**
    is a tool which manages Ruby packages. It should have been installed along with Ruby and you can
    test your installation by running

    ```bash
    gem --version
    ```

3. If you want to run `bin/lesson_check.py` (which is invoked by `make lesson-check`)
you will need the [PyYAML](https://pypi.org/project/PyYAML/) module for Python 3.
