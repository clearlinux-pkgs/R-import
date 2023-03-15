#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-import
Version  : 1.3.0
Release  : 44
URL      : https://cran.r-project.org/src/contrib/import_1.3.0.tar.gz
Source0  : https://cran.r-project.org/src/contrib/import_1.3.0.tar.gz
Summary  : An Import Mechanism for R
Group    : Development/Tools
License  : MIT
BuildRequires : buildreq-R

%description
and R modules. The syntax allows for importing multiple objects with a single
    command in an expressive way. The import package bridges some of the gap
    between using library (or require) and direct (single-object) imports.
    Furthermore the imported objects are not placed in the current environment.

%prep
%setup -q -c -n import
cd %{_builddir}/import

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1653342426

%install
export SOURCE_DATE_EPOCH=1653342426
rm -rf %{buildroot}
export LANG=C.UTF-8
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper" > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library import
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v4 -ftree-vectorize -mno-vzeroupper  " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library import
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library import
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc import || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/import/DESCRIPTION
/usr/lib64/R/library/import/INDEX
/usr/lib64/R/library/import/LICENSE
/usr/lib64/R/library/import/Meta/Rd.rds
/usr/lib64/R/library/import/Meta/features.rds
/usr/lib64/R/library/import/Meta/hsearch.rds
/usr/lib64/R/library/import/Meta/links.rds
/usr/lib64/R/library/import/Meta/nsInfo.rds
/usr/lib64/R/library/import/Meta/package.rds
/usr/lib64/R/library/import/Meta/vignette.rds
/usr/lib64/R/library/import/NAMESPACE
/usr/lib64/R/library/import/NEWS.md
/usr/lib64/R/library/import/R/import
/usr/lib64/R/library/import/R/import.rdb
/usr/lib64/R/library/import/R/import.rdx
/usr/lib64/R/library/import/WORDLIST
/usr/lib64/R/library/import/doc/import.R
/usr/lib64/R/library/import/doc/import.Rmd
/usr/lib64/R/library/import/doc/import.html
/usr/lib64/R/library/import/doc/index.html
/usr/lib64/R/library/import/help/AnIndex
/usr/lib64/R/library/import/help/aliases.rds
/usr/lib64/R/library/import/help/figures/lifecycle-archived.svg
/usr/lib64/R/library/import/help/figures/lifecycle-defunct.svg
/usr/lib64/R/library/import/help/figures/lifecycle-deprecated.svg
/usr/lib64/R/library/import/help/figures/lifecycle-experimental.svg
/usr/lib64/R/library/import/help/figures/lifecycle-maturing.svg
/usr/lib64/R/library/import/help/figures/lifecycle-questioning.svg
/usr/lib64/R/library/import/help/figures/lifecycle-stable.svg
/usr/lib64/R/library/import/help/figures/lifecycle-superseded.svg
/usr/lib64/R/library/import/help/import.rdb
/usr/lib64/R/library/import/help/import.rdx
/usr/lib64/R/library/import/help/paths.rds
/usr/lib64/R/library/import/html/00Index.html
/usr/lib64/R/library/import/html/R.css
/usr/lib64/R/library/import/tests/test_import/cleanup_environment.R
/usr/lib64/R/library/import/tests/test_import/module_S3.R
/usr/lib64/R/library/import/tests/test_import/module_base.R
/usr/lib64/R/library/import/tests/test_import/module_chdir/module_chdir.R
/usr/lib64/R/library/import/tests/test_import/module_hidden_objects.R
/usr/lib64/R/library/import/tests/test_import/module_recursive/src/run_me.R
/usr/lib64/R/library/import/tests/test_import/module_recursive/src/text.R
/usr/lib64/R/library/import/tests/test_import/module_recursive/src/title_text.R
/usr/lib64/R/library/import/tests/test_import/module_recursive/src/title_text_here.R
/usr/lib64/R/library/import/tests/test_import/module_recursive/src/to_title.R
/usr/lib64/R/library/import/tests/test_import/module_recursive_inner.R
/usr/lib64/R/library/import/tests/test_import/module_recursive_library.R
/usr/lib64/R/library/import/tests/test_import/module_recursive_outer_from.R
/usr/lib64/R/library/import/tests/test_import/module_recursive_outer_here.R
/usr/lib64/R/library/import/tests/test_import/module_recursive_package_from.R
/usr/lib64/R/library/import/tests/test_import/module_recursive_package_here.R
/usr/lib64/R/library/import/tests/test_import/packageToTest/DESCRIPTION
/usr/lib64/R/library/import/tests/test_import/packageToTest/NAMESPACE
/usr/lib64/R/library/import/tests/test_import/packageToTest/R/get.R
/usr/lib64/R/library/import/tests/test_import/packageToTest/R/hello.R
/usr/lib64/R/library/import/tests/test_import/packageToTest/man/get.Rd
/usr/lib64/R/library/import/tests/test_import/packageToTest/man/hello.Rd
/usr/lib64/R/library/import/tests/test_import/packageToTest_0.1.0.tar.gz
/usr/lib64/R/library/import/tests/test_import/skipped_test_module_urls.R
/usr/lib64/R/library/import/tests/test_import/test_S3.R
/usr/lib64/R/library/import/tests/test_import/test_basetemplate.R
/usr/lib64/R/library/import/tests/test_import/test_from.R
/usr/lib64/R/library/import/tests/test_import/test_hidden_objects.R
/usr/lib64/R/library/import/tests/test_import/test_into_and_here.R
/usr/lib64/R/library/import/tests/test_import/test_into_param.R
/usr/lib64/R/library/import/tests/test_import/test_module_directories.R
/usr/lib64/R/library/import/tests/test_import/test_module_recursive.R
/usr/lib64/R/library/import/tests/testthat.R
/usr/lib64/R/library/import/tests/testthat/test_import.R
