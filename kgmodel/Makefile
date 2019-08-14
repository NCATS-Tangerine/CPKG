
# ----------------------------------------
# TOP LEVEL TARGETS
# ----------------------------------------
all: install build

install: env.lock

build: clinicalprofiles.py docs/index.md clinicalprofiles.shex


# ---------------------------------------
# Install package into build environment
# ---------------------------------------
env.lock:
	pipenv install --dev
	cp /dev/null env.lock


# ----------------------------------------
# BUILD/COMPILATION
# ----------------------------------------
# ~~~~~~~~~~~~~~~~~~~~
# Python
# ~~~~~~~~~~~~~~~~~~~~
clinicalprofiles.py: clinicalprofiles.yaml env.lock
	pipenv run gen-py-classes $< > tmp.py && pipenv run python tmp.py &&  (pipenv run comparefiles tmp.py $@ && cp $@ $@-PREV && cp tmp.py $@); rm tmp.py

# ~~~~~~~~~~~~~~~~~~~~
# DOCS
# ~~~~~~~~~~~~~~~~~~~~
docs/index.md: clinicalprofiles.yaml env.lock
	pipenv run gen-markdown --dir docs $<

# ~~~~~~~~~~~~~~~~~~~~
# ShEx
# ~~~~~~~~~~~~~~~~~~~~
clinicalprofiles.shex: clinicalprofiles.yaml env.lock
	pipenv run gen-shex $< > $@


# ----------------------------------------
# CLEAN
# ----------------------------------------
clean:
	rm -rf docs/* clinicalprofiles.py clinicalprofiles.shex
	rm -f env.lock
	pipenv --rm
