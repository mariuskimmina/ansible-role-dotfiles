# Ansible Role: Dotfiles

Installs a set of dotfiles from a given Git repostiory. By default it will use my [dotfiles repo][dotfiles] but you can easily change it to use yours.
Works for all dotfile repos that follow the [stow][stow] format.

## Usage

1. Change the `dotfiles_repo` variable in `defaults/main.yml` to point to your dotfiles repo
2. TBD

## Requirements

Requires `git` to be installed on the maschine

## Dependencies

None

## Credits

Inspired by: https://github.com/geerlingguy/ansible-role-dotfiles
The main difference between the original project and this one is the usage of [stow][stow].

[stow]: https://www.gnu.org/software/stow/
[dotfiles]: https://github.com/mariuskimmina/.dotfiles
