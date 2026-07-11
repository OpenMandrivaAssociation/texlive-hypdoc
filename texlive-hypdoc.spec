%global tl_name hypdoc
%global tl_revision 79461

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.19
Release:	%{tl_revision}.1
Summary:	Hyper extensions for doc.sty
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/hypdoc
License:	lppl1.3c
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/hypdoc.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/hypdoc.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/hypdoc.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This package adds hypertext features to the package doc that is used in
the documentation system of LaTeX2e. Bookmarks are added and references
are linked as far as possible.

