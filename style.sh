#!/bin/bash

## Author      : Rohit Raj
## Instagram   : @done4us18
## Github      : done4us

## t-style installer script

## ANSI Colors (FG & BG)

red="$(printf '\033[31m')"
green="$(printf '\033[32m')"
orange="$(printf '\033[33m')"
blue="$(printf '\033[34m')"
magenta="$(printf '\033[35m')"
cyan="$(printf '\033[36m')"
white="$(printf '\033[37m')"
black="$(printf '\033[30m')"
redbg="$(printf '\033[41m')"
greenbg="$(printf '\033[42m')"
orangebg="$(printf '\033[43m')"
bluebg="$(printf '\033[44m')"
magentabg="$(printf '\033[45m')"
cyanbg="$(printf '\033[46m')"
whitebg="$(printf '\033[47m')"
blackbg="$(printf '\033[40m')"
defaultfg="$(printf '\033[39m')"
defaultbg="$(printf '\033[49m')"

## Directories
PREFIX='/data/data/com.termux/files/usr'
termux_dir="$HOME/.termux"

## Banner
banner () {
      clear
      echo "
     ${blue}┌──────────────────────────────────────────────────┐
     ${blue}│${red}░▀█▀░█▀▀░█▀▄░█▄█░█░█░█░█${orange}░░░░░${green}█▀▀░▀█▀░█░█░█░░░█▀▀░░${blue}│
     ${blue}│${red}░░█░░█▀▀░█▀▄░█░█░█░█░▄▀▄${orange}░▄▄▄${red}░${green}▀▀█░░█░░░█░░█░░░█▀▀░░${blue}│
     ${blue}│${red}░░▀░░▀▀▀░▀░▀░▀░▀░▀▀▀░▀░▀${orange}░░░░░${green}▀▀▀░░▀░░░▀░░▀▀▀░▀▀▀░░${blue}│
     ${blue}└──────────────────────────────────────────────────┘
     ${blue}[${red}*${blue}] ${orange}By- Rohit Raj ${red}//${orange} done4us"
}



banner
