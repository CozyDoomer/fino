# Release Checklist

* [ ] Get master to the appropriate code release state. [Travis CI](https://travis-ci.org/hugovk/fino) should be running cleanly for all merges to master.
* [ ] Update version in `setup.py` and commit:
```bash
git checkout master
edit setup.py
git add setup.py
git commit -m "Release 0.3.0"
```
* [ ] Tag the last commit with the version number:
```bash
git tag -a 0.3.0 -m "Release 0.3.0"
```
* [ ] Release on PyPI:
```bash
python setup.py register
python setup.py sdist --format=gztar upload
```
* [ ] Push: `git push`
* [ ] Push tags: `git push --tags`
* [ ] Create new GitHub release: https://github.com/hugovk/fino/releases/new
* [ ] Update develop branch from master:
```bash
git checkout develop
git merge master --ff-only
git push
```
