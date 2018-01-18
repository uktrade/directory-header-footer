#!/bin/bash
REPOS="
../directory-sso
../directory-sso-profile
../help
../directory-ui-buyer
../directory-ui-export-readiness
../navigator"
IFS= read -r -p "Enter commit message: " commitmsg
for dir in $REPOS; do
	echo "Switching to repo $dir"
	cd $dir
	git add -A
	git commit -m "$commitmsg"
	git push -u origin $(git rev-parse --abbrev-ref HEAD)
done
