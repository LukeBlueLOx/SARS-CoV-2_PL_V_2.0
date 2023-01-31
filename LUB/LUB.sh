#! /bin/bash

cd scv2pl

git pull heroku main

git update-index --chmod=+x startupscript_1.sh
git update-index --chmod=+x startupscript_2.sh

git ls-files --stage

git status

git restore .

git commit -am "startupscripts ==> 100755 mode"

git push heroku main

shutdown +2
