# Ansible Role: Dotfiles

Installs a set of dotfiles from a given Git repostiory. By default it will use my [dotfiles repo][dotfiles] but you can easily change it to use yours.
Works for all dotfile repos that follow the [stow][stow] format.

## Usage

1. Change the `dotfiles_repo` variable in `defaults/main.yml` to point to your dotfiles repo
2. Create a playbook with this Role
3. Run the playbook

## Dependencies

None

## Example playbook

```
---
- hosts: localhost
  roles:
    - { role: mariuskimmina.dotfiles }
  become: true
```


## Tests

Fully tested on:

* Fedora 36
* Ubuntu 20.04

## Credits

Inspired by: https://github.com/geerlingguy/ansible-role-dotfiles
The main difference between the original project and this one is the usage of [stow][stow].

[stow]: https://www.gnu.org/software/stow/
[dotfiles]: https://github.com/mariuskimmina/.dotfiles
