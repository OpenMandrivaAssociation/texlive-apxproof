%global tl_name apxproof
%global tl_revision 79251

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.4.1
Release:	%{tl_revision}.1
Summary:	Proofs in appendix
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/apxproof
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/apxproof.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/apxproof.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/apxproof.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
Requires(pre):	texlive-tlpkg
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package makes it easier to write articles where proofs and other
material are deferred to the appendix. The appendix material is written
in the LaTeX code along with the main text which it naturally
complements, and it is automatically deferred. The package can
automatically send proofs to the appendix, can repeat in the appendix
the theorem environments stated in the main text, can section the
appendix automatically based on the sectioning of the main text, and
supports a separate bibliography for the appendix material. It depends
on the following packages: amsthm, bibunits (if the bibliography option
is set to separate), environ, etoolbox, fancyvrb, ifthen, and kvoptions.

%prep
%setup -q -c -a1 -a2
rm -rf tlpkg
if [ -d RELOC ]; then
	cp -a RELOC/. .
	rm -rf RELOC
fi

%build

%install
mkdir -p %{buildroot}%{_datadir}/texmf-dist
# Flat tlnet layout: tex/ doc/ source/ fonts/ ... -> texmf-dist/
if [ -d texmf-dist ]; then
	cp -a texmf-dist/. %{buildroot}%{_datadir}/texmf-dist/
elif [ -d texmf ]; then
	mkdir -p %{buildroot}%{_datadir}/texmf
	cp -a texmf/. %{buildroot}%{_datadir}/texmf/
else
	for d in * .[!.]* ..?*; do
		[ -e "$d" ] || continue
		case "$d" in tlpkg|RELOC) continue ;; esac
		cp -a "$d" %{buildroot}%{_datadir}/texmf-dist/
	done
fi
rm -rf %{buildroot}%{_datadir}/texmf-dist/tlpkg

%files
%dir %{_datadir}/texmf-dist
%dir %{_datadir}/texmf-dist/doc
%dir %{_datadir}/texmf-dist/source
%dir %{_datadir}/texmf-dist/tex
%dir %{_datadir}/texmf-dist/doc/latex
%dir %{_datadir}/texmf-dist/source/latex
%dir %{_datadir}/texmf-dist/tex/latex
%dir %{_datadir}/texmf-dist/doc/latex/apxproof
%dir %{_datadir}/texmf-dist/source/latex/apxproof
%dir %{_datadir}/texmf-dist/tex/latex/apxproof
%doc %{_datadir}/texmf-dist/doc/latex/apxproof/LICENSE
%doc %{_datadir}/texmf-dist/doc/latex/apxproof/README.md
%doc %{_datadir}/texmf-dist/doc/latex/apxproof/apxproof.bib
%doc %{_datadir}/texmf-dist/doc/latex/apxproof/apxproof.pdf
%doc %{_datadir}/texmf-dist/source/latex/apxproof/apxproof.dtx
%doc %{_datadir}/texmf-dist/source/latex/apxproof/apxproof.ins
%{_datadir}/texmf-dist/tex/latex/apxproof/apxproof.sty
