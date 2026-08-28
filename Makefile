RELEASE = 1.1.4

clean:
	$(info -> Makefile: cleanup previous builds ... )
	@(rm -rf dist build .venv uv.lock)

release:
	$(info -> Makefile: validating RELEASE=${RELEASE} format)
	@(echo ${RELEASE} | grep -qE "[0-9]+\.[0-9]+\.*[0-9]*[a-zA-Z]*[0-9]*") || (echo " ${RELEASE} is not in compliance with our version format"; exit 1)	
	@(sed -i -E "s/version = \"[0-9]+.[0-9]+\.*[0-9]+[a-zA-Z]*[0-9]*\"/version = \"${RELEASE}\"/g" pyproject.toml)

bdist: release clean
	$(info -> Makefile: building the bdist distribution package ...)
	@(	uv build && \
		uv add --dev check-wheel-contents && \
		uv run check-wheel-contents dist/*.whl )

rpm: bdist
	$(info -> Makefile: packaging as RPM ...)
	[ -d ~/rpmbuild ] || mkdir ~/rpmbuild
	[ -d ~/rpmbuild/SOURCES ] || mkdir ~/rpmbuild/SOURCES
	[ -d ~/rpmbuild/SPECS ] || mkdir ~/rpmbuild/SPECS
	mv -f dist/py2srbcyr-${RELEASE}* ~/rpmbuild/SOURCES/
	cp -f cli/*.py ~/rpmbuild/SOURCES/
	rpmbuild --define "_version ${RELEASE}" -bb rpmspec/py2srbcyr.spec
