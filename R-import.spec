#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-import
Version  : 1.1.0
Release  : 8
URL      : https://cran.r-project.org/src/contrib/import_1.1.0.tar.gz
Source0  : https://cran.r-project.org/src/contrib/import_1.1.0.tar.gz
Summary  : An Import Mechanism for R
Group    : Development/Tools
License  : MIT
BuildRequires : clr-R-helpers

%description
objects from packages. The syntax allows for importing multiple objects
  from a package with a single command in an expressive way. The import
  package bridges some of the gap between using library (or require) and
  direct (single-object) imports. Furthermore the imported objects are not
  placed in the current environment. It is also possible to import
  objects from stand-alone .R files. For more information, refer to
  the package vignette.

%prep
%setup -q -c -n import

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1523745930

%install
rm -rf %{buildroot}
export SOURCE_DATE_EPOCH=1523745930
export LANG=C
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=haswell -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library import
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=skylake-avx512 -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library import
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library import
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc -l %{buildroot}/usr/lib64/R/library import|| : 
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :


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
/usr/lib64/R/library/import/NEWS
/usr/lib64/R/library/import/R/import
/usr/lib64/R/library/import/R/import.rdb
/usr/lib64/R/library/import/R/import.rdx
/usr/lib64/R/library/import/doc/import.R
/usr/lib64/R/library/import/doc/import.Rmd
/usr/lib64/R/library/import/doc/import.html
/usr/lib64/R/library/import/doc/index.html
/usr/lib64/R/library/import/help/AnIndex
/usr/lib64/R/library/import/help/aliases.rds
/usr/lib64/R/library/import/help/import.rdb
/usr/lib64/R/library/import/help/import.rdx
/usr/lib64/R/library/import/help/paths.rds
/usr/lib64/R/library/import/html/00Index.html
/usr/lib64/R/library/import/html/R.css
