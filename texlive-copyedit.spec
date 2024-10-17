Name:		texlive-copyedit
Version:	37928
Release:	2
Summary:	Copyediting support for LaTeX documents
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/copyedit
License:	lppl1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/copyedit.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/copyedit.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/copyedit.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This package implements copyediting support for LaTeX
documents. Authors can enjoy the freedom of using, for example,
words with US or UK or Canadian or Australian spelling in a
mixed way, yet, they can choose any one of the usage forms for
their entire document irrespective of kinds of spelling they
have adopted. In the same fashion, the users can have the
benefit of the following features available in the package:
Localization -- British-American-Australian-Canadian Close-up,
Hyphenation, and Spaced words Latin abbreviations Acronyms and
Abbreviations Itemization, nonlocal lists and labels
Parenthetical and serial commas Non-local tokenization in
language through Abbreviations and pronouns.

%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%doc %{_texmfdistdir}/source/latex/copyedit
%{_texmfdistdir}/tex/latex/copyedit
%doc %{_texmfdistdir}/doc/latex/copyedit

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
