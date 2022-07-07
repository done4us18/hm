# cyan/yellow/orange (256 color)
PS1='${debian_chroot:+($debian_chroot)}\[\033[38;2;72;201;176m\]\u\[\033[00m\]\[\033[38;2;220;118;51m\]@\[\033[00m\]\[\033[38;2;244;208;63m\]\h\[\033[00m\]:\[\033[38;2;220;118;51m\]\w\[\033[00m\]\$ '

# 3-tone green; tput
PS1='\[$(tput setaf 34; tput bold; tput rev)\]\u@\[$(tput setaf 70)\]\h🗄\[$(tput setaf 106)\]  \w \[$(tput sgr0)\]💲 '

# tput bold, setaf, setab
FGBG1="\[$(tput bold; tput setaf 3; tput setab 4)\]"
FGBG2="\[$(tput bold; tput setaf 4; tput setab 3)\]"
RESET="\[$(tput sgr0)\]"
export PS1="${FGBG1} \u:${FGBG2} \w ${RESET} 🤓 \$ "

# blue gemstone theme
export PS1="\[\e[0;36;44m\]\u💎\[\e[7m\]\w\[\e[0m\]\[\e[0;38m\]\$ \[\e[0m\]"

# blue gemstone theme (Python os)
export PS1="\[\e[36;44m\]$(echo -e "import os;print(os.getlogin())" | python3)\[\e[0m\]💎\[\e[34;46m\]\w\[\e[0m\]\\$ "
