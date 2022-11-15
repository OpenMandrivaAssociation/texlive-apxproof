Name:		texlive-apxproof
Version:	64715
Release:	1
Summary:	Proofs in appendix
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/apxproof
License:	lppl1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/apxproof.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/apxproof.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/apxproof.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package makes it easier to write articles where proofs and
other material are deferred to the appendix. The appendix
material is written in the LaTeX code along with the main text
which it naturally complements, and it is automatically
deferred. The package can automatically send proofs to the
appendix, can repeat in the appendix the theorem environments
stated in the main text, can section the appendix automatically
based on the sectioning of the main text, and supports a
separate bibliography for the appendix material. It depends on
the following other packages: amsthm, bibunits (if the
bibliography option is set to separate), environ, etoolbox,
fancyvrb, ifthen, and kvoptions.

%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%doc %{_texmfdistdir}/source/latex/apxproof
%{_texmfdistdir}/tex/latex/apxproof
%doc %{_texmfdistdir}/doc/latex/apxproof

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
