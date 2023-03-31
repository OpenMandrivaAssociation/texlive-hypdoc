Name:		texlive-hypdoc
Version:	63808
Release:	2
Summary:	Hyper extensions for doc.sty
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/hypdoc
License:	lppl1.3c
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/hypdoc.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/hypdoc.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/hypdoc.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This package adds hypertext features to the package doc that is
used in the documentation system of LaTeX2e. Bookmarks are
added and references are linked as far as possible.

%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%doc %{_texmfdistdir}/source/latex/hypdoc
%{_texmfdistdir}/tex/latex/hypdoc
%doc %{_texmfdistdir}/doc/latex/hypdoc

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
