#!/usr/bin/env bash

player_status=$(playerctl status 2>/dev/null)

if [[ $player_status == "Playing" ]]; then
    text=" $(playerctl metadata --format '{{artist}} - {{title}}' 2>/dev/null)"
elif [[ $player_status == "Paused" ]]; then
    text=" $(playerctl metadata --format '{{artist}} - {{title}}' 2>/dev/null)"
else
    text=""
fi

echo "{\"text\":\"$text\",\"class\":\"music\"}"