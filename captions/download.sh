#!/bin/bash
yt-dlp --skip-download --write-auto-sub --sub-lang en --sub-format json3 -o '%(upload_date)s__%(id)s__%(title)s.%(ext)s' $@
