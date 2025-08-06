#
# ~/.bashrc
#

# If not running interactively, don't do anything
[[ $- != *i* ]] && return

# Alias
alias ls='ls -lahX --color=auto --group-directories-first'
alias grep='grep --color=auto'
alias venvo='source .venv/bin/activate'

# Prompt
PS1="\[\e[30;44m\]\t\[\e[m\] \[\e[32m\][\[\e[m\]\[\e[32m\]\u\[\e[m\]\[\e[32m\]@\[\e[m\]\[\e[32m\]\h\[\e[m\]\[\e[32m\]]\[\e[m\] \[\e[30;43m\]\w\[\e[m\]\n\$ "
