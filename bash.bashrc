if [ -x /data/data/com.termux/files/usr/libexec/termux/command-not-found ]; then
command_not_found_handle() {
/data/data/com.termux/files/usr/libexec/termux/command-not-found 
}
fi
#PS1='\w $ '

PS1='\033[1;34m\]╭───\[\033[1;31m\]≼\[\033[1;33m\]Mr. Rohit\[\033[1;34m\]•\[\033[1;30m\]\w\[\033[1;31m\]≽
\[\033[1;34m\]╰──╼\[\033[1;31m\]✠\[\033[1;32m\] '

clear

alias a=alias
alias c=clear
alias py=python
alias ba=bash
