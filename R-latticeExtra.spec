#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-latticeExtra
Version  : 0.6.29
Release  : 42
URL      : https://cran.r-project.org/src/contrib/latticeExtra_0.6-29.tar.gz
Source0  : https://cran.r-project.org/src/contrib/latticeExtra_0.6-29.tar.gz
Summary  : Extra Graphical Utilities Based on Lattice
Group    : Development/Tools
License  : GPL-2.0+
Requires: R-RColorBrewer
Requires: R-jpeg
Requires: R-png
BuildRequires : R-RColorBrewer
BuildRequires : R-jpeg
BuildRequires : R-png
BuildRequires : buildreq-R

%description
package, this package provides several new high-level
	     functions and methods, as well as additional utilities
	     such as panel and axis annotation functions.

%prep
%setup -q -c -n latticeExtra
cd %{_builddir}/latticeExtra

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1641044393

%install
export SOURCE_DATE_EPOCH=1641044393
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
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library latticeExtra
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v4 -ftree-vectorize -mno-vzeroupper  " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library latticeExtra
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library latticeExtra
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc latticeExtra || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/latticeExtra/DESCRIPTION
/usr/lib64/R/library/latticeExtra/INDEX
/usr/lib64/R/library/latticeExtra/Meta/Rd.rds
/usr/lib64/R/library/latticeExtra/Meta/data.rds
/usr/lib64/R/library/latticeExtra/Meta/features.rds
/usr/lib64/R/library/latticeExtra/Meta/hsearch.rds
/usr/lib64/R/library/latticeExtra/Meta/links.rds
/usr/lib64/R/library/latticeExtra/Meta/nsInfo.rds
/usr/lib64/R/library/latticeExtra/Meta/package.rds
/usr/lib64/R/library/latticeExtra/NAMESPACE
/usr/lib64/R/library/latticeExtra/NEWS
/usr/lib64/R/library/latticeExtra/R/latticeExtra
/usr/lib64/R/library/latticeExtra/R/latticeExtra.rdb
/usr/lib64/R/library/latticeExtra/R/latticeExtra.rdx
/usr/lib64/R/library/latticeExtra/data/Rdata.rdb
/usr/lib64/R/library/latticeExtra/data/Rdata.rds
/usr/lib64/R/library/latticeExtra/data/Rdata.rdx
/usr/lib64/R/library/latticeExtra/help/AnIndex
/usr/lib64/R/library/latticeExtra/help/aliases.rds
/usr/lib64/R/library/latticeExtra/help/latticeExtra.rdb
/usr/lib64/R/library/latticeExtra/help/latticeExtra.rdx
/usr/lib64/R/library/latticeExtra/help/paths.rds
/usr/lib64/R/library/latticeExtra/html/00Index.html
/usr/lib64/R/library/latticeExtra/html/R.css
/usr/lib64/R/library/latticeExtra/scripts/README.USAge
/usr/lib64/R/library/latticeExtra/tests/layer.R
